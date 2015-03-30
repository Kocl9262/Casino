from random import randint
secret = randint(1, 10)
print("Welcome!")
guess = 0
while guess != secret:
    guess = int(raw_input("Guess the number: "))
    if guess == secret:
        print("You win!")
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
print("Game over!")
