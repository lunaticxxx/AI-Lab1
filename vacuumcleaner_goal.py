import random
import time

x = int(input("Enter the number of rows (x): "))
y = int(input("Enter the number of columns (y): "))

random.seed(time.time())
grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

print("Randomly assigned grid states:")
for row in grid:
    print(" ".join(str(cell) for cell in row))

initial_pos = [random.randint(0, x - 1), random.randint(0, y - 1)]
print(f"\nInitial Position in the Grid: Room[{initial_pos[0]}, {initial_pos[1]}] => {grid[initial_pos[0]][initial_pos[1]]}")

directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],          [0, 1],
    [1, -1],  [1, 0], [1, 1]
]

steps = 0

while True:
    if grid[initial_pos[0]][initial_pos[1]] == 1:
        grid[initial_pos[0]][initial_pos[1]] = 0
        steps += 1
        print(f"Step {steps}: Room[{initial_pos[0]}, {initial_pos[1]}] was dirty. Cleaned it.")
    else:
        moved = False
        for d in directions:
            ni = initial_pos[0] + d[0]
            nj = initial_pos[1] + d[1]
            if 0 <= ni < x and 0 <= nj < y and grid[ni][nj] == 1:
                initial_pos[0], initial_pos[1] = ni, nj
                steps += 1
                print(f"Step {steps}: Current room clean. Moved to dirty neighbor Room[{ni}, {nj}].")
                moved = True
                break

        if not moved:
            found = False
            for i in range(x):
                for j in range(y):
                    if grid[i][j] == 1:
                        initial_pos[0], initial_pos[1] = i, j
                        steps += 1
                        print(f"Step {steps}: No dirty neighbor. Moving to Room[{i}, {j}].")
                        found = True
                        break
                if found:
                    break
            if not found:
                print(f"\nAll rooms are clean! Cleaning completed in {steps} steps.")
                break

print("\nFinal grid state:")
for i in range(x):
    for j in range(y):
        if i == initial_pos[0] and j == initial_pos[1]:
            print("P", end=" ")
        else:
            print(grid[i][j], end=" ")
    print()
