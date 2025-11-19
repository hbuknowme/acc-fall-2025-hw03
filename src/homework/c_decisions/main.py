from src.homework.c_decisions.decisions import get_letter_grade

print("MAIN MENU\n")
print("1-Letter grade using if")
print("2-Letter grade using switch")
print("3-Exit")

choice = input("\nEnter your choice: ")

def switch_letter_grade(grade):
    if grade < 0 or grade > 100:
        return "Invalid"
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

if choice == "1":
    num = int(input("Enter a grade (0-100): "))
    if 0 <= num <= 100:
        print("Letter grade:", get_letter_grade(num))
    else:
        print("Number out of range.")

elif choice == "2":
    num = int(input("Enter a grade (0-100): "))
    if 0 <= num <= 100:
        print("Letter grade:", switch_letter_grade(num))
    else:
        print("Number out of range.")

elif choice == "3":
    print("Goodbye.")
else:
    print("Invalid selection.")
