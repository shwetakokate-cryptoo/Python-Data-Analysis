import pandas as pd


def main():

    data = {
        "Name": ["Shweta", "Aarav", "Priya", "Rahul", "Aarav"],
        "Age": [20, 21, None, 22, 21],
        "Marks": [88, 76, 92, None, 76],
        "City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"]
    }

    students = pd.DataFrame(data)

    print("Original Data:")
    print(students)

    print("\nMissing Values:")
    print(students.isnull().sum())

    students["Age"] = students["Age"].fillna(students["Age"].mean())
    students["Marks"] = students["Marks"].fillna(students["Marks"].mean())

    students = students.drop_duplicates()

    students["Age"] = students["Age"].astype(int)

    print("\nCleaned Data:")
    print(students)

    print("\nData Types:")
    print(students.dtypes)


if __name__ == "__main__":
    main()
