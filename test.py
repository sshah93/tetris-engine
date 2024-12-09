# test_sequence.py
from tetris import Tetris


def test_t1_z3_i4():
    tetris = Tetris()
    print("\nTesting T1,Z3,I4 sequence step by step:")

    # # Place Q piece
    # print("\nPlacing Q1:")
    # tetris.place_piece('Q', 1)
    # tetris.debug_print()

    # Place T piece
    print("\nPlacing T1:")
    tetris.place_piece('T', 1)
    tetris.debug_print()
    print("\nPlacing T1:")
    tetris.place_piece('T', 1)
    tetris.debug_print()

    # # Place Z piece
    # print("\nPlacing Q3:")
    # tetris.place_piece('Q', 3)
    # tetris.debug_print()
    #
    # # Place I piece
    # print("\nPlacing I4:")
    # tetris.place_piece('Q', 5)
    # tetris.debug_print()

    # Get final height
    height = tetris.get_height()
    print(f"\nFinal height: {height}")


if __name__ == '__main__':
    test_t1_z3_i4()