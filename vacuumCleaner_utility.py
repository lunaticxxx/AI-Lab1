import random
import time
import sys

def abs_val(a):
    return -a if a < 0 else a

x = int(input("Enter the number of rows (x): "))
y = int(input("Enter the number of columns (y): "))

random.seed(time.time())
grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

print("Initial grid state:")
for row in grid:
    print(" ".join(str(cell) for cell in row))

pos_x = random.randint(0, x - 1)
pos_y = random.randint(0, y - 1)
steps = 0

print(f"\nInitial Position: Room[{pos_x}, {pos_y}]")

while True:
    if grid[pos_x][pos_y] == 1:
        grid[pos_x][pos_y] = 0
        steps += 1
        print(f"Step {steps}: Cleaned Room[{pos_x}, {pos_y}].")
    else:
        min_dist = sys.maxsize
        target_x, target_y = -1, -1
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    dist = abs_val(i - pos_x) + abs_val(j - pos_y)
                    if dist < min_dist:
                        min_dist = dist
                        target_x, target_y = i, j

        if target_x == -1:
            break

        if target_x > pos_x:
            pos_x += 1
        elif target_x < pos_x:
            pos_x -= 1
        elif target_y > pos_y:
            pos_y += 1
        elif target_y < pos_y:
            pos_y -= 1

        steps += 1
        print(f"Step {steps}: Moved to Room[{pos_x}, {pos_y}].")

print(f"\nAll rooms clean! Total steps = {steps}")
