def calculate_average (filename):

    with open('grades_list.txt','r') as fh:
        grades_list = fh.readlines()
        grades = [float(grade.strip()) for grade in grades_list]

        total = sum(grades)
        return total/len(grades)
        

input_filename = input('file:')
average = calculate_average(input_filename)
print("Average:", average)
