class AvgException(Exception):
    def __init__(self, average, msage = "you crossed the extremes"):
        self.average = average
        self.message = msage
        super().__init__(self.message)

        try:
            average = int(input())
            if average > 20 or < 0:
                raise AvgException(average)
        except AvgException as ae:
            ("invalid input")


class MaxCourseLimitError(Exception):
    def __init__(self, course, message = "you crossed the limits"):
        self.course = course
        self.messagee = message
        super().__init__(self.message)

        try:
            course = list(input())
            if len(course)> 3:
                raise CrsException(course)
        except CrsException as ce:
            ("invalid input")

class InvalidGradeError(Exception):
    def __init__(self, grades, message = "you crossed the limits"):
        self.grades = grades
        self.message = message
        super().__init__(self.message)

class NameTooLongError(Exception):
    def __init__(self, name, message="Name must be 16 characters or fewer."):
        self.name = name
        self.message = message
        super().__init__(self.message)