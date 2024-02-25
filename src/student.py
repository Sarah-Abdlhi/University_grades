from src.AcademicFigure import academic_figure
from src.exception import InvalidGradeError
from src.grades_list import save_grades_to_json

class student (academic_figure):
    def __init__(self, name, id, grade)
        super().__init__(name, id, grade)
        s


def course_selection(self, course):
    self.course = course

def calculate_average(self):
    total = sum(self.grade)
    return total/ len(self.grade)

def final_status(self):
    average = self.calculate_average()
    rerurn "pass" if average >= 10 else "fail"