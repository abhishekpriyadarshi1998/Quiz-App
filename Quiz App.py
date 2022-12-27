import json
import random 

#Create a JSON File

questions = {
    "questions" : [
        {
        "question" : "What is the capital of India?",
        "option1" : "Mumbai",
        "option2" : "Delhi",
        "option3" : "Kolkata",
        "option4" : "Chennai",
        "answer"  : "2"
        },
        {
        "question" : "What is the capital of USA?",
        "option1" : "New York",
        "option2" : "Washington DC",
        "option3" : "Los Angeles",
        "option4" : "Dallas",
        "answer"  : "2"
        },
        {
        "question" : "What is the capital of China?",
        "option1" : "Beijing",
        "option2" : "Shanghai",
        "option3" : "Hong Kong",
        "option4" : "Taipei",
        "answer"  : "1"
        },
        {
        "question" : "What is the capital of Germany?",
        "option1" : "Berlin",
        "option2" : "Hamburg",
        "option3" : "Frankfurt",
        "option4" : "Munich",
        "answer"  : "1"
        },
        {
        "question" : "What is the capital of Australia?",
        "option1" : "Canberra",
        "option2" : "Sydney",
        "option3" : "Adelaide",
        "option4" : "Melbourne",
        "answer"  : "1"
        },
        {
        "question" : "What is the capital of France?",
        "option1" : "Paris",
        "option2" : "Lyon",
        "option3" : "Marseille",
        "option4" : "Nice",
        "answer"  : "1"
        },
        {
        "question" : "What is the capital of England?",
        "option1" : "Birmingham",
        "option2" : "Cardiff",
        "option3" : "Manchester",
        "option4" : "London",
        "answer"  : "4"
        },
        {
        "question" : "What is the capital of Japan?",
        "option1" : "Tokyo",
        "option2" : "Kyoto",
        "option3" : "Hiroshima",
        "option4" : "Osaka",
        "answer"  : "1"
        },
        {
        "question" : "What is the capital of Italy?",
        "option1" : "Venice",
        "option2" : "Rome",
        "option3" : "Milan",
        "option4" : "Florence",
        "answer"  : "2"
        },
        {
        "question" : "What is the capital of Brazil?",
        "option1" : "Rio de Janeiro",
        "option2" : "Sao Paulo",
        "option3" : "Brasilia",
        "option4" : "Salvador",
        "answer"  : "3"
        }
    ]
}

#Write to a JSON File

with open('questions.json', 'w') as q:
    json.dump(questions, q)

#Read from a JSON File

with open('questions.json', 'r') as q:
    questions = json.load(q)

#Generate a quiz

correct_answers = 0

for q in questions['questions']:
    print(q['question'])
    print("1. "+q['option1'])
    print("2. "+q['option2'])
    print("3. "+q['option3'])
    print("4. "+q['option4'])
    answer = input("Your Answer: ")
    if answer == q['answer']:
        correct_answers += 1

print("You got "+str(correct_answers)+" questions correct out of "+str(len(questions['questions']))+" questions")