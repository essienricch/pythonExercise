import random

count = 0
# random.seed(104)

number = random.randint(1, 10)
guess = int(input("Guess a number between '1 and 10' : "))

if guess == number:
    print("You guessed right")

elif guess != number:

    print("Wrong Guess, your 2 trails starts now...")

    while count < 2:

        guess = int(input("So, Guess a number between '1 and 10' : "))
        if guess == number:
            print('You guessed right')
            break
        else:
            print("you can do better, keep trying")

        count += 1

print("But you couldn't figure it out, Inconsistent MF")

