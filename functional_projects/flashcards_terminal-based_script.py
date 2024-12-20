'''
A terminal-based simple flashcard app. 
Functions include adding and removing flashcards, 
displaying and quizing flashcards, and checking whether a flashcard exists. 
Type 'help' for a list of commands. 
Type '-' after the definition of a flashcard, if not known, 
and that card will circle through the quiz again. 
Flashcards are saved to a JSON file.
'''

# Imports and pre-defined variables
import random
import json
from pathlib import Path
forgotten = {}

# Define path for storing flashcards as a JSON file
script_directory = Path(__file__).parent
storage_file = script_directory / 'flashcards_terminal-based_storage.json'

# Load existing flashcards from the storage file (if any)
def load_flashcards():
    global flashcards
    if storage_file.exists():
        with open(storage_file, 'r') as f:
            flashcards = json.load(f)
    else:
        flashcards = {}

# Add flashcard to flashcards if not already in flashcards
def add_flashcard():
    A = input("   A: ")
    A = A.lower()
    if A in flashcards:
        print(f"   {A.title()} is already a flashcard.")
    else:
        B = input("   B: ")
        B = B.lower()
        flashcards[A] = B
        save()

# Remove flashcard from flashcard if in flashcards
def remove_flashcard():
    deleted_flashcard = input("   Removed flashcard (A): ")
    deleted_flashcard = deleted_flashcard.lower()
    if deleted_flashcard in flashcards:
        del flashcards[deleted_flashcard]
        save()
    else:
        print("Flashcard not in list.")

# Display all flashcards in order they were created
def display():
    for A, B in flashcards.items():
        print(f"{A.title()} - {B.title()}")

# If the user input ends with '?', 
# then displays definition if the word is in flashcards.
def is_it():
    word = user_input[: -1]
    word = word.lower()
    if word in flashcards:
        print(f"  {flashcards[word].title()}")
    else:
        print(f"{word.title()} is not a flashcard.")

# Quiz the user. If a word is not known, user inputs'-'. 
# This copies that flashcard to forgotten to be repeated again in the quiz.
def quiz():
    items = list(flashcards.items())
    random.shuffle(items)
    randomized_flashcards = dict(items)
    for A, B in randomized_flashcards.items():
        print("")
        input(A.title())
        dont_know = input(f"{B.title()} ")
        if dont_know == "-":
            forgotten[A] = B
    while forgotten:
        for A, B in list(forgotten.items()):
            print("")
            input(A)
            dont_know = input(B)
            if dont_know != "-":
                del forgotten[A]
    print("\nQuiz completed.")

# Displays a list of commands
def help():
    print("\nTo add flashcard, enter '+.'")
    print("To remove flashcard, enter '-.'")
    print("To display flashcards, enter 'd.'")
    print("To see if a word is already a flashcard, enter the name of the word plus '?.'")
    print("To quiz yourself, enter 'q.'")
    print("To mark flashcard as forgotten, enter '-' after definition.")
    print("To exit, enter 'exit.'")

# save flashcards to JSON
def save():
    with open(storage_file, "w") as file:
        json.dump(flashcards, file, indent=4)

# Import flashcards from JSON and display commands from help
load_flashcards()
help()

# Main while loop    
while True:
    user_input = input("\n: ")
    if user_input == "exit":
        save()
        break
    
    elif user_input == "+":
        add_flashcard()

    elif user_input == "-":
        remove_flashcard()

    elif user_input == "d":
        display()

    elif user_input == "q":
        quiz()

    elif user_input == "help":
        help()

    elif user_input.endswith("?"):
        is_it()

    else:
        print("\nUnrecognized command.")
        help()