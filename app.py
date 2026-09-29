import tkinter as tk
from tkinter import messagebox
from student_analyzer import analyze_student
def analyze():
    name = name_entry.get().strip()
    grades_text = grades_entry.get().strip()
    if not name or not grades_text:
        messagebox.showwarning(
            "Warning",
            "Please enter student name and grades."
        )
        return
    try:
        grades = [float(x.strip()) for x in grades_text.split(",")]
        if not grades:
            raise ValueError
        result = analyze_student(name, grades)
        average_label.config(
            text=f"{result['average']:.2f}"
        )
        status_label.config(
            text=result["status"]
        )
        student_label.config(
            text=result["name"]
        )
    except ValueError:
        messagebox.showerror(
            "Error",
            "Grades must be numbers separated by commas.\n\nExample: 85, 90, 78, 92"
        )
# Main window
root = tk.Tk()
root.title("Student Analyzer")
root.geometry("650x600")
root.resizable(False, False)
root.configure(bg="#0B1120")
# Header
header = tk.Frame(
    root,
    bg="#111C33",
    height=120
)
header.pack(fill="x")
title = tk.Label(
    header,
    text="🎓 STUDENT ANALYZER",
    font=("Segoe UI", 26, "bold"),
    bg="#111C33",
    fg="white"
)
title.pack(pady=(25, 5))
subtitle = tk.Label(
    header,
    text="Student Performance Analysis System",
    font=("Segoe UI", 11),
    bg="#111C33",
    fg="#94A3B8"
)
subtitle.pack()
# Main container
main = tk.Frame(
    root,
    bg="#0B1120"
)
main.pack(fill="both", expand=True, padx=45, pady=25)
# Student name
name_title = tk.Label(
    main,
    text="Student Name",
    font=("Segoe UI", 11, "bold"),
    bg="#0B1120",
    fg="#E2E8F0"
)
name_title.pack(anchor="w")
name_entry = tk.Entry(
    main,
    font=("Segoe UI", 13),
    bg="#111C33",
    fg="white",
    insertbackground="white",
    relief="flat"
)
name_entry.pack(fill="x", ipady=12, pady=(7, 18))
# Grades
grades_title = tk.Label(
    main,
    text="Grades",
    font=("Segoe UI", 11, "bold"),
    bg="#0B1120",
    fg="#E2E8F0"
)
grades_title.pack(anchor="w")
grades_entry = tk.Entry(
    main,
    font=("Segoe UI", 13),
    bg="#111C33",
    fg="white",
    insertbackground="white",
    relief="flat"
)
grades_entry.pack(fill="x", ipady=12, pady=(7, 20))
hint = tk.Label(
    main,
    text="Example: 85, 90, 78, 92, 88",
    font=("Segoe UI", 9),
    bg="#0B1120",
    fg="#64748B"
)
hint.pack(anchor="w")
# Analyze button
analyze_button = tk.Button(
    main,
    text="ANALYZE STUDENT",
    command=analyze,
    font=("Segoe UI", 12, "bold"),
    bg="#6366F1",
    fg="white",
    activebackground="#4F46E5",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
analyze_button.pack(fill="x", ipady=12, pady=25)
# Result card
result_frame = tk.Frame(
    main,
    bg="#111C33"
)
result_frame.pack(fill="x", pady=5)
result_title = tk.Label(
    result_frame,
    text="ANALYSIS RESULT",
    font=("Segoe UI", 10, "bold"),
    bg="#111C33",
    fg="#94A3B8"
)
result_title.pack(pady=(18, 10))
student_label = tk.Label(
    result_frame,
    text="Student: —",
    font=("Segoe UI", 13, "bold"),
    bg="#111C33",
    fg="white"
)
student_label.pack(pady=3)
average_text = tk.Label(
    result_frame,
    text="Average Grade",
    font=("Segoe UI", 10),
    bg="#111C33",
    fg="#94A3B8"
)
average_text.pack(pady=(12, 0))
average_label = tk.Label(
    result_frame,
    text="—",
    font=("Segoe UI", 28, "bold"),
    bg="#111C33",
    fg="#818CF8"
)
average_label.pack()
status_text = tk.Label(
    result_frame,
    text="Status",
    font=("Segoe UI", 10),
    bg="#111C33",
    fg="#94A3B8"
)
status_text.pack(pady=(8, 0))
status_label = tk.Label(
    result_frame,
    text="—",
    font=("Segoe UI", 18, "bold"),
    bg="#111C33",
    fg="#22C55E"
)
status_label.pack(pady=(0, 20))
# Footer
footer = tk.Label(
    root,
    text="Student Analyzer • Python Library Project",
    font=("Segoe UI", 9),
    bg="#0B1120",
    fg="#475569"
)
footer.pack(pady=(0, 15))
root.mainloop()