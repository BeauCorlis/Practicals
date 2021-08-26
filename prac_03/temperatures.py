

"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()



def fahrenheit_to_celcius(fahrenheit):
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)

def celsius_to_fahrenheit(celsius):
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32

def main():
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit_to_celcius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")



main()
