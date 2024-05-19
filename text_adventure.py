import random

class Player:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None

class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items if items else []
        self.used_items = []

    def display_info(self):
        # Define the ASCII art for each room
        room_art = {
            "start": [
                "+-------------------------------------------------------+",
                "|    Start room                                         |",
                "|                                                       |",
                "|   Items:                                              |",
                "|    -" + "\n|   - ".join(self.items).center(17) + "    ",
                "|                                                       |",
                "|   Used Items:                                         |",
                "|    -" + "\n|   - ".join(self.used_items).center(17) +"",
                "|                                                       |",
                "+-------------------------------------------------------+"
            ],
            "hallway": [
                "+------------------------------------------------------+",
                "|   Hallway                                            |",
                "|                                                      |",
                "|   Items:                                             |",
                "|    -" + "\n|   - ".join(self.items).center(17) + "   ",
                "|                                                      |",
                "|   Used Items:                                        |",
                "|    -" + "\n|   - ".join(self.used_items).center(17)+"",
                "|                                                      |",
                "+------------------------------------------------------+"
            ],
            "kitchen": [
                "+-----------------------------------------------------+",
                "|    Kitchen                                          |",
                "|                                                     |",
                "|   Items:                                            |",
                "|    -" + "\n|   - ".join(self.items).center(17) + "  ",
                "|                                                     |",
                "|   Used Items:                                       |",
                "|    -" + "\n|   - ".join(self.used_items).center(17) +"",
                "|                                                     |",
                "+------------------------------------------------------+"
            ]
        }

        # Print the room's ASCII art
        print("\n".join(room_art[self.name]))

        # Print room description and exits
        print("Description:", self.description)
        print("Exits:", ", ".join(self.exits.keys()))



class Game:
    def __init__(self):
        self.player = Player()
        self.current_room = None
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def start_game(self):
        self.current_room = random.choice(list(self.rooms.values()))
        self.play()

    def display_current_room(self):
        print("\nCurrent Room:", self.current_room)
        self.current_room.display_info()

    # Impure function: Changes the current room and prints output
    def move(self, direction):
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            if next_room_name in self.rooms:
                self.current_room = self.rooms[next_room_name]
                self.display_current_room()  # Update display
            else:
                print("There is no room in that direction.")
        else:
            print("You cannot go in that direction.")

    # Impure function: Changes the current room and prints output
    def take_item(self, item_name):
        if item_name in self.current_room.items:
            item = self.current_room.items.remove(item_name)
            self.player.add_item(item)
            print("You picked up the", item_name)
            self.display_current_room()  # Update display
        else:
            print("There is no", item_name, "here.")

    # Impure function: Changes the current room and prints output
    def use_item(self, item_name):
        if item_name in self.player.inventory:
            print("You used the", item_name)
            self.current_room.used_items.append(item_name)  # Add the used item to used_items list
        elif item_name in self.current_room.items:
            print("You used the", item_name)
            self.current_room.used_items.append(item_name)  # Add the used item to used_items list
        else:
            print("You don't have a", item_name)
        self.display_current_room()  # Update display

    # Impure function: Prints output and handles user input
    def play(self):
        print("Welcome to the adventure game!")
        print("Type 'help' for instructions.")
        self.display_current_room()  # Initial display

        while True:
            command = input("What would you like to do? ").strip().lower().split()

            if command[0] == 'go' and len(command) > 1:
                self.move(command[1])
            elif command[0] == 'take' and len(command) > 1:
                self.take_item(command[1])
            elif command[0] == 'use' and len(command) > 1:
                self.use_item(command[1])
            elif command[0] == 'help':
                print("Available commands: go <direction>, take <item>, use <item>, help, quit")
            elif command[0] == 'quit':
                print("Good luck!")
                break  # Stop the game
            else:
                print("Invalid command. Type 'help' for instructions.")

# Create rooms
rooms_data = {
    "start": {"description": "You are in the start room. There are exits to the north and east.", "exits": {"north": "hallway", "east": "kitchen"}, "items": ["key", "mirror"]},
    "hallway": {"description": "You are in the hallway room. There's an exit to the south.", "exits": {"south": "start"}, "items": ["torch", "bed", "comb"]},
    "kitchen": {"description": "You are in the kitchen room. There's an exit to the west.", "exits": {"west": "start"}, "items": ["knife", "fruit", "nuts"]}
}

rooms = {name: Room(name, **data) for name, data in rooms_data.items()}

# Start the game
game = Game()
for room in rooms.values():
    game.add_room(room)

game.start_game()
