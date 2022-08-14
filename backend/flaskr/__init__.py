import os
from unicodedata import category
import werkzeug
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import math

import werkzeug

from models import setup_db, Question, Category, db
from utils.helper import convertRowToObject, convertTableToList
QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    cors = CORS(app)
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, PUT, OPTIONS')
        return response
    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available questions.
    """
    @app.route('/questions/all', methods=['GET'])
    def getAllQuestions():
        listQuestions = Question.query.all()
        listObj = convertTableToList(listQuestions)

        return jsonify({
            'success':True,
            'questions':listObj,
            'totalQuestions':len(listObj)
        })
    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions', methods=['GET'])
    def getQuestionsByPage():
        page = int(request.args.get('page', 1, type=int))
        if(page<=0):
            return "Bad request!", 400
        size = 10
        start = (page-1) * size
        end = start + size
        questions = Question.query.all()
        paginateQuestion = [question.format() for question in questions]
        categories = Category.query.all()
        listCategoryObj = convertTableToList(categories)
        return jsonify({
            'success': True,
            'questions': paginateQuestion[start:end],
            'total_questions': len(paginateQuestion),
            'totalPage':math.ceil(len(paginateQuestion)/size),
            'categories':listCategoryObj,
            'current_category':listCategoryObj
            })
    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def deleteQuestion(id):
        if(not id):
             return "Bad request!", 400
        
        try:
            Question.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            abort(500)
            return
        #delete successful    
        return jsonify({
                "success": True
            })
    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route("/questions", methods=['POST'])
    def addNewQuestion():
        data = request.json
        question = data["question"]
        answer = data["answer"]
        category = data["category"]
        difficulty = data["difficulty"]

        try:
                questionObj = Question(question, answer, category, difficulty)
                db.session.add(questionObj)
                db.session.commit()
                returnQuestion = convertRowToObject(questionObj)
                return jsonify({
                    "success": True,
                    "question": returnQuestion
                })
        except:
            abort(500, "server error")
            return

        
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route("/questions/search", methods=["POST"])
    def searchQuestion():
        searchTerm = request.json["searchTerm"]
        if searchTerm:
        
            listQuestions = Question.query.filter(Question.question.like('%' + searchTerm + '%')).all()
            resultObject = convertTableToList(listQuestions)
            category = Category.query.all()
            listCategoryObj = convertTableToList(category)

            return jsonify({
                "success": True,
                "questions": resultObject,
                "totalQuestions": len(resultObject),
                "currentCategory": listCategoryObj
            })
        abort(404)
    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route("/categories/<int:id>/questions")
    def getQuestionsByCategory(id):
        questions = Question.query.filter_by(category=id).all()
        category = Category.query.filter_by(id=id).all()

        listCategoryObj = convertTableToList(category)
        listQuestionObj = convertTableToList(questions)

        return jsonify({
            "success": True,
            "questions": listQuestionObj,
            "totalQuestions": len(listQuestionObj),
            "currentCategory": listCategoryObj
        })
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def getQuestionOfQuizzes():
        try:

            data = request.get_json()
            category = data.get('quiz_category')
            previous_questions = data.get('previous_questions')
            if not ('quiz_category' in data and 'previous_questions' in data):
                abort(404)

            if category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)).all()
            else:
                available_questions = Question.query.filter_by(
                    category=category['id']).filter(
                    Question.id.notin_(
                        previous_questions)).all()

            new_question = available_questions[random.randrange(
                0, len(available_questions))].format() if \
                len(available_questions) > 0 else None

            return jsonify({
                'success': True,
                'question': new_question
            })
        except BaseException:
            abort(404)

             

    @app.route('/categories', methods=['GET'])
    def getAllCategories():
        listCategory = Category.query.all()
        if len(listCategory ) == 0:
            abort(404)
        listObj = convertTableToList(listCategory)

        return jsonify({
            'success': True,
            'categories': listObj
        })
        

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    def handle_bad_request(e):
        return 'Bad request!', 400
    app.register_error_handler(400, handle_bad_request)

    def handle_not_found(e):
        return 'Not found!!!!', 404
    app.register_error_handler(404, handle_not_found)

    def handle_422(e):
        return 'Unprocessable Entity!!!!', 404
    app.register_error_handler(422, handle_422)

    def handle_server_error(e):
        return 'Something went wrong with server', 500
    app.register_error_handler(500, handle_server_error)

    return app