import numpy as np

def roll_dice():
    return np.random.randint(1, 7)

def main():
    print("Welcome to the Roll Dice Game!")
    while True:
        roll = input("Press 'r' to roll the dice or 'q' to quit: ").lower()
        if roll == 'r':
            print(f"You rolled a {roll_dice()}")
        elif roll == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()