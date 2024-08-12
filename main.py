import os
from copy import deepcopy
from utils import it_step, SIZE, INDENT, COMBINATIONS, CIRCLE, print, greeting, Color

BIG_CROSS = [f"{Color.BLUE}{s}{Color.END}" for s in ["\\   /", "  X  ", "/   \\"]]
BIG_CIRCLE = [f"{Color.RED}{s}{Color.END}" for s in ["/ ‾ \\", "|   |", "\\ _ /"]]
FIELD = [deepcopy([[" "] * SIZE for _ in range(SIZE)]) for _ in range(SIZE * SIZE)]
WINNER_CEIL = [[" "] * SIZE for _ in range(SIZE)]


def build_row(i, j, matrix_idx):
    total_row = "|"
    for k in range(SIZE):
        ceil = WINNER_CEIL[(i + k) // SIZE][(i + k) % SIZE]
        if matrix_idx != i + k and ceil != " ":
            total_row += (BIG_CROSS[j], BIG_CIRCLE[j])[ceil == CIRCLE] + "|"
        else:
            cur_row = f"{' '.join(FIELD[i + k][j])}{Color.END}"
            if matrix_idx == i + k:
                cur_row = f"{Color.WHITE}{cur_row}"
            total_row += cur_row + "|"
    return total_row


def print_game_field(step, matrix_idx):
    print(INDENT)
    for i in range(0, SIZE * SIZE, SIZE):
        for j in range(SIZE):
            print(build_row(i, j, matrix_idx))
        print(INDENT)
    print(f"\nCur step: {step}")


def check_combinations(data):
    for case in COMBINATIONS:
        p1, p2, p3 = case
        x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
        if data[x1][y1] == data[x2][y2] == data[x3][y3] and data[x1][y1] != " ":
            return data[x1][y1]
    return " "


def main():
    cur_step, empty_ceils = next(it_step), SIZE**4
    cur_matrix = greeting()
    print_game_field(cur_step, cur_matrix)

    while True:
        if not empty_ceils:
            print("Draw! =)")
            break
        info = input("> ")
        if info.lower() == "stop":
            break
        os.system("cls" if os.name == "posix" else "clear")

        try:
            x, y = map(int, info.split())
            if FIELD[cur_matrix][x][y] != " ":
                print(f"> Ceil ({x}; {y}) already matched!")
            else:
                FIELD[cur_matrix][x][y] = cur_step
                if WINNER_CEIL[cur_matrix // SIZE][cur_matrix % SIZE] == " ":
                    cur_winner = check_combinations(FIELD[cur_matrix])
                    WINNER_CEIL[cur_matrix // SIZE][cur_matrix % SIZE] = cur_winner
                cur_step = next(it_step)
                cur_matrix = x * SIZE + y
                empty_ceils -= 1
        except ValueError:
            print("> Incorrect input!")
        except IndexError:
            print(f"> Incorrect coords ({x}; {y})!")

        winner = check_combinations(WINNER_CEIL)
        print_game_field(cur_step, cur_matrix)
        if winner != " ":
            print(f"Winner is '{winner}'! =)")
            break
