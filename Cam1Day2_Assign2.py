import random

Guess = 0

while(1):
    Answer = random.randint(1, 10)
    while(Guess !=  Answer ):
        Guess = int(input("Guess the Number: "))
        if (Guess == Answer):
            break
        print("Wrong Number! Try Again!")
    print("Correct!")
