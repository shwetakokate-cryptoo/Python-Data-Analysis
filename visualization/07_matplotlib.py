import matplotlib.pyplot as plt


def main():

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [120, 150, 135, 180, 210, 195]

    plt.figure(figsize=(8, 5))

    plt.plot(
        months,
        sales,
        marker="o",
        linewidth=2
    )

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
