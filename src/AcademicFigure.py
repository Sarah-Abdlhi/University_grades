class academic_figure ():
    def __init__(self, name, id, grade, unit, rank):
        
        self.name = name
        self.id = id
        self.grade = grade
        self.unit = unit
        self.rank = rank


        #def repr
        def average (self):

            total = sum(self.grade)
            return total/len (self.grade)


