"""
Program: Software Development Final 
Author: Landon Ernst
Date: May 12, 2024
"""

#Imports tkinter as tk.
import tkinter as tk
#Imports my other file.
import ErnstLandonFinalpt2

#Sets up and runs the game using both files.
def main():
    root = tk.Tk()
    app = ErnstLandonFinalpt2.StarWarsTriviaGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
