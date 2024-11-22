# instructions
print("\nWelcome to 'Guess the Number'!")
print("Guess the random number between 1 and 100.")
print("Do this by entering a number.")
print("You will be told whether this number is greater than or less than the random number.")
print("By narrowing the possible numbers, you will find the correct number.\n")

# Pre-defined variables
high_score = None
play_again = "Y"

# Main while loop
while True:

    # Exit if the play_again input is "n"
    if play_again.lower() == "n":
        break
    
    # Set range for 1-100
    random_number_lower = 1
    random_number_higher = 100

    # Set guess to zero
    guesses = 0

    # Input loop
    while True:
        # Handle invalid input errors
        try:
            # Input and input to integer
            user_input = input("Number: ")
            user_input = int(user_input)

            # Adds 1 to the score each time an input() is used
            guesses += 1

            # Finds the differences of the lower and higher range number and the user_number
            dif_high_and_N = random_number_higher - user_input
            dif_lower_and_N = user_input - random_number_lower
            
            # When only one possible number is left
            if random_number_higher == random_number_lower:

                # End game if player guess the one number left
                if user_input == random_number_higher:
                    print(f"Congratulations! You found the number! The random number was {user_input}.\n")
                    print(f"You found the number in {guesses} guesses.")
                
                    # Update high score if this is the best round
                    if high_score is None or guesses < high_score:
                        high_score = guesses
                        print(f"New high score: {high_score} guesses!\n")

                    # Prints high score if the score for current round is greater than the high score
                    else:
                        print(f"High score: {high_score} guesses.\n")

                    # Asks whether player wants to play again
                    play_again = input("Do you want to play again? [Y/N]: ")
                    print()
                    break

                # When one number is left but the user_input is too low
                elif user_input > random_number_higher:
                    print(f"Number is less than {user_input}.\n")

                # When one number is left but the user_input is too high
                else:
                    print(f"Number is greater than {user_input}.\n")

            # Sets lower range to user_input + 1 when the higher differences is greater than the lower difference
            elif dif_high_and_N >= dif_lower_and_N:
                if user_input >= random_number_lower:
                    random_number_lower = user_input + 1
                print(f"Number is greater than {user_input}.\n")

            # Sets higher range to user_input - 1 when the lower differences is greater than the higher difference
            elif dif_lower_and_N > dif_high_and_N:
                if user_input <= random_number_higher:
                    random_number_higher = user_input - 1
                print(f"Number is less than {user_input}.\n")
            
        # When invalid input
        except ValueError:
            print("Invalid input. Please enter a valid number.")