import tkinter as tk
import random
import json
from pathlib import Path

# Setup
root = tk.Tk()
root.title("Flashcards")
root.geometry("515x200")

# Define path for storing flashcards as a JSON file
script_directory = Path(__file__).parent
storage_file = script_directory / 'flashcards_tkinter_storage.json'

# Load existing flashcards from the storage file (if any)
def load_flashcards():
    global flashcards
    if storage_file.exists():
        with open(storage_file, 'r') as f:
            flashcards = json.load(f)
    else:
        flashcards = {}

load_flashcards()

# Set pre-defined variables
confirmation = None
flashcardwidget = None
randomized_flashcards = []

#region 1st Tab (Adding Flashcards)
def add_flashcards_tab():
    global quiz_widget, plus_widget, A, B, A_entry, B_entry
    for widget in root.winfo_children():
        widget.destroy()
    quiz_widget = tk.Button(root, text="Quiz", width=30, command=quiztab)
    quiz_widget.grid(row=0, column=0, columnspan=2, padx=5, pady=1)
    plus_widget = tk.Button(root, text="+", width=30, command=add_flashcard)
    plus_widget.grid(row=1, column=0, columnspan=2, padx=5, pady=1)

    A = tk.Label(root, text="Term (A)")
    A.grid(row=2, column=0, padx=5, pady=1)
    B = tk.Label(root, text="Definition (B)")
    B.grid(row=2, column=1, padx=5, pady=1)

    A_entry = tk.Entry(root, width=30)
    A_entry.grid(row=3, column=0, padx=5, pady=1)
    B_entry = tk.Entry(root, width=30)
    B_entry.grid(row=3, column=1, padx=5, pady=1)

def add_flashcard():
    global A_entry, B_entry, confirmation
    A_text = A_entry.get().strip().lower()
    B_text = B_entry.get().strip().lower()
    
    # Clear previous confirmation message if any
    if confirmation is not None and confirmation.winfo_exists():
        confirmation.destroy()

    # Check if the term already exists or if the fields are empty
    if A_text in flashcards or B_text in flashcards.values():
        confirmation = tk.Label(root, text=f"'{A_text.title()}' or '{B_text.title()}' is already a flashcard.")
    elif not A_text or not B_text:
        confirmation = tk.Label(root, text="The Term (A) or Definition (B) is empty.")
    else:
        flashcards[A_text] = B_text
        # Save the flashcards to the JSON file
        with open(storage_file, 'w') as f:
            json.dump(flashcards, f, indent=4)
        confirmation = tk.Label(root, text=f"'{A_text.title()}' added as '{B_text.title()}'.")
    
    # Clear the input fields
    A_entry.delete(0, tk.END)
    B_entry.delete(0, tk.END)
    confirmation.grid(row=4, column=0, columnspan=2, padx=5, pady=1)

#endregion

#region Quiz Tab
def quiztab():
    global randomized_flashcards, flashcard_setnumber
    # Shuffle flashcards
    items = list(flashcards.items())
    random.shuffle(items)
    randomized_flashcards = dict(items)

    # Sets the button for going back to the add_flashcards_tab
    flashcard_setnumber = 0
    for widget in root.winfo_children():
        widget.destroy()
    add = tk.Button(root, text="Add", command=add_flashcards_tab)
    add.grid(row=0, column=0, padx=5, pady=1)
    
    get_A()

# Displays the A or term of the current flashcard
def get_A(event=None):
    global A_flashcard, flashcardwidget, B_flashcard
    if flashcardwidget:
        flashcardwidget.destroy()
    
    # Get the index for the current flashcard
    current_flashcard_set = list(randomized_flashcards.items())[flashcard_setnumber]
    A_flashcard, B_flashcard = current_flashcard_set
    
    flashcardwidget = tk.Label(root, text=A_flashcard.title())
    flashcardwidget.grid(row=1, column=0, columnspan=3, padx=5, pady=1)
    root.unbind("<Return>")
    root.bind("<Return>", get_B)

# Displays the B or definition of the current flashcard
# FIX - Inconsistency using both the terminal and Tkinter window
def get_B(event=None):
    global flashcard_setnumber, B_flashcard, flashcardwidget
    user_answer = input("What is the definition of " + A_flashcard + "?: ")
    flashcardwidget.destroy()
    if user_answer.strip().lower() == B_flashcard:
        flashcardwidget = tk.Label(root, text="Correct!")
    else:
        flashcardwidget = tk.Label(root, text=f"Incorrect. The correct answer is {B_flashcard}.")
    flashcardwidget.grid(row=1, column=0, columnspan=3, padx=5, pady=1)

    flashcard_setnumber += 1
    root.unbind("<Return>")
    if flashcard_setnumber == len(randomized_flashcards):
        root.bind("<Return>", quiz_finished)
    else:
        root.bind("<Return>", get_A)
        
# FIX Needs a def for editing a flashcard - this could also be added to the add_flashcard_tab
# FIX Needs a def for deleting a file - this could also be added to the add_flashcard_tab

def quiz_finished(event=None):
    global flashcardwidget, flashcard_setnumber
    flashcardwidget.destroy()
    flashcardwidget = tk.Label(root, text="QUIZ COMPLETE")
    flashcardwidget.grid(row=1, column=0, columnspan=3, padx=5, pady=1)
    root.unbind("<Return>")

#endregion

add_flashcards_tab()
root.mainloop()
