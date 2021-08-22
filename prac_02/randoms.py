

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"line 1: the smallest number that could be seen was 5, while the largest was 20"
"line 2: the smallest number that could be seen was 3, while the largest was 9. No a 4 could not be produced"
"line 3: the smallest number that could be seen was 2.5, while the largest was 5.5"

print(random.randint(1, 100))