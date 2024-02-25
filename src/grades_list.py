import json

def save_grades_to_json(grades_of_students, grades_list):

with open ('grades_list.txt','w') as list:
    json.dump(grades_of_students, list)