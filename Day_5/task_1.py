# Dictionary Comprehension for Data Transformation

students = {
    "Dharm": 78,
    "Azim": 34,
    "Vedant": 56,
    "Ronak": 89,
    "Dharmit": 42
}

result = {name: "Pass" if marks >= 40 else "Fail"
          for name, marks in students.items()}

print("Student Results:", result)
                     