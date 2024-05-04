import unittest
from unittest.mock import patch
from io import StringIO
from frakle import FarklePlayer, FarkleGame, getPlayerNameInput, checkPlayerName, getPlayerMenuInput

class TestFarkleGame(unittest.TestCase):
    def test_getPlayerNameInput_valid(self):
        with patch('builtins.input', side_effect=['Alice']):
            name = getPlayerNameInput()
            self.assertEqual(name, 'Alice')

    def test_getPlayerNameInput_invalid(self):
        with patch('builtins.input', side_effect=['123', 'Alice']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                name = getPlayerNameInput()
                self.assertEqual(name, 'Alice')
                self.assertEqual(fake_out.getvalue().strip(), "Invalid name. Please enter only alphabetical characters.")

    def test_checkPlayerName(self):
        self.assertFalse(checkPlayerName('Alice'))

    def test_getPlayerMenuInput_roll(self):
        with patch('builtins.input', side_effect=['r']):
            choice = getPlayerMenuInput()
            self.assertEqual(choice, 'r')

    def test_getPlayerMenuInput_end(self):
        with patch('builtins.input', side_effect=['e']):
            choice = getPlayerMenuInput()
            self.assertEqual(choice, 'e')

    def test_game_play(self):
        with patch('builtins.input', side_effect=['1', 'Alice', 'r', 'e']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                game = FarkleGame(winning_score=10000)
                game.play_game()
                output = fake_out.getvalue()
                self.assertIn("Welcome to Farkle!", output)
                self.assertIn("Alice's turn", output)
                self.assertIn("Total score:", output)
                self.assertIn("Dice:", output)
                self.assertIn("Farkle! No scoring combinations.", output)
                self.assertIn("Turn ended. Total score for this turn:", output)
                self.assertIn("wins with", output)
                self.assertIn("Game over. Thanks for playing!", output)

if __name__ == '__main__':
    unittest.main()
