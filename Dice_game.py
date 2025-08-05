# Ask: roll the dice?
# If yes, roll dice. If no, don't roll the dice. If neither, say invalid choice.
import random

choice = input("Roll the dice? (yes/no): ")

if choice.lower() == "yes":
    dice = random.randint(1, 6)
    print("You rolled a", dice)
elif choice.lower() == "no":
    print("Maybe next time!")
else:
    print("Invalid choice.")
