"""Chapter 9 project: Student Subject Enrollment Tracker.
Reconstructed from manuscript project descriptions; not a verbatim screenshot transcription.
"""

def main():
    enrollments = {"Alice": {"Python", "Math"}, "Bob": {"Python", "English"},
                   "Chloe": {"Math", "English"}}
    print("========== SUBJECT ENROLLMENT TRACKER ==========")
    for student, subjects in enrollments.items():
        print(student, sorted(subjects))
    names = list(enrollments)
    print("Common subjects for", names[0], "and", names[1],
          sorted(enrollments[names[0]] & enrollments[names[1]]))
    all_subjects = set().union(*enrollments.values())
    for subject in sorted(all_subjects):
        print(subject, "enrolled:", [n for n, s in enrollments.items() if subject in s])

if __name__ == "__main__":
    main()
