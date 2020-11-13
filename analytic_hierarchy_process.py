import numpy as np
import pandas as pd

def matrix(number):
    pass

def main():
    number = str(input("How many criteria do you want to enter? Type an integer: "))
    if number.isdigit():
        matrix(number)
    else:
        print("Something went wrong. Let's try again")
        main()


if __name__ == "__main__":
    main()