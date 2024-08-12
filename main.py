from copy import deepcopy
import os

SIZE = 3
CROSS, CIRCLE = f"\x1b[38;5;27mX\x1b[0m", f"\x1b[38;5;9mO\x1b[0m"
WIDTH = SIZE * SIZE * 2 + 1
base_matrix = [[" "] * SIZE for _ in range(SIZE)]
field = [deepcopy(base_matrix) for _ in range(SIZE * SIZE)]
winner_ceil = [None for _ in range(SIZE * SIZE)]
big_cross, big_circle = [], []


def print_field():
    print("-" * WIDTH)
    for i in range(0, SIZE * SIZE, SIZE):
        for j in range(SIZE):
            total_row = "|"
            for k in range(SIZE):
                if matrix_idx != i + k and not winner_ceil[i + k]:
                    total_row += " ".join(field[i + k][j]) + "|"
                else:
                    total_row += (big_cross[k], big_circle[k])[step] + "|"
            print(total_row)
        print("-" * WIDTH)


def check_combinations():
    pass


matrix_idx, step, empty_ceils = 0, 0, SIZE**SIZE
print_field()

while True:
    info = input("\n> ")
    os.system("cls" if os.name == "posix" else "clear")

    try:
        x, y = map(int, info.split())
        if field[matrix_idx][x][y] != " ":
            print(f"Ceil ({x}; {y}) already matched")
        else:
            field[matrix_idx][x][y] = (CROSS, CIRCLE)[step]
            if not winner_ceil[matrix_idx]:
                check_combinations(field[matrix_idx])
            step = (step + 1) % 2
            matrix_idx = x * SIZE + y
            empty_ceils -= 1
    except ValueError:
        print("Incorrect input")
    except IndexError:
        print(f"Incorrect input coords ({x}; {y})")

    winner = check_combinations(winner_ceil)
    print_field()
    if winner:
        print(f"Winner - {winner}")
        break
    if not empty_ceils:
        print("Draw!")
        break

# \ /
#  X
# / \

# /‾\
# | |
# \_/
