
'''New Concept: Dictionaries

1.Store questions in dictionary

2. Keep score

3.Show final result'''

questions = {
    "What does CPU stand for?": "Central Processing Unit",
    "What does RAM stand for?": "Random Access Memory",
    "What does ROM stand for?": "Read Only Memory",
    "What is the brain of the computer?": "CPU",
    "Which device is used to enter data into a computer?": "Keyboard",
    "Which device shows output on a screen?": "Monitor",
    "Which device is used to print documents?": "Printer",
    "Which device connects a computer to the internet?": "Router",
    "What is the main circuit board of a computer called?": "Motherboard",
    "Which storage device is used to store data permanently?": "Hard Drive"
}

score = 0

for question in questions:

    print(question)
    print("Enter Q to exit!!!")

    user = input("Answer -> ")

    if user == 'Q' or user == 'q':
        break

    if user == questions[question]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("Your final score is:", score)
