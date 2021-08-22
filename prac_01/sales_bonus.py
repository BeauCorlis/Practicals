

"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
from webbrowser import get

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 1/10
    else:
        bonus = sales * 1.5/10
    print("Bonus: ", bonus, sep=' ')
    sales = float(input("Enter sales: $"))