import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "mydb"
        self.database_path = "postgresql://{}/{}".format('baoson@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
        self.newQuestion={
            "question": "How old are you ?",
            "answer":"18",
            "category": 1,
            "difficulty":2,
        }

        self.payloadSearch={
            "searchTerm": "How old",
        }

        self.payloadGetQuiz = {
            "previous_questions":[15],
            "quiz_category":
                {
                    "type":"Geography",
                    "id":3
                }
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_all_question(self):
        res = self.client().get('/questions/all')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))


    def test_get_pagination_question(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["totalPage"])
        self.assertTrue(len(data["categories"]))
        self.assertTrue(len(data["current_category"]))

    def test_400_pagination_question(self):
        res = self.client().get('/questions?page=-1')
        self.assertEqual(res.status_code, 400)
    

    def test_delete_question(self):
        res = self.client().delete('/questions/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_400_delete_question_(self):
        res = self.client().delete('/questions/0')
        self.assertEqual(res.status_code,400)
    
    def test_404_delete_question(self):
        res = self.client().delete('/questions/')
        self.assertEqual(res.status_code,404)
    

    def test_create_question(self):
        res = self.client().post('/questions', json=self.newQuestion)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_search_question(self):
        res = self.client().post('/questions/search', json=self.payloadSearch)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))

    def test_get_question_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(len(data["currentCategory"]))

    def test_get_404_questions(self):
        res = self.client().get('/categories/-1/questions')
        self.assertEqual(res.status_code,404)

    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["categories"]))


    def test_get_quiz(self):
        res = self.client().post('/quizzes', json=self.payloadGetQuiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()