import sys
import re
import numpy as np

extractor = re.compile(r"#(\d+) @ (\d+).(\d+): (\d+)x(\d+)")

freq = 0
claims = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        m = extractor.search(line)
        claim_id, left, top, length, width = [int(group) for group in m.groups()]
        claims[claim_id] = (left, top, left+length, top+width)
x = max(c[2] for c in claims.values())
y = max(c[3] for c in claims.values())

array = np.zeros([x, y])
for top, left, bottom, right in claims.values():
    array[top:bottom, left:right] += 1
print((array > 1).sum())
