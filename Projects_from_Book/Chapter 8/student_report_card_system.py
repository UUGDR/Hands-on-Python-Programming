"""Chapter 8 project: Student Report Card System.
Reconstructed from manuscript project descriptions; not a verbatim screenshot transcription.
"""

def report_card(students):
    print("========== STUDENT REPORT CARD ==========")
    for name, marks in students.items():
        if not marks:
            continue
        average = sum(marks.values()) / len(marks)
        grade = "A" if average >= 90 else "B" if average >= 80 else "C" if average >= 70 else "D" if average >= 60 else "F"
        print(f"{name}: {marks} | Average: {average:.2f} | Grade: {grade}")

if __name__ == "__main__":
    students = {"Alice": {"Python": 92, "Math": 88, "English": 95},
                "Bob": {"Python": 74, "Math": 68, "English": 79}}
    report_card(students)
