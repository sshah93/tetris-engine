import sys

SHAPES = {
    "Q": [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
    "Z": [(1, 0), (2, 0), (0, 1), (1, 1)],  # Z-shape
    "S": [(1, 0), (2, 0), (0, 1), (1, 1)],  # S-shape
    "T": [(1, 0), (0, 1), (1, 1), (2, 1)],  # T-shape
    "I": [(0, 0), (1, 0), (2, 0), (3, 0)],  # I-shape
    "L": [(0, 0), (0, 1), (0, 2), (1, 2)],  # L-shape
    "J": [(1, 0), (1, 1), (1, 2), (0, 2)],  # J-shape
}

MAX_WIDTH = 10
MAX_HEIGHT = 100


def simulate_tetris(lines):
    results = []

    for line in lines:
        grid = [[0] * MAX_WIDTH for _ in range(MAX_HEIGHT)]

        for piece in line.split(","):
            shape, col = piece[0], int(piece[1])
            positions = [(x + col, y) for x, y in SHAPES[shape]]

            # Debug: Display current piece and intended positions
            # print(f"Placing piece {piece}: {positions}")

            # ensure the piece fits horizontally in the grid
            if any(x >= MAX_WIDTH for x, _ in positions):
                raise ValueError(f"Piece {piece} exceeds grid width at column {col}.")

            # find the lowest valid position for the piece
            drop_heights = []
            for x, y in positions:
                height = 0
                while height < MAX_HEIGHT - y - 1 and grid[y + height + 1][x] == 0:
                    height += 1
                drop_heights.append(height)

            drop_height = min(drop_heights)

            # Debug: Display drop height
            # print(f"Drop height for {piece}: {drop_height}")

            for x, y in positions:
                grid[y + drop_height][x] = 1

            # Debug: Display grid after placing the piece
            # print(f"Grid after placing {piece}:")
            # for row in reversed(grid[-10:]):  # Display bottom 10 rows for clarity
            #     print("".join(["#" if cell else "." for cell in row]))

            # remove filled rows and maintain grid size
            grid = [row for row in grid if not all(row)]
            while len(grid) < MAX_HEIGHT:
                grid.insert(0, [0] * MAX_WIDTH)

            # Debug: Display grid after row clearing
            # print(f"Grid after row clearing {piece}:")
            # for row in reversed(grid[-10:]):
            #     print("".join(["#" if cell else "." for cell in row]))

        height = MAX_HEIGHT - next((y for y, row in enumerate(grid) if any(row)), MAX_HEIGHT)
        # print(f"Final height for line {line}: {height}")
        results.append(str(height))

    return results


if __name__ == "__main__":
    input_lines = sys.stdin.read().strip().split("\n")
    output_lines = simulate_tetris(input_lines)
    sys.stdout.write("\n".join(output_lines) + "\n")
