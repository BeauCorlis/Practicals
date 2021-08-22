

"""
CP1404/CP5632 - Practical
Program to display all odd values between 1 and 21.
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
CP1404/CP5632 - Practical
a. Program to display all values on 10 between 0 and 100.
"""

for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""
CP1404/CP5632 - Practical
b. Program to display values counting down from 20 to 1.
"""

for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
CP1404/CP5632 - Practical
c. Program to display the requested amount of stars from the user.
"""

num_stars = int(input("Enter star amount: "))
for i in range(num_stars):
    print('*', end=' ')
print()

"""
CP1404/CP5632 - Practical
d. Program to display the requested rows of stars from the user. Because of the previous question num_stars is already defined. As such the inital line in the script doesn't need to be written.
"""

for i in range(1, num_stars + 1):
    print('*' * i)
print()