from unittest import TestCase

from pandas import np

from games.tictactoe.board import Board


class TestBoard(TestCase):
    def test_get_position_by_index(self):
        board = Board()

        for i in range(board.size):
            x, y = board.get_position_by_index(i)
            index = board.get_index_by_position(x, y)
            self.assertEqual(i, index)

    def test_hash(self):
        b1 = Board()
        b2 = Board()
        self.assertEqual(b1, b2)

        b1.set_value(x=1, y=1, value=1)
        self.assertNotEqual(b1, b2)

    def test_check_winner_1(self):
        board = Board()
        self.assertEqual(board.check_winner(), 0)

        for y in range(3):
            board.set_value(x=y, y=1, value=1)

        self.assertEqual(board.check_winner(), 1)
        board.clear()
        self.assertEqual(board.check_winner(), 0)

        for y in range(3):
            board.set_value(x=1, y=y, value=1)
        self.assertEqual(board.check_winner(), 1)

        board.clear()
        for x in range(3):
            board.set_value(x=x, y=x, value=1)
        self.assertEqual(board.check_winner(), 1)

        board.clear()
        for x in range(3):
            board.set_value(x=2 - x, y=x, value=1)
        self.assertEqual(board.check_winner(), 1)

    def test_check_winner_2(self):
        b = Board()
        b.board = np.array([1, 2, 1, 2, 1, 2, 1, 2, 1])
        self.assertEqual(b.check_winner(), 1)

        b.board = np.array([1, 1, 0, 1, 2, 0, 1, 2, 2])
        self.assertEqual(b.check_winner(), 1)

    def test_indices(self):
        a = np.array([0, 2, 5, 9, 0])
        i = np.where(a == 0)
        self.assertEqual(2, len(i[0]))
