
# Task 6.1: Create a custom exception
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


# Task 6.2: Create the Board class
class Board:
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.turn = "X"

    # Task 6.3: Display the board
    def __str__(self):
        lines = []
        lines.append(
            f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n"
        )
        return "".join(lines)

    # Task 6.4: Make a move
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    # Task 6.5: Check whether the game is over
    def whats_next(self):
        # Check rows
        for i in range(3):
            if (
                self.board_array[i][0] != " "
                and self.board_array[i][0]
                == self.board_array[i][1]
                == self.board_array[i][2]
            ):
                winner = self.board_array[i][0]
                return (True, f"{winner} wins!")

        # Check columns
        for i in range(3):
            if (
                self.board_array[0][i] != " "
                and self.board_array[0][i]
                == self.board_array[1][i]
                == self.board_array[2][i]
            ):
                winner = self.board_array[0][i]
                return (True, f"{winner} wins!")

        # Check diagonals
        if (
            self.board_array[1][1] != " "
            and self.board_array[0][0]
            == self.board_array[1][1]
            == self.board_array[2][2]
        ):
            winner = self.board_array[1][1]
            return (True, f"{winner} wins!")

        if (
            self.board_array[1][1] != " "
            and self.board_array[0][2]
            == self.board_array[1][1]
            == self.board_array[2][0]
        ):
            winner = self.board_array[1][1]
            return (True, f"{winner} wins!")

        # Check whether the board is full
        for row in self.board_array:
            if " " in row:
                return (False, f"{self.turn}'s turn.")

        # The board is full and nobody has won
        return (True, "Cat's Game.")


# Task 6.6: Play the game
if __name__ == "__main__":
    board = Board()

    print("Welcome to Tic-Tac-Toe!")
    print("Enter moves such as 'upper left', 'center', or 'lower right'.")
    print()

    while True:
        print(board)

        game_over, message = board.whats_next()

        if game_over:
            print(message)
            break

        print(message)
        move_string = input("Enter your move: ").strip().lower()

        try:
            board.move(move_string)
        except TictactoeException as error:
            print(error.message)
            print("Please try again.")
