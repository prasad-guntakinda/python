import random

while True:
    choice = input("Roll a dice? (y/n) : ")

    if choice == 'y':
        print("You rolled a dice!")
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(
            f"your dice values are: {die1} and {die2}, Total: {die1 + die2} ")
    elif choice == 'n':
        print("Exiting the program.")
        break
    else:
        print("Invalid input")
