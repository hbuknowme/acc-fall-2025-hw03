def get_letter_grade(numerical_grade):
    if 90 <= numerical_grade <= 100:
        return "A"
    elif 80 <= numerical_grade <= 89:
        return "B"
    elif 70 <= numerical_grade <= 79:
        return "C"
    elif 60 <= numerical_grade <= 69:
        return "D"
    elif 0 <= numerical_grade <= 59:
        return "F"
    else:
        return "Invalid"
