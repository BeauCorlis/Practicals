"""
CP1404 Practical - "Quick Pick" Lottery Ticket Generator
"""

import random

picks_on_each_line = 6
smallest_quick_pick_value = 1
largest_quick_pick_value = 45


def main():
    total_number_of_picks = int(input("How many pick would you like? "))

    for i in range(total_number_of_picks):
        picks = []
        for j in range(picks_on_each_line):
            random_number = random.randint(smallest_quick_pick_value, largest_quick_pick_value)
            while random_number in picks:
                random_number = random.randint(smallest_quick_pick_value, largest_quick_pick_value)
            picks.append(random_number)

        random_picks = [random_number for random_number in picks]
        print(random_picks)


main()
