

"""
CP1404 Practical - List exercises
"""

"""
Question 1: Basic list operations
"""

numbers = []
for i in range(5):
    number = float(input("What number? "))
    numbers.append(number)

print("The initial values was ", numbers[0])
print("The final value was ", numbers[4])
print("The selected number that proved to be the smallest was ", min(numbers))
print("The selected number that proved to be the largest was ", max(numbers))
print("The average of the selected numbers is ", sum(numbers) / len(numbers))


"""
Question 2: Woefully inadequate security checker
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = input("Please enter your username: ")
if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")

