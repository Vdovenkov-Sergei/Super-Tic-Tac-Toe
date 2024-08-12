from copy import deepcopy
from itertools import cycle, chain
import os

SIZE = 3
WIDTH = 2 * 3**2 + 1
base_matrix = [[" "] * SIZE for _ in range(SIZE)]
field = [deepcopy(base_matrix) for _ in range(SIZE * SIZE)]
winner_ceil = [[" "] * SIZE for _ in range(SIZE)]

CROSS, CIRCLE = f"\x1b[38;5;27mX\x1b[0m", f"\x1b[38;5;9mO\x1b[0m"
big_cross = ["\\   /", "  X  ", "/   \\"]
big_circle = ["/ ‾ \\", "|   |", "\\ _ /"]

it_hoz = zip((x for x in range(SIZE) for _ in range(SIZE)), cycle(range(SIZE)))
it_vert = zip(cycle(range(SIZE)), (x for x in range(SIZE) for _ in range(SIZE)))
it_diag = zip(cycle(range(SIZE)), chain(range(SIZE), range(SIZE - 1, -1, -1)))
horizontal = zip(it_hoz, it_hoz, it_hoz)
vertical = zip(it_vert, it_vert, it_vert)
diagonal = zip(it_diag, it_diag, it_diag)
combinations = list((*horizontal, *vertical, *diagonal))


def print_field():
    print("-" * WIDTH)
    for i in range(0, SIZE * SIZE, SIZE):
        for j in range(SIZE):
            total_row = "|"
            for k in range(SIZE):
                ceil = winner_ceil[(i + k) // SIZE][(i + k) % SIZE]
                if matrix_idx != i + k and ceil != " ":
                    cross_row = f"\x1b[38;5;27m{big_cross[j]}\x1b[0m"
                    circle_row = f"\x1b[38;5;9m{big_circle[j]}\x1b[0m"
                    idx = (0, 1)[ceil.find('O') != -1]
                    total_row += (cross_row, circle_row)[idx] + "|"
                else:
                    total_row += " ".join(field[i + k][j]) + "|"
            print(total_row)
        print("-" * WIDTH)


def check_combinations(matrix):
    for case in combinations:
        p1, p2, p3 = case
        x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
        if matrix[x1][y1] == matrix[x2][y2] == matrix[x3][y3] and matrix[x1][y1] != " ":
            return matrix[x1][y1]
    return " "


matrix_idx, step, empty_ceils = 0, 0, SIZE**4
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
            if winner_ceil[matrix_idx // SIZE][matrix_idx % SIZE] == " ":
                cur_winner = check_combinations(field[matrix_idx])
                winner_ceil[matrix_idx // SIZE][matrix_idx % SIZE] = cur_winner
            step = (step + 1) % 2
            matrix_idx = x * SIZE + y
            empty_ceils -= 1
    except ValueError:
        print("Incorrect input")
    except IndexError:
        print(f"Incorrect input coords ({x}; {y})")

    winner = check_combinations(winner_ceil)
    print_field()
    if winner != " ":
        print(f"Winner - {winner}")
        break
    if not empty_ceils:
        print("Draw!")
        break
