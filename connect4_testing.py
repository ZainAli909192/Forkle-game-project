import unittest
from unittest.mock import patch
from io import StringIO
from connect_4 import Connect4, Player, player_move, cpu_move, start_game

class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_is_valid_move(self):
        self.assertTrue(self.game.is_valid_move(0, 0))
        self.assertTrue(self.game.is_valid_move(5, 6))
        self.assertFalse(self.game.is_valid_move(-1, 0))
        self.assertFalse(self.game.is_valid_move(0, 7))

    def test_make_move(self):
        self.game.make_move(0, 0, 'X')
        self.assertEqual(self.game.board[0][0], 'X')

    def test_check_winner(self):
        # Test horizontal win
        for i in range(3):
            self.game.make_move(0, i, 'X')
        self.assertTrue(self.game.check_winner('X'))

        # Test vertical win
        for i in range(3):
            self.game.make_move(i, 0, 'O')
        self.assertTrue(self.game.check_winner('O'))

    @patch('builtins.input', side_effect=['1', '1', '1', '2', '2', '1', '3', '2', '3', '2', '4', '2', '4', '3', '5', '3', '5', '3', '6', '4', '4', '4', '6', '4', '5', '5', '6', '5', '6', '5', '6'])
    def test_player_move(self, mock_input):
        player = Player("Player", 'X')
        player_move(self.game, player)
        self.assertEqual(self.game.board[0][0], 'X')

    @patch('random.randint', side_effect=[0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5])
    def test_cpu_move(self, mock_randint):
        player = Player("CPU", 'O')
        cpu_move(self.game, player)
        self.assertEqual(self.game.board[0][0], 'O')

    @patch('builtins.input', side_effect=['2', 'Player1', 'X', '2', 'Player2', 'O'])
    def test_start_game(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            start_game()
            output = fake_out.getvalue().strip()
            self.assertIn("Player2's token is O", output)

if __name__ == '__main__':
    unittest.main()
