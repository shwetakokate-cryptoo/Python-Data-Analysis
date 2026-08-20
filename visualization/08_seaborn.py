import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():

    data = {
        "Department": [
            "AI", "AI", "AI", "Data Science",
            "Data Science", "Data Science"
        ],
        "Marks": [88, 92, 95, 76, 81, 69],
        "StudyHours": [5, 7, 8, 4, 6, 3]
    }

    students = pd.DataFrame(data)

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(data=students, x="Marks", bins=5, kde=True)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=students, x="Department", y="Marks")
    plt.title("Marks by Department")
    plt.xlabel("Department")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=students,
        x="StudyHours",
        y="Marks",
        hue="Department",
        s=100
    )
    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
