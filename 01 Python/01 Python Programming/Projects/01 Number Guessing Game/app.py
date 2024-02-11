import random

maxAttempts = 3
attempts = 0

# Generate random number between 1 to 20
rNumber = random.randint(1, 20)

while attempts < 3:
    print(f"\nYou have {maxAttempts} chances left")
    guessNum = int(input("Guess a number between 1 to 20 : "))
    
    if rNumber == guessNum:
        print("You Won!")
        break
    elif rNumber < guessNum:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

    attempts += 1
    maxAttempts -= 1

if attempts == 3:
    print(f"Sorry, you are out of attempts. The correct number was {rNumber}")
