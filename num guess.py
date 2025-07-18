import random

low = int(input())
high = int(input())
n = random.randint(low, high)

while True:
    guess = int(input())
    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high")
    else:
        print("Correct")
        break
