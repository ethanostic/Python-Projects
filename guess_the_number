# instructions
print("\nWelcome to 'Guess the Number'!")
print("Guess the random number between 1 and 100.")
print("Do this by entering a number.")
print("You will be told whether this number is greater than or less than the random number.")
print("By narrowing the possible numbers, you will find the correct number.\n")

# Imports and pre-defined variables
import random
high_score = None
play_again = "Y"

# Main while loop
while True:

    if play_again.lower() == "n":
        break

    # Creates random number
    random_number = random.randint(1, 100)

    # initializes guesses
    guesses = 0

    # Input loop
    while True:
        # handles errors
        try:
            user_input = input("Number: ")
            user_input = int(user_input)
            guesses += 1

            if random_number > user_input:
                print(f"Number is greater than {user_input}.\n")
            elif random_number < user_input:
                print(f"Number is less than {user_input}.\n")
            else:
                print(f"Congratulations! You found the number! The random number was {random_number}.\n")
                print(f"You found the number in {guesses} guesses.")
                
                # Update high score if this is the best round
                if high_score is None or guesses < high_score:
                    high_score = guesses
                    print(f"New high score: {high_score} guesses!\n")

                # prints high score if the score for current round is greater than the high score
                else:
                    print(f"High score: {high_score} guesses.\n")

                play_again = input("Do you want to play again? [Y/N]: ")
                print()
                break

        # when invalid input
        except ValueError:
            print("Please enter a valid number.")
