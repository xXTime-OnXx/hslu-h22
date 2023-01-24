# decisions.py
"""Comparing integers using if statements and comparison operators."""

print('Enter two integers, and I will tell you the relationhips they satisfy.')

# read first integer
number1 = int(input('Enter first integer: '))

# read second integer
number2 = int(input('Enter second integer: '))

# Compare integers and print messages based on conditions that evaluate to True
if number1 == number2:
    print(number1, 'is equal to', number2)
    
if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)
    
if number1 > number2:
    print(number1, 'is greater than', number2)
    
if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
    
if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)