import random

class DecodingBoard:
    def __init__(self, num_guesses):
        self.num_guesses = num_guesses
        self.rows = [[] for _ in range(num_guesses)]
        self.key_pegs = [[] for _ in range(num_guesses)]

    def display_board(self):
        for i, (row, key_pegs) in enumerate(zip(self.rows, self.key_pegs)):
            if row:
                row_str = " ".join(row)
                feedback_str = " ".join(key_pegs)
            else:
                row_str = "Guess: "
                feedback_str = ""
            print(f"{row_str:<10}Feedback: {feedback_str:<10}")
        print()

    def make_guess(self, guess):
        if len(self.rows[0]) == 0:
            self.rows[0] = guess
            return True
        else:
            for i in range(1, self.num_guesses):
                if len(self.rows[i]) == 0:
                    self.rows[i] = guess
                    return True
        return False

    def provide_feedback(self, secret_code):
        for i, guess in enumerate(self.rows):
            if not guess:
                self.key_pegs[i] = ["-"] * 4
                continue
            feedback = self._calculate_feedback(guess, secret_code)
            self.key_pegs[i] = feedback

    def _calculate_feedback(self, guess, secret_code):
        feedback = []
        checked = [False] * len(secret_code)
        for i in range(len(guess)):
            if guess[i] == secret_code[i]:
                feedback.append("Correct")  # Correct digit and position
                checked[i] = True
            elif guess[i] > secret_code[i]:
                feedback.append("Higher")  # Guess is greater than secret
            else:
                feedback.append("Lower")  # Guess is lower than secret
        return feedback


class Player:
    def __init__(self, name):
        self.name = name

    def make_secret_code(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def make_guess(self):
        raise NotImplementedError("Subclass must implement abstract method")

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_secret_code(self):
        print(f"{self.name}, choose a secret four-digit code.")
        secret_code = input("Enter your secret code (4 digits): ")
        # Validate input
        while not self.validate_secret_code(secret_code):
            print("Invalid code! Please enter a valid four-digit code.")
            secret_code = input("Enter your secret code (4 digits): ")
        return secret_code

    def make_guess(self):
        print(f"{self.name}, make your guess:")
        guess = input("Enter your guess (4 digits): ")
        # Validate input
        while not self.validate_guess(guess):
            print("Invalid guess! Please enter a valid four-digit guess.")
            guess = input("Enter your guess (4 digits): ")
        return guess

    def validate_secret_code(self, code):
        # Validate the secret code
        return code.isdigit() and len(code) == 4

    def validate_guess(self, guess):
        # Validate the guess
        return guess.isdigit() and len(guess) == 4

class CPUPlayer(Player):
    def __init__(self, level):
        super().__init__("CPU")
        self.level = level
        self.predefined_codes = {
            1: ["1234", "5678", "4321", "8765"],
            2: ["1111", "2222", "3333", "4444"],
            3: ["9876", "5432", "6789", "1234"]
        }

    def make_secret_code(self):
        print("CPU has chosen a secret four-digit code.")
        numb=self.predefined_codes[self.level][random.randint(0, 3)]
        # print(numb)
        return numb

    def make_guess(self):
        guess = "".join(str(random.randint(0, 9)) for _ in range(4))
        print("CPU's guess:", guess)
        return guess

class MastermindGame:
    def __init__(self, num_guesses=8):
        self.num_guesses = num_guesses

    def setup_game(self):
        print("Welcome to Mastermind!")
        print("Choose your game mode:")
        print("1. Single player (against CPU with random codes)")
        print("2. Single player (against CPU with predefined codes)")
        print("3. Two players")
        mode = input("Enter your choice (1, 2 or 3): ")
        while mode not in ("1", "2", "3"):
            print("Invalid choice! Please enter 1, 2 or 3.")
            mode = input("Enter your choice (1, 2 or 3): ")

        if mode == "1":
            self.code_maker = CPUPlayer(1)
            self.code_breaker = HumanPlayer("Player")
        elif mode == "2":
            print("Choose the level of difficulty:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            level = input("Enter your choice (1, 2 or 3): ")
            while level not in ("1", "2", "3"):
                print("Invalid choice! Please enter 1, 2 or 3.")
                level = input("Enter your choice (1, 2 or 3): ")
            self.code_maker = CPUPlayer(int(level))
            self.code_breaker = HumanPlayer("Player")
        else:
            self.code_maker = HumanPlayer("Codemaker")
            self.code_breaker = HumanPlayer("Codebreaker")

        self.decoding_board = DecodingBoard(self.num_guesses)

    def play_game(self):
        print("Setting up the game...")
        secret_code = self.code_maker.make_secret_code()
        print("Secret code set!")
        for _ in range(self.num_guesses):
            guess = self.code_breaker.make_guess()
            if not self.decoding_board.make_guess(guess):
                print("Decoding board is full. Game over!")
                break
            self.decoding_board.provide_feedback(secret_code)
            self.decoding_board.display_board()
            if guess == secret_code:
                print("Congratulations! You guessed the code.")
                break
        else:
            print("Out of guesses! The code was:", secret_code)

def main():
    game = MastermindGame()
    game.setup_game()
    game.play_game()

if __name__ == "__main__":
    main()
