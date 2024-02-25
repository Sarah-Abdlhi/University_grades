from src.AcademicFigure import academic_figure
from src.exception import MaxCourseLimitError, InvalidGradeError
from src.grades_list import save_grades_to_json

class professor (academic_figure):
    def __init__(self, name, id, rank):
        super().__init__(name, id)
        self.rank = rank
        self.courses_taught = []
        

    def grade_insertion(self, student_id, grades):
        for grade in grades:
            if not 0<= grade <= 20:
                raise InvalidGradeError()
        save_grades_to_json({student_id:grades}, 'grades_list.txt')
        
    
    def take_course(self, course):
        if len(self.courses_taught) > 3:
            raise MaxCourseLimitError()
        self.courses_taught.append(course)

