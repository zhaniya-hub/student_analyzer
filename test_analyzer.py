from student_analyzer import calculate_average, get_status


def test_calculate_average():
    grades = [80, 90, 100]
    assert calculate_average(grades) == 90


def test_get_status():
    assert get_status(95) == "Excellent"
    assert get_status(80) == "Good"
    assert get_status(60) == "Satisfactory"
    assert get_status(40) == "Fail"