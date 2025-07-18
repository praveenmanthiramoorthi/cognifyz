import random

n = random.randint(1, 100)
while True:
    guess = int(input())
    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high")
    else:
        print("Correct")
        break
