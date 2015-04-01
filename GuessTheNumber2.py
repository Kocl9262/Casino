from random import randint
secret = randint(1, 20)

print("Welcome!")

poskus = 1

guess = int(raw_input("Ugani cifro: "))

while guess != secret and poskus < 6:
    if guess > secret:
        print("Cifra previsoka...")
    elif guess < secret:
        print("Cifra prenizka...")
    guess = int(raw_input("Ugani cifro: "))

    poskus += 1


if poskus == 6:
    print("Porabili ste vseh 5 poskusov")
else:
    print("************************************************")
    print("*****          Uganili ste cifro!          *****")
    print("************************************************")

print("Game Over!")
