import unittest
from unittest.mock import patch
from mastermind import HumanPlayer

if __name__ == "__main__":
    unittest.main()

class TestTwoPlayers(unittest.TestCase):
    def test_make_secret_code(self):
        player1 = HumanPlayer("Player 1")
        player2 = HumanPlayer("Player 2")
        
        # Player 1's secret code
        with patch('builtins.input', side_effect=["1234"]):
            secret_code = player1.make_secret_code()
        self.assertEqual(secret_code, "1234")
        
        # Player 2's secret code
        with patch('builtins.input', side_effect=["5678"]):
            secret_code = player2.make_secret_code()
        self.assertEqual(secret_code, "5678")

    def test_make_guess(self):
        player1 = HumanPlayer("Player 1")
        player2 = HumanPlayer("Player 2")
        
        # Player 1's guess
        with patch('builtins.input', side_effect=["2345"]):
            guess = player1.make_guess()
        self.assertEqual(guess, "2345")
        
        # Player 2's guess
        with patch('builtins.input', side_effect=["6789"]):
            guess = player2.make_guess()
        self.assertEqual(guess, "6789")

