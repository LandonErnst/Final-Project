"""
Program: Final Project 
Author: Landon Ernst
Date: May 12, 2024
"""

#Imports tkinter as tk
import tkinter as tk
#Imports the messagebox from the tkinter library.
from tkinter import messagebox

#Creates a class for StarWarsTriviaGame
class StarWarsTriviaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Star Wars Trivia Game")
        self.master.geometry("600x300")

        #Sets the value of the questions to 0.
        self.current_question = 0

        #The List that holds the questions for trivia.
        self.questions = [
            "Who is Luke Skywalker's father?",
            "What is the name of Han Solo's ship?",
            "What weapons do Jedi Knights use?",
            "What creatures live in the forests of Endor?",
            "Who built C-3PO?",
            "What is the name of the creature that holds Princess Leia captive in Return of the Jedi?",
            "What is Darth Vader's real name?",
            "Who created Star Wars?"
        ]

        #The list that holds the answers for the trivia.
        self.answers = ["Darth Vader", 
                        "Millennium Falcon", 
                        "Lightsabers", 
                        "Ewoks", 
                        "Anakin Skywalker", 
                        "Jabba the Hutt", 
                        "Anakin Skywalker",
                        "George Lucas"
                        ]

        #Creates a label that shows the question
        self.label = tk.Label(master, text=self.questions[self.current_question])
        self.label.pack()

        #Creates the box to enter answers in.
        self.entry = tk.Entry(master)
        self.entry.pack()

        #Creates the submit button.
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        #Creates the next button.
        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack()

        #Creates the exit button.
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.place(x=0, y=0)

    #Checks the answer that was inputted using the list.
    def check_answer(self):
        answer = self.entry.get()
        correct_answer = self.answers[self.current_question]
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Right!", "You got it right!")
        else:
            messagebox.showerror("Wrong!", "Try again!")

    #Allows the user to continue to the next question until there are no more.
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.label.config(text=self.questions[self.current_question])
        else:
            messagebox.showinfo("The End", "No more Star Wars questions :(")

    #Closes the GUI window
    def exit_app(self):
        self.master.destroy()

#Sets up and runs the game.
def main():
    root = tk.Tk()
    app = StarWarsTriviaGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
