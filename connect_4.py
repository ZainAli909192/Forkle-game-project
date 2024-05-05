import random

class Connect4:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = None
        self.winning_condition = 4

    def print_board(self):
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("+---+---+---+---+---+---+---+")

    def is_valid_move(self, row, column):
        return row >= 0 and row < 6 and column >= 0 and column < 7 and self.board[row][column] == ' '

    def make_move(self, row, column, token):
        self.board[row][column] = token

    def check_winner(self, token):
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col + i] == token for i in range(self.winning_condition)):
                    return True

        # Check vertical
        for row in range(3):
            for col in range(7):
                if all(self.board[row + i][col] == token for i in range(self.winning_condition)):
                    return True

        # Check diagonal (positive slope)
        for row in range(3):
            for col in range(4):
                if all(self.board[row + i][col + i] == token for i in range(self.winning_condition)):
                    return True

        # Check diagonal (negative slope)
        for row in range(3):
            for col in range(3, 7):
                if all(self.board[row + i][col - i] == token for i in range(self.winning_condition)):
                    return True

        return False

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

def player_move(game, player):
    while True:
        try:
            row = int(input(f"{player.name}'s turn ({player.token}): Enter row (1-6): ")) - 1
            column = int(input(f"{player.name}'s turn ({player.token}): Enter column (1-7): ")) - 1
            if game.is_valid_move(row, column):
                game.make_move(row, column, player.token)
                break
            else:
                print("Invalid move! Please choose an empty cell.")
        except ValueError:
            print("Invalid input! Please enter numbers.")

def cpu_move(game, player):
    print(f"{player.name}'s turn ({player.token}):")
    while True:
        row = random.randint(0, 5)
        column = random.randint(0, 6)
        if game.is_valid_move(row, column):
            game.make_move(row, column, player.token)
            break

def start_game():
    print("Welcome to Connect 4!")
    while True:
        try:
            num_players = int(input("Enter number of players (1 or 2): "))
            if num_players == 1 or num_players == 2:
                break
            else:
                print("Invalid number of players! Please enter 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    game = Connect4()

    player1_name = input("Enter Player 1's name: ")
    player1_token = input("Enter Player 1's token (X or O): ").upper()
    while player1_token not in ['X', 'O']:
        player1_token = input("Invalid token! Please enter X or O: ").upper()
    player1 = Player(player1_name, player1_token)

    player2_token = 'X' if player1_token == 'O' else 'O'
    if num_players == 1:
        player2_name = "CPU"
    else:
        player2_name = input("Enter Player 2's name: ")
    player2 = Player(player2_name, player2_token)

    print(f"{player2.name}'s token is {player2.token}")

    game.current_player = player1

    while True:
        print("\n" + "  ".join(str(i) for i in range(1, 8)))
        print("+---+---+---+---+---+---+---+")
        game.print_board()
        if game.current_player == player1:
            player_move(game, player1)
        else:
            cpu_move(game, player2) if num_players == 1 else player_move(game, player2)

        if game.check_winner(game.current_player.token):
            print("\n" + "  ".join(str(i) for i in range(1, 8)))
            print("+---+---+---+---+---+---+---+")
            game.print_board()
            print(f"{game.current_player.name} wins!")
            break

        if all(token != ' ' for row in game.board for token in row):
            print("\n" + "  ".join(str(i) for i in range(1, 8)))
            print("+---+---+---+---+---+---+---+")
            game.print_board()
            print("It's a draw!")
            break

        game.current_player = player2 if game.current_player == player1 else player1

start_game()
