import numpy as np

def matrix(number):
    """Function for creating a pairwise matrix"""
    A = np.ones([number, number])
    importance = [i for i in range(1, 10)]
    for i in range(0, number):
        for j in range(0, number):
            if i < j:
                a = str(input(f'How much more important is criterion {i} than criterion {j}? Type an integer from 1 to 9: '))
                if a.isdigit() and float(a) in importance:
                    A[i,j] = float(a)
                    A[j, i] = 1 / float(a)
                else:
                    print("It is an incorrect value. Let's start again \n")
                    main()

def main():
    number = str(input("How many criteria do you want to enter? Type an integer: "))
    if number.isdigit():
        matrix(int(number))
    else:
        print("Something went wrong. Let's try again \n")
        main()


if __name__ == "__main__":
    main()