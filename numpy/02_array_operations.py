import numpy as np


def main():

    numbers = np.array([10, 20, 30, 40, 50])

    print("Original Array:")
    print(numbers)

    print("\nFirst Element:")
    print(numbers[0])

    print("\nLast Element:")
    print(numbers[-1])

    print("\nArray Slice:")
    print(numbers[1:4])

    print("\nAddition:")
    print(numbers + 5)

    print("\nMultiplication:")
    print(numbers * 2)

    print("\nSquare:")
    print(numbers ** 2)

    print("\nMean:")
    print(np.mean(numbers))

    print("\nMaximum:")
    print(np.max(numbers))

    print("\nMinimum:")
    print(np.min(numbers))


if __name__ == "__main__":
    main()
