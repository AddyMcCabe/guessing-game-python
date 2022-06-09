import random

name = input("Hello, what's you're name?\n")
number = random.randrange(1,100)

print(name, "I am thinking of a number between 1 and 100\n")
guess = int(input("You're guess? "))

while guess != number:
    if guess < number:
        print("You're guess was too low")
        guess = int(input("You're guess? "))
    elif guess > number:
        print("You're guess was too high")
        guess = int(input("You're guess? "))
print("Correct!")
    

