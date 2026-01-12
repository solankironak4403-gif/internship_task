#student mark analysis using dictionary
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}
total_marks = sum(marks.values())
average_marks = total_marks / len(marks)
highest_scorer = max(marks, key=marks.get)
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Scorer: {highest_scorer} with {marks[highest_scorer]} marks")
