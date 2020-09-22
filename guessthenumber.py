import random
import sys
import time

theNumber = random.randint(1, 20)
print("Hello, what is your name?")
name = input()

print(f"Hi {name}, I am thinking of a number between 1 and 20")

time.sleep(1.5)

for i in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess > theNumber:
        print("Guess is too high.")
    elif guess < theNumber:
        print("Guess is too low.")
    elif guess == theNumber:
        break
    else:
        print("Error?!")

if guess == theNumber:
    print("Correct, Nice Job")
else:
    print("Nope, The number I was thinking of was " + str(theNumber))
