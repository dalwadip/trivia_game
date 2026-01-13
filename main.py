import json
import random

#use json
#want to make the options randomly shuffled
with open("trivia.json") as f: #to use it, first open file
    trivia_data = json.load(f) #easily read in the contents of that file as python dictionaries
# print(trivia_data) #print things out before and after when confused
random.shuffle(trivia_data) #randomly shuffles the items in that list
# print(trivia_data)

score = 0
question_number = 1
letters = ['A', 'B', 'C'] #puts the letters in uppercase, so must put the user_choice as upper

print("Welcome to trivia!\n")

for question in trivia_data: #loop via each question, and present the question and the options, 'question' takes one whole block from json (question, options, answer)
    print(f"Question {question_number}:  {question['question']}") # outputs: Question 1. What is grass?
    options = question['options'] #extracting the list
    random.shuffle(options) #put it where the option is declared

    for i in range(len(options)): #need options, so have to put it inside the for loop above or could put it outside
        # print(i) # prints out the index short for i
        print(f"  {letters[i]}. {options[i]}") #outputs: A. ice

    choice = input("Your choice (A/B/C): ").upper().strip()

    # print(choice, letters) #checks if choice and letters match
    if choice in letters: #checks if choice is in letters, if not then not valid choice
        index = letters.index(choice) #.index(): gets the index of this value
        # print(index) #prints index of the choice and gets index from letters
        selected = options[index]
        # print(selected) #gets the option the user selected

        if selected == question['answer']: #if selected answer equals correct answer, question['answer']: looks at one block in json then say answer because you want that
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {question['answer']}")
    else:
        print("Invalid choice. Skipping question.")

    question_number += 1

print(f"Quiz complete! You scored {score} / {len(trivia_data)}!")
