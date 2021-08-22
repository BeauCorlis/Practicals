

"""
CP1404 - Practical
expectations demo
"""

finished = False
numerator = 0
denominator = 0
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        finished = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!", numerator, denominator)
    print("Finished.")

"1. when a variable that isn't a number is entered"
"2. when 0 is entered as a value in the division formula"