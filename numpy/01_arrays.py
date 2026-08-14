import numpy as np


def main():

    numbers = np.array([10, 20, 30, 40, 50])

    print("Array:")
    print(numbers)

    print("\nData Type:")
    print(numbers.dtype)

    print("\nShape:")
    print(numbers.shape)

    print("\nDimensions:")
    print(numbers.ndim)

    print("\nSize:")
    print(numbers.size)


if __name__ == "__main__":
    main()
