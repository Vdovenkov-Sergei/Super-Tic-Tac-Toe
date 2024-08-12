from itertools import cycle, chain

old_print = print


class Color:
    RED = "\x1b[38;5;9m"
    BLUE = "\x1b[38;5;27m"
    WHITE = "\x1b[47m"
    END = "\x1b[0m"


def print(*args, sep=" ", end="\n"):
    old_print(*args, sep=sep, end=f"{Color.END}{end}")


SIZE = 3
INDENT = "-" * (2 * SIZE**2 + 1)
CROSS, CIRCLE = f"{Color.BLUE}X", f"{Color.RED}O"

it_hoz = zip((x for x in range(SIZE) for _ in range(SIZE)), cycle(range(SIZE)))
it_vert = zip(cycle(range(SIZE)), (x for x in range(SIZE) for _ in range(SIZE)))
it_diag = zip(cycle(range(SIZE)), chain(range(SIZE), range(SIZE - 1, -1, -1)))
it_step = cycle([CROSS, CIRCLE])
COMBINATIONS = list(
    (
        *zip(it_hoz, it_hoz, it_hoz),
        *zip(it_vert, it_vert, it_vert),
        *zip(it_diag, it_diag, it_diag),
    )
)
