import unittest
from unittest.mock import patch
from io import StringIO
from text_adventure import Room, Player, Game

class TestAdventureGame(unittest.TestCase):
    def setUp(self):
        # Create rooms
        rooms_data = {
            "start": {"description": "You are in the start room. There are exits to the north and east.", "exits": {"north": "hallway", "east": "kitchen"}, "items": ["key", "mirror"]},
            "hallway": {"description": "You are in the hallway room. There's an exit to the south.", "exits": {"south": "start"}, "items": ["torch", "bed", "comb"]},
            "kitchen": {"description": "You are in the kitchen room. There's an exit to the west.", "exits": {"west": "start"}, "items": ["knife", "fruit", "nuts"]}
        }

        self.rooms = {name: Room(name, **data) for name, data in rooms_data.items()}
        self.game = Game()

        for room in self.rooms.values():
            self.game.add_room(room)

    @patch('builtins.input', side_effect=['go north', 'go east', 'take key', 'take chair', 'use key', 'use chair', 'go west', 'help', 'quit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game(self, mock_stdout, mock_input):
        self.game.start_game()
        output = mock_stdout.getvalue()
        expected_output = [
            "Current Room: start",
            "Welcome to the adventure game!",
            "Type 'help' for instructions.",
            "Description: You are in the start room. There are exits to the north and east.",
            "Exits: north, east",
            "What would you like to do? ",
            "Current Room: hallway",
            "Description: You are in the hallway room. There's an exit to the south.",
            "Exits: south",
            "What would you like to do? ",
            "Current Room: kitchen",
            "Description: You are in the kitchen room. There's an exit to the west.",
            "Exits: west",
            "What would you like to do? ",
            "You picked up the key",
            "Current Room: start",
            "Description: You are in the start room. There are exits to the north and east.",
            "Exits: north, east",
            "What would you like to do? ",
            "There is no chair here.",
            "Current Room: start",
            "Description: You are in the start room. There are exits to the north and east.",
            "Exits: north, east",
            "What would you like to do? ",
            "You used the key",
            "Current Room: start",
            "Description: You are in the start room. There are exits to the north and east.",
            "Exits: north, east",
            "What would you like to do? ",
            "You don't have a chair",
            "Current Room: start",
            "Description: You are in the start room. There are exits to the north and east.",
            "Exits: north, east",
            "What would you like to do? ",
            "Current Room: kitchen",
            "Description: You are in the kitchen room. There's an exit to the west.",
            "Exits: west",
            "What would you like to do? ",
            "Available commands: go <direction>, take <item>, use <item>, help, quit",
            "Current Room: kitchen",
            "Description: You are in the kitchen room. There's an exit to the west.",
            "Exits: west",
            "What would you like to do? ",
            "Good luck!\n"
        ]
        
        output_lines = output.split('\n')
        expected_output_lines = [line.strip() for line in expected_output]

        for expected_line, actual_line in zip(expected_output_lines, output_lines):
            self.assertEqual(expected_line, actual_line)

if __name__ == '__main__':
    unittest.main()
