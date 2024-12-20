'''
User tries to guess a number from 1-100. 
User is told whether their picked number is higher or lower 
than the randomly generated number. 
This process is repeated until the user narrows down the possible number 
and types the randomly selected number.
'''

# Imports and pre-defined variables
import random
high_score = None # High score is only saved in game. Restarting the program will reset the high score
play_again = None

# Instructions printed at the beginning of the game
print("\nWelcome to 'Guess the Number'!")
print("Guess the random number between 1 and 100.")
print("Do this by entering a number.")
print("You will be told whether this number is greater than or less than the random number.")
print("By narrowing the possible numbers, you will find the correct number.\n")

# Main while loop
while True:

    # If user input is 'n' break the loop and end the game
    if play_again.lower() == "n":
        break

    # Creates random number every round
    random_number = random.randint(1, 100)

    # Sets guesses to 0 every round
    guesses = 0

    # Input loop for a round
    while True:
        # Handle invalid input errors
        try:
            # Gets the integer of the user input
            user_input = int(input("Number: "))

            # Increments guesses by one
            guesses += 1

            # If random number is greater than user input, print so
            if random_number > user_input:
                print(f"Number is greater than {user_input}.\n")

            # If random number is less than user input, print so
            elif random_number < user_input:
                print(f"Number is less than {user_input}.\n")
            
            # Otherwise, user input must equal the random number. 
            # Print so, display answer and number of guesses
            else:
                print(f"Congratulations! You found the number! The random number was {random_number}.\n")
                print(f"You found the number in {guesses} guesses.")
                
                # Update high score if the round high score for this round was the lowest, print so
                if high_score is None or guesses < high_score:
                    high_score = guesses
                    print(f"New high score: {high_score} guesses!\n")

                # If current round score is greater than high score, print high score
                else:
                    print(f"High score: {high_score} guesses.\n")

                # Ask user whether they want to play again
                play_again = input("Do you want to play again? [Y/N]: ")
                print()
                break

        # When invalid input, tell user to enter a valid input
        except ValueError:
            print("Please enter a number.")
