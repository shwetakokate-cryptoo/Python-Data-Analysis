import pandas as pd


def main():

    data = {
        "Name": [
            "Shweta",
            "Aarav",
            "Priya",
            "Rahul",
            "Neha",
            "Rohan"
        ],
        "Department": [
            "AI",
            "Data Science",
            "AI",
            "Data Science",
            "AI",
            "Data Science"
        ],
        "Marks": [88, 76, 92, 81, 95, 69],
        "City": [
            "Pune",
            "Mumbai",
            "Pune",
            "Nashik",
            "Mumbai",
            "Pune"
        ]
    }

    students = pd.DataFrame(data)

    print("Dataset:")
    print(students)

    print("\nStudents with Marks above 80:")
    print(students[students["Marks"] > 80])

    print("\nStudents Sorted by Marks:")
    print(students.sort_values("Marks", ascending=False))

    print("\nAverage Marks by Department:")
    print(students.groupby("Department")["Marks"].mean())

    print("\nMaximum Marks by Department:")
    print(students.groupby("Department")["Marks"].max())

    print("\nStudents by City:")
    print(students["City"].value_counts())

    print("\nOverall Statistics:")
    print(students["Marks"].describe())


if __name__ == "__main__":
    main()
