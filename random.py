import random

def guess_the_number():
    # Pick a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess this branch is FEATURE branch?")
    
    # Loop until the player guesses correctly
    while True:
        try:
            # Get input from the user
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the user's guess against the secret number
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            elif user_guess == secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found the number in {attempts} attempts!")
                break # Exit the loop
            

# Run the game
if __name__ == "__main__":
    guess_the_number()
