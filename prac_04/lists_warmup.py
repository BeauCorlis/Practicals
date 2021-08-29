

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
What values do the following expressions have?
"""

numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = [1, 5]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 5, 9, 2, 6, 5, 3]

"""
Change the first element of numbers to "ten" (the string, not the number 10)
"""

numbers = ["ten", 1, 4, 1, 5, 9, 2] "or" numbers[0] = "ten"

"""
Change the last element of numbers to 1
"""

numbers = ["ten", 1, 4, 1, 5, 9, 1] "or" numbers[-1] = 1

"""
Get all the elements from the numbers except the first two (slice)
"""

numbers[2:] = [4, 1, 5, 9, 2]

"""check if 9 is an element of numbers"""

9 in numbers
