import numpy as np


def main():

    data = np.array([10, 20, 20, 30, 40, 50, 60])

    print("Data:")
    print(data)

    print("\nMean:")
    print(np.mean(data))

    print("\nMedian:")
    print(np.median(data))

    print("\nStandard Deviation:")
    print(np.std(data))

    print("\nVariance:")
    print(np.var(data))

    print("\nMinimum:")
    print(np.min(data))

    print("\nMaximum:")
    print(np.max(data))

    print("\n25th Percentile:")
    print(np.percentile(data, 25))

    print("\n50th Percentile:")
    print(np.percentile(data, 50))

    print("\n75th Percentile:")
    print(np.percentile(data, 75))


if __name__ == "__main__":
    main()
