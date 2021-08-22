

"""
CP1404/CP5632 - Practical
Program to request and display the number of items followed by calculating potential discounts and displaying the total price of said items.
"""

total = 0
n = int(input("Number of items: "))
while n < 0:
    print("Invalid number of items")
    n = int(input("Number of items: "))
for i in range(n):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(n, total))