import sys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

coords = np.array([[int(i) for i in line.split(', ')] for line in sys.stdin])
convex_hull = ConvexHull(coords)
out_vertices = convex_hull.vertices
print(convex_hull.vertices)
plt.plot(coords[:,0], coords[:,1], 'o')
for simplex in convex_hull.simplices:
    plt.plot(coords[simplex, 0], coords[simplex, 1], 'k-')
plt.plot(coords[convex_hull.vertices,0], coords[convex_hull.vertices,1], 'r--', lw=2)
plt.plot(coords[convex_hull.vertices[0],0], coords[convex_hull.vertices[0],1], 'ro')
plt.show()

x_min = coords[:, 0].min()
x_max = coords[:, 0].max()
y_min = coords[:, 1].min()
y_max = coords[:, 1].max()

territory = defaultdict(int)

max_dist = (x_max - x_min) + (y_max - y_min)
for i in range(x_min, x_max + 1):
    for j in range(y_min, y_max + 1):
        best = max_dist
        count = 0
        point = None
        for curr_point, (x, y) in enumerate(coords):
            dist = abs(x -i) + abs(y - j)
            if dist == best:
                count += 1
            elif dist < best:
                best = dist
                count = 1
                point = curr_point
        if (count == 1) and point not in out_vertices:
            territory[point] += 1
print(max(v for v in territory.values()))

