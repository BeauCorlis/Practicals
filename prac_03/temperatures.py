

"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()



while choice != "Q":
    if choice == "C":
        method_name(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit_to_celcius(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

def fahrenheit_to_celcius(fahrenheit):
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)


def method_name(celsius):
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32

