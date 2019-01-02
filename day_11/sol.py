#!/usr/bin/env python3
import numpy as np

serial_number = int(input())

X, Y = 300, 300

data = np.zeros((X, Y), dtype=np.int32)
rack_id = np.array([range(X)] * Y)
Y_coord = rack_id.copy().T + 1

rack_id += 11
power_level = rack_id * Y_coord
power_level += serial_number
power_level *= rack_id
power_level %= 1000
power_level = power_level // 100
power_level -= 5
power_level = power_level.astype(np.int8)

score = np.array([[power_level[i:i+3, j:j+3].sum() for j in range(Y-2)] for i in range(X-2)])

y, x = np.unravel_index(score.argmax(), score.shape)
x += 1
y += 1
print(x, y)
print(score.max())

