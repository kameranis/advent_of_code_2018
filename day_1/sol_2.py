import sys
from itertools import cycle

freq = 0
visited = set([0])
freqs = [int(line) for line in sys.stdin]
for d_freq in cycle(freqs):
    freq += d_freq
    if freq in visited:
        print(freq)
        break
    visited.add(freq)
