

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    worked_months_total = int(input("How many months? "))

    for month in range(1, worked_months_total + 1):
        income = float(input("Enter income for month {:2}: ".format(month)))
        incomes.append(income)
    else:
        print("Invalid number of months")

    print_income_report(incomes, worked_months_total)


def print_income_report(incomes, worked_months_total):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, worked_months_total + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
