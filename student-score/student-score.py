import numpy as np

# Set precision for better readability
np.set_printoptions(precision=2, floatmode='fixed')

# Given scores array
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1. Calculate and print the average score for each student.
student_averages = scores.mean(axis=1)
print("Average score for each student:", student_averages)
print("\n")

# 2. Calculate and print the average score for each subject.
subject_averages = scores.mean(axis=0)
print("Average score for each subject:", subject_averages)
print("\n")

# 3. Identify the student (row index) with the highest total score.
total_scores = scores.sum(axis=1)
highest_total_index = np.argmax(total_scores)
print("Student with the highest total score is at row index:", highest_total_index)
print("\n")

# 4. Add 5 bonus points to the third subject for all students
scores_with_bonus = scores.copy()
scores_with_bonus[:, 2] += 5
print("Scores after adding 5 bonus points to the third subject:\n", scores_with_bonus)