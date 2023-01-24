"""Class average program with sentinel-controlled iteration"""

# initialization phase
sum_of_grades = 0
grade_counter = 0

# processing phase
grade = int(input('Enter grade, -1 to end: '))

while grade != -1:
    sum_of_grades += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))
    
# termination phase
if grade_counter > 0:
    average = sum_of_grades / grade_counter
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')
