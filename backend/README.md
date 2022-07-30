# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "categories": [
    { "id": 1, "type": "Science" },
    { "id": 2, "type": "Art" },
    { "id": 3, "type": "Geography" },
    { "id": 4, "type": "History" },
    { "id": 5, "type": "Entertainment" },
    { "id": 6, "type": "Sports" }
  ],
  "success": true
}
```

`GET '/questions/all'`

- Get all question
- Returns: An Object with keys `questions`, that contains an list of object questions and keys `totalQuestions` that reflect the total number of questions

```json
{
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled I Know Why the Caged Bird Sings?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer s original name is Cassius Clay?"
    },
    {
      "answer": "Apollo",
      "category": 5,
      "difficulty": 134,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ],
  "success": true,
  "totalQuestions": 3
}
```

`GET '/questions'`

- Get the question by page number. For example : `/questions?page=1`
- Returns: An object with keys `questions` containing the question and key `total_questions` containing the total number of questions (default 10 items) and other information
- if page <= 0 return 400 bad request
- Example:

```json
{
  "categories": [
    { "id": 1, "type": "Science" },
    { "id": 2, "type": "Art" },
    { "id": 3, "type": "Geography" },
    { "id": 4, "type": "History" },
    { "id": 5, "type": "Entertainment" },
    { "id": 6, "type": "Sports" }
  ],
  "current_category": [
    { "id": 1, "type": "Science" },
    { "id": 2, "type": "Art" },
    { "id": 3, "type": "Geography" },
    { "id": 4, "type": "History" },
    { "id": 5, "type": "Entertainment" },
    { "id": 6, "type": "Sports" }
  ],
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled I Know Why the Caged Bird Sings?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer s original name is Cassius Clay?"
    },
    {
      "answer": "Apollo",
      "category": 5,
      "difficulty": 134,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "totalPage": 4,
  "total_questions": 34
}
```

`DELETE '/questions/<int:id>`
- remove question by id
- Returns: An Object with keys success is true when delete success
- return 400 if id is zero
- return 404 if id is not a positive integer
Example for success:
```json
{"success":true}
```

`POST '/questions'`
- Add new question to database with payload in request
- The payload like: 
```json
{
  "question": "how old are you",
  "answer": "18",
  "difficulty": 1,
  "category": 1
}
```
and the success case: 
```json
{
  "answer": "18",
  "category": 1,
  "difficulty": 1,
  "id": 41,
  "question": "how old are you"
}
```
- In case any property in payload is null, the response is 400

`POST '/questions/search'`
- Get the question with search key in payload of request
- Returns: An object containing the list of questions found
Example:
Payload: 
```json
{
  "searchTerm": "Whose autobiography"
}
```
and success response: 
```json
{
  "currentCategory": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled I Know Why the Caged Bird Sings?"
    }
  ],
  "success": true,
  "totalQuestions": 1
}
```

`GET '/categories/<int:id>/questions'`
- Get the question by category
`id` is the id of the category
Return: an object containing the list of questions and total questions
Example: 
```json
{
  "currentCategory": [
    {
      "id": 3,
      "type": "Geography"
    }
  ],
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "totalQuestions": 3
}
```

`POST '/quizzes'`
- get a random question for the quiz
- You need send the payload like this:
```json
{
  "previous_questions": [
    15
  ],
  "quiz_category": {
    "type": "Geography",
    "id": 3
  }
}
```
and then the success response:
```json
{
  "question": {
    "answer": "Lake Victoria",
    "category": 3,
    "difficulty": 2,
    "id": 13,
    "question": "What is the largest lake in Africa?"
  },
  "success": true
}
```


## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
