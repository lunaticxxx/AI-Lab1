import random
import time

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
        while True:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            new_x = pos_x + dx
            new_y = pos_y + dy
            if 0 <= new_x < x and 0 <= new_y < y:
                break
        pos_x = new_x
        pos_y = new_y
        steps += 1
        print(f"Step {steps}: Moved to Room[{pos_x}, {pos_y}].")

    dirty = any(cell == 1 for row in grid for cell in row)
    if not dirty:
        break

print(f"\nAll rooms clean! Total steps = {steps}")
