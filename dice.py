import random

while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == "yes":
        print("🎲 You rolled:", random.randint(1, 6))
    elif roll == "no":
        print("Goodbye!")
        break
    else:
        print("Please type 'yes' or 'no'.")
