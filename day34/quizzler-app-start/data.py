import requests

parameters = {
    'type': 'boolean',
    'amount': 10,
    'category': 15,
    'difficulty':'medium'
}

trivia_questions = requests.get("https://opentdb.com/api.php", params=parameters)
trivia_questions.raise_for_status()

question_data = trivia_questions.json()['results']
