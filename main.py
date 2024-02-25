from src.professor import professor
from src.student import student
from src.exception import *

# Create a professor
prof = professor("John Doe", "P001", "Associate Professor")

# Take courses
try:
    prof.take_course("Mathematics")
    prof.take_course("Physics")
    prof.take_course("Chemistry") # Raises MaxCourseLimitError
except MaxCourseLimitError as e:
    print(e)

# Insert grades
try:
    prof.insert_grades("S001", [15, 18, 20])
    prof.insert_grades("S002", [10, 12, 9]) # Raises InvalidGradeError
except InvalidGradeError as e:
    print(e)

# Create a student
stud = student("Alice", "S001", None)

# Select a course
stud.select_course("Mathematics")

# Calculate average
grades = [15, 18, 20]
try:
    average = stud.calculate_average(grades)
    print("Average:", average)
    print("Final Status:", stud.final_status(average))
except InvalidGradeError as e:
    print(e)