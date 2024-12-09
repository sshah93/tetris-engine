
import sys

class TetrisEngine:
    def __init__(self, width=10, height=100):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.shapes = {
            "Q": [(0, 0), (0, 1), (1, 0), (1, 1)],
            "Z": [(0, 0), (0, 1), (1, 1), (1, 2)],
            "S": [(0, 1), (0, 2), (1, 0), (1, 1)],
            "T": [(0, 0), (0, 1), (0, 2), (1, 1)],
            "I": [(0, 0), (1, 0), (2, 0), (3, 0)],
            "L": [(0, 0), (1, 0), (2, 0), (2, 1)],
            "J": [(0, 1), (1, 1), (2, 1), (2, 0)],
        }

    def place_piece(self, piece, column):
        shape = self.shapes[piece]
        max_row = self.height - 1

        while max_row >= 0:
            if all(0 <= column + x < self.width and self.grid[max_row + y][column + x] == 0 for x, y in shape):
                for x, y in shape:
                    self.grid[max_row + y][column + x] = 1
                self.clear_full_rows()
                return
            max_row -= 1

    def clear_full_rows(self):
        self.grid = [row for row in self.grid if not all(row)]
        while len(self.grid) < self.height:
            self.grid.insert(0, [0 for _ in range(self.width)])

    def get_height(self):
        for i, row in enumerate(self.grid):
            if any(row):
                return self.height - i
        return 0

    def process_input_line(self, line):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        instructions = line.strip().split(",")
        for instruction in instructions:
            piece, column = instruction[0], int(instruction[1])
            self.place_piece(piece, column)
        return self.get_height()

def main():
    engine = TetrisEngine()
    results = []
    for line in sys.stdin:
        results.append(engine.process_input_line(line))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
