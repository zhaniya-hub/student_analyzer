from student_analyzer import calculate_average, get_status, analyze_student


grades = [85, 90, 78, 92, 88]

average = calculate_average(grades)

print("Орташа баға:", average)
print("Статус:", get_status(average))

student = analyze_student("Aruzhan", grades)

print("Студент:", student["name"])
print("Орташа балл:", student["average"])
print("Статус:", student["status"])
