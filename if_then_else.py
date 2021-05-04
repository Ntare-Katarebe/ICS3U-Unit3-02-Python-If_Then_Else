#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program guesses your number
#    with numbers inputted from the user

import random


def main():
    # This function guesses your number

    # input
    guessed_number = int(input("Enter the number between 0 - 9: "))
    random_number = random.randint(0, 9)
    print("")

    # process/output
    if guessed_number == random_number:
        print("You guessed correct!")
    else:
        print("Incorrect, the number was {}".format(random_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
