import json
import requests
import pickle

class Questions:

    def __init__(self,category,level,question,correct_answer,incorrect_answers):
        self.category = category
        self.level = level
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answers
        self.isAsk = False


def selectQuestion(list,level):
    for question in list:
        if question.level == level and not question.isAsk:
            return question

def QuestionList(category):
    question_list = []

    science_URL = "https://opentdb.com/api.php?amount=50&type=multiple"
    sports_URL = "https://opentdb.com/api.php?amount=50&category=21&type=multiple"
    history_URL = "https://opentdb.com/api.php?amount=50&category=23&type=multiple"

    API_URL = "https://opentdb.com/api.php?amount=50&type=multiple" #default

    if category == "science":
        API_URL = science_URL
    elif category == "sports":
        API_URL = sports_URL
    elif category == "history":
        API_URL = history_URL

    response = requests.get(API_URL)
    questionsResponse = response.json()

    for i in questionsResponse['results']:
        question = Questions(i['category'],i['difficulty'],i['question'],i['correct_answer'],i['incorrect_answers'])
        question_list.append(question)

    return question_list



list = QuestionList("sports")

with open('fileSports.pickle', 'wb') as questionList:
    pickle.dump(list, questionList)

with open('fileSports.pickle', 'rb') as questionList:
    result = pickle.load(questionList)
