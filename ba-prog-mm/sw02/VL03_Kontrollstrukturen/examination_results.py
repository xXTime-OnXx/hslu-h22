"""Using nested control statements to analyze examination results."""

# initialize variables
number_passed = 0
number_failed = 0

# process 10 students
for student in range(10):
    result = int(input(f'Enter result (1=pass, 2=fail) for student {student + 1}: '))
    
    if result == 1:
        number_passed += 1
    else: 
        number_failed += 1
        
# termination phase
print('Passed:', number_passed)
print('Failed:', number_failed)

if number_passed > 8:
    print('Bonus to instructor')
