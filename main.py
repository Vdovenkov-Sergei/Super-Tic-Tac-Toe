from copy import deepcopy
import os

SIZE = 3
CROSS, CIRCLE = f"\x1b[38;5;27mX\x1b[0m", f"\x1b[38;5;9mO\x1b[0m"
WIDTH = SIZE * SIZE * 2 + 1
base_matrix = [[" "] * SIZE for _ in range(SIZE)]
field = [deepcopy(base_matrix) for _ in range(SIZE * SIZE)]


def print_field():
    print("-" * WIDTH)
    for i in range(SIZE):
        idx = i * SIZE
        for j in range(SIZE):
            row_m1 = " ".join(field[idx][j])
            row_m2 = " ".join(field[idx + 1][j])
            row_m3 = " ".join(field[idx + 2][j])
            total_row = f"{'|'}{'|'.join([row_m1, row_m2, row_m3])}{'|'}"
            print(total_row)
        print("-" * WIDTH)


matrix_idx, step, empty_ceils = 0, 0, SIZE**SIZE
print_field()

while True:
    if not empty_ceils:
        break

    info = input("\n> ")
    if info.lower() == "end":
        break

    x, y = map(int, info.split())
    if not (0 <= x < SIZE and 0 <= y < SIZE):
        print(f"Incorrect input coords ({x}; {y})")
    elif field[matrix_idx][x][y] != " ":
        print(f"Ceil ({x}; {y}) already matched")
    else:
        field[matrix_idx][x][y] = (CROSS, CIRCLE)[step]
        step = (step + 1) % 2
        matrix_idx = x * SIZE + y
        empty_ceils -= 1

    os.system("cls" if os.name == "posix" else "clear")
    print_field()
