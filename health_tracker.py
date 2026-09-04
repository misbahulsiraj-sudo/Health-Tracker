import csv
import os
from datetime import datetime

FILE_NAME = "health_data.csv"


def create_file():
    """Create CSV file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Date", "Name", "Age", "Height(cm)", "Weight(kg)", "BMI", "Status"]
            )


def calculate_bmi(weight, height_cm):
    """Calculate BMI."""
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def bmi_status(bmi):
    """Return BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def add_record():
    """Add a new health record."""
    print("\n=== Add Health Record ===")

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()

    try:
        height = float(input("Enter Height (cm): "))
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return

    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, name, age, height, weight, bmi, status])

    print("\n✅ Record Saved Successfully!")
    print(f"BMI: {bmi}")
    print(f"Health Status: {status}")


def view_records():
    """Display all records."""
    print("\n=== Health Records ===")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            records = list(reader)

            if len(records) <= 1:
                print("No records found.")
                return

            for row in records:
                print(" | ".join(row))

    except FileNotFoundError:
        print("No records found.")


def search_record():
    """Search record by name."""
    name = input("\nEnter name to search: ").strip().lower()

    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 1 and row[1].lower() == name:
                    print("\nFound Record:")
                    print(" | ".join(row))
                    found = True

        if not found:
            print("❌ No record found.")

    except FileNotFoundError:
        print("No records available.")


def health_tips():
    """Display health tips based on BMI."""
    try:
        weight = float(input("\nEnter Weight (kg): "))
        height = float(input("Enter Height (cm): "))
    except ValueError:
        print("❌ Invalid input.")
        return

    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Status: {status}")

    if status == "Underweight":
        print("Tip: Eat nutritious foods and increase protein intake.")
    elif status == "Normal Weight":
        print("Tip: Maintain your healthy lifestyle.")
    elif status == "Overweight":
        print("Tip: Exercise regularly and reduce processed foods.")
    else:
        print("Tip: Consult a healthcare professional and follow a fitness plan.")


def menu():
    create_file()

    while True:
        print("\n" + "=" * 40)
        print("      HEALTH TRACKER SYSTEM")
        print("=" * 40)
        print("1. Add Health Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. BMI Health Tips")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            health_tips()
        elif choice == "5":
            print("\n👋 Thank you for using Health Tracker!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()