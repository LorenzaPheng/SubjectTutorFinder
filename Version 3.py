'''This program quizzes the user on a variety of different subject-based questions
and returns the name of a teacher in the subject they need the most help in'''
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tutor quiz")
root.geometry("400x300")

# Empty dictionaries
tutors = {}
answers = {
    "q1": "",
    "q2": "",
    "q3": ""
}

# Open and read tutor file
with open("tutor_list.txt","r")as file: 
    for line in file:
        line = line.strip()  # remove spaces and new lines
        if line != "":
            subject, tutor = line.split(":")  # split into subject and tutor
            tutors[subject] = tutor   # store in dictionary

# Function to check answers
def check_answers():

    results = []
    incorrect_subject = []
 
    if answers["q1"] == "3.1416":
        results.append("Q1 Correct!")
    else:
        results.append("Q1 Incorrect.")
        incorrect_subject.append("math")

    if answers["q2"] == "Water":
        results.append("Q2 Correct!")
    else:
        results.append("Q2 Incorrect.")
        incorrect_subject.append("chemistry")

    if answers["q3"] == "Paris":
        results.append("Q3 Correct!")
    else:
        results.append("Q3 Incorrect.")
        incorrect_subject.append("geography")

    # If no wrong answers
    if len(incorrect_subject) == 0:
        results.append("No tutoring needed!")
    else:
        results.append("\n\nTutoring needed:\n")
        
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
welcome_frame = tk.Frame(root)
result_frame = tk.Frame(root)
list_frame = tk.Frame(root)
q1_frame = tk.Frame(root)
q2_frame = tk.Frame(root)
q3_frame = tk.Frame(root)

# Place frames on top of each other
welcome_frame.grid(row=0, column=0, sticky="nsew")
result_frame.grid(row=0, column=0, sticky="nsew")
list_frame.grid(row=0, column=0, sticky="nsew")
q1_frame.grid(row=0, column=0, sticky="nsew")
q2_frame.grid(row=0, column=0, sticky="nsew")
q3_frame.grid(row=0, column=0, sticky="nsew")


# Welcome screen title
title = tk.Label(welcome_frame, text="Welcome to the Tutor Quiz!", font=("Arial", 16)) 
title.grid(row=0, column=0, pady=20, padx=60)
intro_message = tk.Label(welcome_frame, text="Take this Year 9 quiz to find a Tutor suitable for you!", font=("Arial", 9)) 
intro_message.grid(row=1, column=0, pady=20, padx=60)

# Button to go to quiz
quiz_button = tk.Button( 
    welcome_frame, 
    text="Start Quiz", 
    command=lambda: show_frame(q1_frame) 
)

# Button to show tutor list
list_button = tk.Button( 
    welcome_frame, 
    text="Show Tutors", 
    command=lambda: show_frame(list_frame) 
)

# Welcome_frame button grid

quiz_button.grid(row=2, column=0, columnspan=2, pady=10)
list_button.grid(row=3, column=0, columnspan=2, pady=10)

# Question 1 label
q1 = tk.Label(q1_frame, text="1. What is pi?", font=("Arial", 15)) 
q1.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)

# choices for question 1
q1_opt1 = tk.Button(q1_frame, text="3.1416",
                    command=lambda: (answers.update({"q1": "3.1416"}), show_frame(q2_frame))) # updating the dictionaries

q1_opt2 = tk.Button(q1_frame, text="A food",
                    command=lambda: (answers.update({"q1": "A food"}), show_frame(q2_frame)))

q1_opt3 = tk.Button(q1_frame, text="4.121",
                    command=lambda: (answers.update({"q1": "4.121"}), show_frame(q2_frame)))

# Q1 options grid
q1_opt1.grid(row=1, column=0, pady=20, padx = 40)
q1_opt2.grid(row=1, column=1, pady=20, padx = 40)
q1_opt3.grid(row=1, column=2, pady=20, padx = 40)

# Question 2 label
q2 = tk.Label(q2_frame, text="2. What is H2O?", font=("Arial", 15)) 
q2.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=20, pady=20) 

# choices for question 2
q2_opt1 = tk.Button(q2_frame, text="Lava",
                    command=lambda: (answers.update({"q2": "Lava"}), show_frame(q3_frame)))

q2_opt2 = tk.Button(q2_frame, text="Liquid",
                    command=lambda: (answers.update({"q2": "Liquid"}), show_frame(q3_frame)))

q2_opt3 = tk.Button(q2_frame, text="Water",
                    command=lambda: (answers.update({"q2": "Water"}), show_frame(q3_frame)))

# Q2 options grid
q2_opt1.grid(row=1, column=0, pady=20, padx = 40)
q2_opt2.grid(row=1, column=1, pady=20, padx = 40)
q2_opt3.grid(row=1, column=2, pady=20, padx = 40)

# Question 3 label
q3 = tk.Label(q3_frame, text="3. What is the capital of France?", font=("Arial", 15)) 
q3.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)

# choices for question 3
q3_opt1 = tk.Button(q3_frame, text="Paris",
                    command=lambda: (answers.update({"q3": "Paris"}), check_answers()))

q3_opt2 = tk.Button(q3_frame, text="London",
                    command=lambda: (answers.update({"q3": "London"}), check_answers()))

q3_opt3 = tk.Button(q3_frame, text="Berlin",
                    command=lambda: (answers.update({"q3": "Berlin"}), check_answers()))
# Q3 options grid
q3_opt1.grid(row=1, column=0, pady=20, padx = 40)
q3_opt2.grid(row=1, column=1, pady=20, padx = 40)
q3_opt3.grid(row=1, column=2, pady=20, padx = 40)


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
main_button.grid(row=1, column=1, pady=0, padx = 20)

# Show welcome screen first
show_frame(welcome_frame) 

# Run the program
root.mainloop()
