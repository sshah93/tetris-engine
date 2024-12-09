# Tetris

This project implements a Tetris engine that models a grid that pieces enter from top and come to rest at the bottom, as if pulled down by gravity. Each piece is made up of four unit squares. No two unit squares occupy the same space in the grid at the same time. The pieces are rigid, and come to rest as soon as any part of a piece contacts the bottom of the grid or any resting block. As in Tetris, whenever an entire row of the grid is filled, it disappears, and any higher rows drop into the vacated space without any change to the internal pattern of blocks in any row.

## Features

- Processes shapes of Tetris pieces denoted by letters Q, Z, S, T, I, L, and J from the provided exercise file
- Handles row clearing when lines are completed
- Maintains correct block stacking and gravity rules
- Processes input from stdin and writes results to stdout

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Usage

### Command Line

The program reads from stdin and writes to stdout:

```bash
./tetris.py < input.txt > output.txt
```

Or you can run it directly with Python:

```bash
python tetris.py < input.txt > output.txt
```

### Input Format

Each line of the input should contain a comma-separated sequence of pieces. Each piece is represented by:
- A letter (Q, Z, S, T, I, L, or J) indicating the piece type
- A single digit (0-9) indicating the leftmost column position

Example input:
```
Q0
I0,I4,Q8
T1,Z3,I4
```

### Output Format

The program outputs one number per line, representing the final height of blocks for each input sequence:
```
2
1
4
```

## Testing

Run the test script using:

```bash
python test_tetris.py
```

## Notes

- The grid is 10 units wide (columns 0-9)
- Maximum height is set to 100 units
- Pieces cannot rotate
- Rows are cleared immediately when filled
- Empty input sequences return height 0
- Invalid inputs are gracefully handled