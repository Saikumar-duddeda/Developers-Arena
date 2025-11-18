# Student Grade Calculator - Simple Version

results = []  # List to store student results

# Taking input
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

# Determine grade
if marks >= 90:
    grade = "A"
    comment = "Excellent performance!"
elif marks >= 75:
    grade = "B"
    comment = "Great job, keep it up!"
elif marks >= 60:
    grade = "C"
    comment = "Good effort, you can do better."
elif marks >= 40:
    grade = "D"
    comment = "Needs improvement."
else:
    grade = "F"
    comment = "Failed. Focus & try again."

# Store result
student_result = {
    "name": name,
    "marks": marks,
    "grade": grade,
    "comment": comment
}

results.append(student_result)

# Display output
print("\n===== STUDENT GRADE REPORT =====")
print("Name    :", name)
print("Marks   :", marks)
print("Grade   :", grade)
print("Comment :", comment)
print("================================\n")

# Show stored list
print("Stored Results:", results)
