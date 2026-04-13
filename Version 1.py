'''This program quizzes the user on a variety of different subject-based questions
and returns the name of a teacher in the subject they need the most help in'''
import sys

#This list defines the available tutors
tutors = {
    "math": "Mr Smith",
    "chemistry": "Ms Lee",
    "geography": "Mr Patel"
}
#This list contains all the questions, answers and assigned subjects
questions = [
    {
        "question": "What is 5 x 6?",
        "answer": "30",
        "subject": "math"
    },
    {
        "question": "What is H2O?",
        "answer": "water",
        "subject": "chemistry"
    },
    {
        "question": "What is the capital of France?",
        "answer": "paris",
        "subject": "geography"
    }
]

#This is an empty list which the program will later use to store the incorrect subjects
incorrect_subject = []

#Tutor quiz function
def quiz():
    score = 0
    
    for i in questions:
        print(i["question"])
        user_ans = input("Enter answer : ").lower()
        
        correct_answer = i["answer"]
        if user_ans == correct_answer:
            print("Correct!")
            score+=1
        else:
            print("Incorrect")
            weak_subject = i["subject"]
            incorrect_subject.append(weak_subject)
            
    quiz_results()
    
#Quiz results function
def quiz_results():
    if len(incorrect_subject) == 0:
        print("\nWell done, you got all questions correct!\nNo tutoring needed.")
        sys.exit()
    else:
        print("\nRecommended tutor list:")
        for subject in incorrect_subject:
            tutor = tutors[subject]
            print(f"Tutor name : {tutor}")

#Main menu function
def main_menu():
    print("\n\n---------Welcome to the quiz---------")
    print("Options:\n")
    print("1. List of tutors\n2. Proceed to quiz\n3. Exit quiz\n")
    choice = input("Enter choice : ")
    if choice == "1":
        print(tutors)
        main_menu()
        
    if choice == "2":
        quiz()
        main_menu()
        
    if choice == "3":
        print("Thank you for playing!")
        sys.exit()

    else:
        print("\nEnter valid choice.")
        main_menu()

main_menu()




