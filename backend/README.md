# Udacity_PJ2
 Project Trivia API
Trivia is a Questions and Answers application
Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

#API documents:
## 1/
GET "/categories"

Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
Request Parameters: None
Response Body: List dict categories ( id + type) + success value.
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
## 2/
`GET '/questions'`

Get the question by page number
Returns: An object with keys `questions` containing the question and key `total_questions` containing the total number of questions (default 10 items) and other information.
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
  ],
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": str,
      "difficulty": str,
      "id": int,
      "question": str
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer s original name is Cassius Clay?"
    },
  ],
  "success": true,
  "totalPage": n,
  "total_questions": n
}
```
## 3/
`DELETE '/questions/<int:id>`
Remove a question by id

## 4/
`POST '/questions'`
Add new question to database with data in payload
- The payload format: 
```json
{
  "question": str,
  "answer": str,
  "difficulty": int,
  "category": int
}
```
## 5/
`POST '/questions/search'`
Get the question with search key
Returns list of questions found
```json
  "questions": [
    {
      "answer": str,
      "category": int,
      "difficulty": int,
      "id": int,
      "question": str
    }
  ],
  "success": true,
  "totalQuestions": 1
```
## 6/
 `GET '/categories/<int:id>/questions'`
 
- Get the question by category
Return list of questions and total questions

## 7/
`POST '/quizzes'`

Get a random question for the quiz.
