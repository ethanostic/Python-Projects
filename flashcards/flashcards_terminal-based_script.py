import random

# Get the directory of the current script
from pathlib import Path
script_directory = Path(__file__).parent
storage_file = script_directory / 'flashcards_terminal-based_storage.py'

# FIX must be a json file
from flashcards_terminal-based_storage import flashcards

forgotten = {}

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

def remove_flashcard():
    deleted_flashcard = input("   Removed flashcard (A): ")
    deleted_flashcard = deleted_flashcard.lower()
    if deleted_flashcard in flashcards:
        del flashcards[deleted_flashcard]
        save()
    else:
        print("Flashcard not in list.")

def display():
    for A, B in flashcards.items():
        print(f"{A.title()} - {B.title()}")

def is_it():
    word = user_inputinput[: -1]
    word = word.lower()
    if word in flashcards:
        print(f"  {flashcards[word].title()}")
    else:
        print(f"{word.title()} is not a flashcard.")

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

def help():
    print("\nTo add flashcard, enter '+.'")
    print("To remove flashcard, enter '-.'")
    print("To display flashcards, enter 'd.'")
    print("To see if a word is already a flashcard, enter the name of the word plus '?.'")
    print("To quiz yourself, enter 'q.'")
    print("To exit, enter 'exit.'")

# FIX must be a json file.
def save():
    with open(storage_file, 'w') as file:
        file.write(f"flashcards = {repr(flashcards)}\n")

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
