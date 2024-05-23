
import random
# List Comprehension:
#list = [1,2,3,4,5,6,7]
#new_list = [i**2 for i in list]
#print(new_list)

num_string = '1, 3, 4, 6, 8, 11, 34, 67'
list_of_strings = num_string.split(",")
list_of_strings_2  =  [int(i) for i in list_of_strings if int(i)%2 == 0]
print(list_of_strings_2)


names = ["Brad", "Julia", "Omesh", "Mariya"]

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)


passed_students = {student:score for (student,score) in students_scores.items() if score > 60}
print(passed_students)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_df = pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)