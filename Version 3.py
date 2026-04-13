'''This program quizzes the user on a variety of different subject-based questions
and returns the name of a teacher in the subject they need the most help in'''
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tutor quiz")
root.geometry("400x300")

# Empty dictionary to store tutors (subject → teacher)
tutors = {}

# Open and read tutor file
with open("tutor_list.txt","r")as file: 
    for line in file:
        line = line.strip()  # remove spaces and new lines
        if line != "":
            subject, tutor = line.split(":")  # split into subject and tutor
            tutors[subject] = tutor   # store in dictionary

# Function to check answers
def check_answers():

    results = []  # stores correct/incorrect messages
    incorrect_subject = []  # stores subjects user got wrong

    # Check question 1
    if q1_entry.get() == "30":
        results.append("Q1 Correct!")
    else:
        results.append("Q1 Incorrect.")
        incorrect_subject.append("math")

    # Check question 2
    if q2_entry.get().lower() == "water":
        results.append("Q2 Correct!")
    else:
        results.append("Q2 Incorrect.")
        incorrect_subject.append("chemistry")

    # Check question 3
    if q3_entry.get().lower() == "paris":
        results.append("Q3 Correct!")
    else:
        results.append("Q3 Incorrect.")
        incorrect_subject.append("geography")

    # If no wrong answers
    if len(incorrect_subject) == 0:
        results.append("No tutoring needed!")
    else:
        results.append("\nTutoring needed:\n")
        
        # Find tutor for each wrong subject
        for subject in incorrect_subject:
            tutor = tutors[subject]
            results.append(f"{subject}: {tutor}\n")
            
    # Combine all results into one string
    final_text = ""       
    for result in results:
        final_text += result + "\n"

    # Show result on screen
    result_text.set(final_text)
        
    # Go to result screen
    show_frame(result_frame)
        
# Function to switch screens
def show_frame(frame):
    frame.tkraise()

# Create frames (different screens)
quiz_frame = tk.Frame(root)
welcome_frame = tk.Frame(root)
result_frame = tk.Frame(root)
list_frame = tk.Frame(root)

# Place frames on top of each other
welcome_frame.grid(row=0, column=0, sticky="nsew")
quiz_frame.grid(row=0, column=0, sticky="nsew") 
result_frame.grid(row=0, column=0, sticky="nsew")
list_frame.grid(row=0, column=0, sticky="nsew")

# Welcome screen title
title = tk.Label(welcome_frame, text="Welcome to the Tutor Quiz!", font=("Arial", 16)) 
title.grid(row=0, column=0, pady=20)

# Button to go to quiz
quiz_button = tk.Button( 
    welcome_frame, 
    text="Start Quiz", 
    command=lambda: show_frame(quiz_frame) 
)
quiz_button.grid(row=1, column=0, pady=20)

# Button to show tutor list
list_button = tk.Button( 
    welcome_frame, 
    text="Show list", 
    command=lambda: show_frame(list_frame) 
) 
list_button.grid(row=2, column=0, pady=20)

# Question 1 label
q1 = tk.Label(quiz_frame, text="1. What is 5 x 6?") 
q1.grid(row=0, column=0, sticky="w", padx=20, pady=20) 

# Input for question 1
q1_entry = tk.Entry(quiz_frame) 
q1_entry.grid(row=0, column=1) 

# Question 2 label
q2 = tk.Label(quiz_frame, text="2. What is H2O?") 
q2.grid(row=1, column=0, sticky="w", padx=20,pady=20) 

# Input for question 2
q2_entry = tk.Entry(quiz_frame) 
q2_entry.grid(row=1, column=1) 

# Question 3 label
q3 = tk.Label(quiz_frame, text="3. What is the capital of France?") 
q3.grid(row=2, column=0, sticky="w", padx=20,pady=20) 

# Input for question 3
q3_entry = tk.Entry(quiz_frame) 
q3_entry.grid(row=2, column=1)

# Submit button to check answers
submit_button = tk.Button(quiz_frame,text="Submit", command=check_answers) 
submit_button.grid(row=3, column=0, columnspan=2, pady=20) 

# Label for tutor list title
list_label = tk.Label(list_frame, text ="Tutor list:",font=("Arial", 12)) 
list_label.grid(row=0, column=0, pady=20)

# Display tutor names
tutor_list = tk.Label(list_frame, text="\nMr Smith - Math\nMs Lee - Chemistry\nMr Patel - Geography",font=("Arial", 12)) 
tutor_list.grid(row=1, column=0, pady=20, padx = 120)

# Button to go back to main menu
main_button = tk.Button(
    list_frame,
    text="Main Menu",
    command=lambda: show_frame(welcome_frame)
)
main_button.grid(row=2, column=0, pady=20, padx = 120)

# Variable to store result text
result_text = tk.StringVar()

# Label to display results
result_label = tk.Label(result_frame, textvariable=result_text)
result_label.grid(row=0, column=1, pady=20, padx = 120)

# Button to go back to main menu
main_button = tk.Button(
    result_frame,
    text="Main Menu",
    command=lambda: show_frame(welcome_frame)
)
main_button.grid(row=1, column=1, pady=20, padx = 120)

# Show welcome screen first
show_frame(welcome_frame) 

# Run the program
root.mainloop()
