#region Setup
import tkinter as tk
import random
from flashcards_tk_storage import flashcards

root = tk.Tk()
root.title("Flashcards")
root.geometry("515x200")

from pathlib import Path
script_directory = Path(__file__).parent
storage_file = script_directory / 'flashcards_tkinter_storage.py'

confirmation = None
flashcardwidget = None
forgotten_flashcards = {}
flashcard_changes = {}
flashcard_deletes = {}
flashcard_setnumber = 0


#endregion

#region 1st Tab
def add_flashcards_tab():
    global quiz_widget, plus_widget, A, B
    for widget in root.winfo_children():
        widget.destroy()
    quiz_widget = tk.Button(root, text="Quiz", width=30, command=quiztab)
    quiz_widget.grid(row=0, column=0, columnspan=2, padx=5, pady=1)
    plus_widget = tk.Button(root, text="+", width=30, command=add_flashcard)
    plus_widget.grid(row=1, column=0, columnspan=2, padx=5, pady=1)

    A = tk.Label(root, text="A")
    A.grid(row=2, column=0, padx=5, pady=1)
    B = tk.Label(root, text="B")
    B.grid(row=2, column=1, padx=5, pady=1)

    A_entry = tk.Entry(root, width=30)
    A_entry.grid(row=3, column=0, padx=5, pady=1)
    B_entry = tk.Entry(root, width=30)
    B_entry.grid(row=3, column=1, padx=5, pady=1)

def add_flashcard():
    global A_entry, B_entry, confirmation
    A_text = A_entry.get().strip().lower()
    B_text = B_entry.get().strip().lower()
    if confirmation is not None and confirmation.winfo_exists():
        confirmation.destroy()
    elif A_text in flashcards or B_text in flashcards.values():
        confirmation = tk.Label(root, text=f"{A_text.title()} or {B_text.title()} is already a flashcard.")
    elif not A_text or not B_text:
        confirmation = tk.Label(root, text= "The A or B word, or both is empty.")
    else:
        flashcards[A_text] = B_text
        confirmation = tk.Label(root, text= f"{A_text.title()} added as {B_text.title()}.")
    A_entry.delete(0, tk.END)
    B_entry.delete(0, tk.END)
    confirmation.grid(row=4, column=0, columnspan=2, padx=5, pady=1)

#endregion

def quiztab():
    global randomized_flashcards
    for widget in root.winfo_children():
        widget.destroy()
    add = tk.Button(root, text="Add", command=add_flashcards_tab)
    add.grid(row=0, column=0, padx=5, pady=1)
    edit = tk.Button(root, text="Edit", command=None) #FIX
    edit.grid(row=0, column=1, padx=5, pady=1)
    remove = tk.Button(root, text="Remove", command=None) #FIX
    remove.grid(row=0, column=2 ,padx=5, pady=1)

    items = list(flashcards.items())
    random.shuffle(items)
    randomized_flashcards = dict(items)
    get_A()
    

def get_A(event=None):
    global A_flashcard, flashcardwidget, B_flashcard
    if flashcardwidget:
        flashcardwidget.destroy()
    current_flashcard_set = list(randomized_flashcards.items())[flashcard_setnumber]
    A_flashcard, B_flashcard = current_flashcard_set
    flashcardwidget = tk.Label(root, text = A_flashcard.title())
    flashcardwidget.grid(row=1, column=0, columnspan = 3, padx=5, pady=1)
    root.unbind("<Return>")
    root.bind("<Return>", get_B)

def get_B(event=None):
    global flashcard_setnumber, B_flashcard, flashcardwidget
    flashcardwidget.destroy()
    flashcardwidget = tk.Label(root, text = B_flashcard.title())
    flashcardwidget.grid(row=1, column=0, columnspan = 3, padx=5, pady=1)
    flashcard_setnumber += 1
    root.unbind("<Return>")
    if fcsetnumber == len(randomized_flashcards):
        root.bind("<Return>", quiz_finished)
    else:
        root.bind("<Return>", get_A)

def quiz_finished(event=None):
    global flashcardwidget, flashcard_setnumber
    flashcardwidget.destroy
    flashcardwidget = tk.Label(root, text = "QUIZ COMPLETE")
    flashcardwidget.grid(row=1, column=0, columnspan = 3, padx=5, pady=1)
    flashcard_setnumber = 0
    root.unbind("<Return>")

add_flashcards_tab()
root.mainloop()

#save

#delete

#edit

#mark as unknown

# Cycle through unknown flashcards
# make storage file
