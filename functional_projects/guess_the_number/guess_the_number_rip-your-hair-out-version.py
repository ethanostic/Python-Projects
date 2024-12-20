'''
User tries to guess a number from 1-100. 
User is told whether their picked number is higher or lower 
than the randomly generated number. 
This process is repeated until the user narrows down the possible number 
and types the randomly selected number.

NOTE The 'randomly generated number' does not exist. 
The program is designed to make the user's last guess possible 
be the random number.
'''

# Pre-defined variables
high_score = None # High score is only saved in game. Restarting the program will reset the high score
play_again = None

# Instructions
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
    
    # Set range of possible number left: 1-100
    random_number_lower = 1
    random_number_higher = 100

    # Sets guesses to 0 every round
    guesses = 0

    # Input loop
    while True:
        # Handle invalid input errors
        try:
            # Input and input to integer
            user_input = input("Number: ")
            user_input = int(user_input)

            # Increments guesses by one
            guesses += 1

            # Finds the differences of the lower and higher range number and the user_number
            dif_high_and_N = random_number_higher - user_input
            dif_lower_and_N = user_input - random_number_lower
            
            # When only one possible number is left
            if random_number_higher == random_number_lower:

                # End game if player guess the one number left
                if user_input == random_number_higher:
                    print(f"Congratulations! You found the number! 
                          The random number was {user_input}.\n")
                    print(f"You found the number in {guesses} guesses.")
                
                    # Update high score if current round score is lower than previous high score, print so
                    if high_score is None or guesses < high_score:
                        high_score = guesses
                        print(f"New high score: {high_score} guesses!\n")

                    # Prints previous high score, 
                    # if current round score is greater than the high score
                    else:
                        print(f"High score: {high_score} guesses.\n")

                    # Asks whether player wants to play again
                    play_again = input("Do you want to play again? [Y/N]: ")
                    print()
                    break

                # When one number is left but the user_input is too low, print so
                elif user_input > random_number_higher:
                    print(f"Number is less than {user_input}.\n")

                # When one number is left but the user_input is too high, print so
                else:
                    print(f"Number is greater than {user_input}.\n")

            # When there is more than one possible answer left
            # Sets lower range to user_input + 1 
            # when the higher differences is greater than the lower difference. 
            # Print that 'random' number is greater than user input
            elif dif_high_and_N >= dif_lower_and_N:
                if user_input >= random_number_lower:
                    random_number_lower = user_input + 1
                print(f"Number is greater than {user_input}.\n")

            # Sets higher range to user_input - 1 
            # when the lower differences is greater than the higher difference. 
            # Print that 'random' number is greater than user input
            elif dif_lower_and_N > dif_high_and_N:
                if user_input <= random_number_higher:
                    random_number_higher = user_input - 1
                print(f"Number is less than {user_input}.\n")
            
        # When invalid input, tell user to enter a valid input
        except ValueError:
            print("Invalid input. Please enter a number.")
