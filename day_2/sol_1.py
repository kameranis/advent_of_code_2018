import sys
from collections import Counter

counter_2 = 0
counter_3 = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        letter_counter = set(Counter(line).values())
        if 2 in letter_counter: counter_2 += 1
        if 3 in letter_counter: counter_3 += 1
print(counter_2 * counter_3)
