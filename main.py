import json
import random

#use json
with open("trivia.json") as f: #to use it, first open file
    trivia_data = json.load(f) #easily read in the contents of that file as python dictionaries

random.shuffle(trivia_data) #randomly shuffles the items in that list
score = 0
question_number = 1
letters = ['A', 'B', 'C']

print("Welcome to trivia!\n")

for question in trivia_data: #loop via each question, and present the question and the options
    print(f"Question {question_number}:  {question['question']}") # outputs: Question 1. What is grass?
    options = question['options'] #extracting the list

    for i in range(len(options)):
        print(f"{letters[i]}. {options[i]}") #outputs: A. ice

    choice = input("Your choice (A/B/C): ").lower().strip()

    if choice in letters: #checks if choice is in letters, if not then not valid choice
        index = letters.index(choice) #.index(): gets the index of this value
        selected = options[index]

        if selected == question['answer']: #if selected answer equals correct answer
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {question['answer']}")
    else:
        print("Invalid choice. Skipping question.")

    question_number += 1

print(f"Quiz complete! You scored {score} / {len(trivia_data)}")
