import numpy as np

serial_number = int(input())

X, Y = 300, 300

rack_id = np.array([range(X)] * Y)
Y_coord = rack_id.copy().T + 1

rack_id += 10
power_level = rack_id * Y_coord
power_level += serial_number
power_level *= rack_id
power_level %= 1000
power_level = power_level // 100
power_level -= 5
power_level = power_level.astype(np.int8)

power_level_cum = np.concatenate((np.zeros((300, 1), dtype=np.int8), np.cumsum(power_level, axis=1)), axis=1)

scores = [power_level[:, 1:]]
max_score = power_level.max()
y, x = np.unravel_index(power_level.argmax(), power_level.shape)
max_size = 1
for size in range(2, X+1):
    score = np.array([[(power_level_cum[i:i+size, j+size] - power_level_cum[i:i+size, j]).sum() for j in range(0, Y - size + 1)] for i in range(X - size + 1)])
    new_score = score.max()
    if new_score > max_score:
        max_score = new_score
        y, x = np.unravel_index(score.argmax(), score.shape)
        max_size = size
    print("Size={:3d}, X={:3d}, Y={:3d}, Max Size{:3d}, Max Score={:3d}".format(size, x+1, y+1, max_size, max_score), end='\r', flush=True)

print()
x += 1
y += 1
print(x, y, max_size)
print(max_score)

