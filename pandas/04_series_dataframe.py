import pandas as pd


def main():

    names = pd.Series(
        ["Shweta", "Aarav", "Priya", "Rahul"],
        name="Name"
    )

    print("Pandas Series:")
    print(names)

    data = {
        "Name": ["Shweta", "Aarav", "Priya", "Rahul"],
        "Age": [20, 21, 20, 22],
        "Marks": [88, 76, 92, 81]
    }

    students = pd.DataFrame(data)

    print("\nDataFrame:")
    print(students)

    print("\nColumns:")
    print(students.columns)

    print("\nShape:")
    print(students.shape)

    print("\nFirst Two Rows:")
    print(students.head(2))

    print("\nMarks Column:")
    print(students["Marks"])


if __name__ == "__main__":
    main()
