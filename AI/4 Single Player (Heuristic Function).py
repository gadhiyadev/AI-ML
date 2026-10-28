import random

def heuristic_feedback(guess, target):
    diff = abs(guess - target)
    if guess < target:
        return f"Too low! (Distance from target: {diff})"
    elif guess > target:
        return f"Too high! (Distance from target: {diff})"
    else:
        return "Correct!"

def game():
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    feedback = ""

    print("--- Number Guessing Game (Heuristic Search) ---")
    print(f"Guess the number between 1 and 100. Total attempts: {max_attempts}\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            feedback = heuristic_feedback(guess, target_number)
            print(feedback)

            if feedback == "Correct!":
                print(f"\nSuccess! You guessed the number in {attempts} attempts.\n")
                break
        except ValueError:
            print("Please enter a valid integer.")

    if feedback != "Correct!":
        print(f"\nGame over! The correct number was {target_number}.")

if __name__ == "__main__":
    game()
