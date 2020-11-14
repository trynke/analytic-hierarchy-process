import numpy as np


def vector(matrix):
    """Function for calculating a priority vector"""
    vect = matrix[:, 0]
    w = vect / vect.sum()
    return w

def matrix(number):
    """Function for creating a pairwise matrix"""
    A = np.ones([number, number])
    importance = [i for i in range(1, 10)] # list of allowed importance values
    for i in range(0, number):
        for j in range(0, number):
            if i < j:
                a = str(input(f'How much more important is criterion {i} than criterion {j}? Type an integer from 1 to 9: '))
                if a.isdigit() and float(a) in importance: # error handling
                    A[i,j] = float(a)
                    A[j, i] = 1 / float(a)
                else:
                    print("It is an incorrect value. Let's start again \n")
                    main()
    return A

def main():
    number = str(input("How many criteria do you want to enter? Type an integer: "))
    if number.isdigit(): # error handling
        A = matrix(int(number))
        weights = vector(A)
        for i in range(len(weights)):
            print(f'Criterion {i} = {np.round(weights[i], 2)}')
    else:
        print("Something went wrong. Let's try again \n")
        main()


if __name__ == "__main__":
    main()