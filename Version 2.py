'''This program quizzes the user on a variety of different subject-based questions
and returns the name of a teacher in the subject they need the most help in'''
import tkinter as tk

root = tk.Tk()
root.title("Tutor quiz")
root.geometry("400x300")

#This list defines the available tutors
tutors = {
    "math": "Mr Smith",
    "chemistry": "Ms Lee",
    "geography": "Mr Patel"
}

incorrect_subject = []

#This function checks the answers
def check_answers():

    results = []

    if q1_entry.get() == "30":
        results.append("Q1 Correct!")
    else:
        results.append("Q1 Incorrect.")
        incorrect_subject.append("math")

    if q2_entry.get().lower() == "water":
        results.append("Q2 Correct!")
    else:
        results.append("Q2 Incorrect.")
        incorrect_subject.append("chemistry")

    if q3_entry.get().lower() == "paris":
        results.append("Q3 Correct!")
    else:
        results.append("Q3 Incorrect.")
        incorrect_subject.append("geography")

    # final message
    if len(incorrect_subject) == 0:
        results.append("No tutoring needed!")
    else:
        results.append("\nTutoring needed:\n")
        for subject in incorrect_subject:
            tutor = tutors[subject]
            results.append(f"{subject}: {tutor}\n")
            
    final_text = ""       
    for result in results:
        final_text += result + "\n"
    result_text.set(final_text)
        
    show_frame(result_frame)
        
def show_frame(frame):
    frame.tkraise()

#Frames
quiz_frame = tk.Frame(root)
welcome_frame = tk.Frame(root)
result_frame = tk.Frame(root)
list_frame = tk.Frame(root)

#
welcome_frame.grid(row=0, column=0, sticky="nsew")
quiz_frame.grid(row=0, column=0, sticky="nsew") 
result_frame.grid(row=0, column=0, sticky="nsew")
list_frame.grid(row=0, column=0, sticky="nsew")

#
title = tk.Label(welcome_frame, text="Welcome to the Tutor Quiz!", font=("Arial", 16)) 
title.grid(row=0, column=0, pady=20)

quiz_button = tk.Button( 
    welcome_frame, 
    text="Start Quiz", 
    command=lambda: show_frame(quiz_frame) 
)
quiz_button.grid(row=1, column=0, pady=20)

list_button = tk.Button( 
    welcome_frame, 
    text="Show list", 
    command=lambda: show_frame(list_frame) 
) 
list_button.grid(row=2, column=0, pady=20)

#quiz frame

q1 = tk.Label(quiz_frame, text="1. What is 5 x 6?") 
q1.grid(row=0, column=0, sticky="w", padx=20, pady=20) 

q1_entry = tk.Entry(quiz_frame) 
q1_entry.grid(row=0, column=1) 

q2 = tk.Label(quiz_frame, text="2. What is H2O?") 
q2.grid(row=1, column=0, sticky="w", padx=20,pady=20) 

q2_entry = tk.Entry(quiz_frame) 
q2_entry.grid(row=1, column=1) 

q3 = tk.Label(quiz_frame, text="3. What is the capital of France?") 
q3.grid(row=2, column=0, sticky="w", padx=20,pady=20) 

q3_entry = tk.Entry(quiz_frame) 
q3_entry.grid(row=2, column=1)

submit_button = tk.Button(quiz_frame,text="Submit", command=check_answers) 
submit_button.grid(row=3, column=0, columnspan=2, pady=20) 

#list frame
list_label = tk.Label(list_frame, text ="Tutor list:",font=("Arial", 12)) 
list_label.grid(row=0, column=0, pady=20)

tutor_list = tk.Label(list_frame, text="\nMr Smith - Math\nMs Lee - Chemistry\nMr Patel - Geography",font=("Arial", 12)) 
tutor_list.grid(row=1, column=0, pady=20, padx = 120)

#result frame
result_text = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=result_text)
result_label.grid(row=0, column=1, pady=20, padx = 120)

#start program
show_frame(welcome_frame) 
root.mainloop()
