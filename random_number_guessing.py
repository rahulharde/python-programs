#Number guessing game program

import random

# Take a number from the user
n = int(input("Enter your number (1-100): "))

# Generate a random number
r = random.randint(1, 100)

print("\nComputer's Number:", r)

# Compare user's number with computer's number
if n == r:
    print("Correct! Your number matches the computer's number.")

elif n > r:
    print("Your number is greater than the computer's number.")
    print("Difference:", n - r)

elif n < r:
    print("Your number is smaller than the computer's number.")
    print("Difference:", r - n)
