

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    Score_scheme(score)

def Score_scheme(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
