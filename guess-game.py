import random # import a random number

play_again = "yes" # Play again is a variable

while play_again.lower() in ["yes", "y"]: # Every line that is indented follows this line


    secret = random.randint(1,100)   # A varaible for secret and generate a random integer between 1 and 100.
    attempts = 0  # Variable for 0
    max_attempts = 7  # Variable for max attempts. When user runs out of guesses.

    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between 1 and 100")
    print(f"You have {max_attempts} attempts")


    while attempts < max_attempts:  # While loop. As long as the attempts are less than max attempts, it is true and continue to run.
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("Please enter valid number.")
            continue

        attempts += 1

        if guess == secret:
            print(f"\nYou got it in {attempts} attempts!")
            break # Once the user guesses the number, the loop will stop.
        elif guess < secret:  # Let's give the user some hints
            print("Too low!")
        else:
            print("Too high!")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"{remaining} attempts remaining")

    else: print(f"\nOut of attempts! The number was {secret}.") # Display to the user they lost and what the correct number was.

    play_again = input("\nplay again? (yes/no): ")  # Use play again variable again, but now with user input.

print("Thanks for playing!")
    