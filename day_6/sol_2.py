import sys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

coords = np.array([[int(i) for i in line.split(', ')] for line in sys.stdin])

x_min = coords[:, 0].min()
x_max = coords[:, 0].max()
y_min = coords[:, 1].min()
y_max = coords[:, 1].max()

territory = 0

max_dist = (x_max - x_min) + (y_max - y_min)
for i in range(x_min, x_max + 1):
    for j in range(y_min, y_max + 1):
        distance = 0
        for curr_point, (x, y) in enumerate(coords):
            dist = abs(x -i) + abs(y - j)
            distance += dist
        if distance < 10000:
            territory += 1
print(territory)

