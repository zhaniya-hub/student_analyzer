def calculate_average(grades):
    """Студенттің орташа бағасын есептейді."""
    if not grades:
        return 0

    return sum(grades) / len(grades)


def get_status(average):
    """Орташа бағаға байланысты студенттің статусын анықтайды."""
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 50:
        return "Satisfactory"
    else:
        return "Fail"


def analyze_student(name, grades):
    """Студент туралы толық ақпарат береді."""
    average = calculate_average(grades)
    status = get_status(average)

    return {
        "name": name,
        "average": round(average, 2),
        "status": status
    }