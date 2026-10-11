import tkinter as tk
import student_utils

students = ["Anna", "Ivan", "Olha"]

def show_report():
    count = input("Enter a count of grades: ")
    report = []
    for student in students:
        grades = student_utils.generate_grades(int(count))
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        report.append((student, grades, avg, level))
    print(report)

    display_lines = []
    for student, grades, avg, level in report:
        display_lines.append(f"{student}: {grades} | Average: {avg:.2f} | Level: {level}")

    label.config(text="\n".join(display_lines))

root = tk.Tk()
root.title("Student Report")
root.geometry("400x300")

button = tk.Button(root, text="Show Report", command=show_report)
button.pack(pady=10)

label = tk.Label(root, text="Student Report", justify="left", font=("Times New Roman", 12))
label.pack(pady=20)

show_report()

root.mainloop()