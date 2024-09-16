class Board:
    def __init__(self, rows, cols):
        self.Rows = rows
        self.Columns = cols
        self.Grid = self.create_grid()

    def create_grid(self):
        """
                Creates a 2D grid (list of lists) with the dimensions specified by the
                `Rows` and `Columns` attributes. Each cell in the grid is initialized
                with a space character (' ').

                Returns:
                    list: A 2D list representing the grid, where each cell is initialized
                          with a space character (' ').
        """
        grid = []
        for i in range(self.Rows):
            row = []
            for j in range(self.Columns):
                row.append(' ')
            grid.append(row)
        return grid

    def get_move(self, player, move):
        """
                Updates the board with the player's move.

                This method places the player's symbol at the specified position on the board
                if the position is valid and currently unoccupied.

                Args:
                    player (str): The symbol representing the player (e.g., 'x' or 'o').
                    move (int): The position on the board where the player wants to place their symbol.
                                The position is treated as a single integer representing the cell index
                                in a flattened version of the 2D grid (row-major order).

                Returns:
                    None
                """
        grid_position = -1
        for i in range(self.Rows):
            for j in range(self.Columns):
                grid_position += 1
                if grid_position == move and self.Grid[i][j] == ' ':
                    self.Grid[i][j] = player

    def convert_list(self):
        """
                Converts the 2D grid into a 1D list.

                This method flattens the 2D grid (list of lists) into a single 1D list,
                preserving the row-major order of the elements.

                Returns:
                    list: A 1D list containing all the elements of the 2D grid in row-major order.
                """
        one_d_list = []
        for i in range(self.Rows):
            for j in range(self.Columns):
                one_d_list.append(self.Grid[i][j])
        return one_d_list

    def get_x_and_y(self, move):
        """
                Converts a move index to its corresponding row and column indices in the grid.

                This method takes a move index, which represents a cell in a flattened version
                of the 2D grid (row-major order), and converts it to the corresponding row and
                column indices in the 2D grid.

                Args:
                    move (int): The position on the board where the player wants to place their symbol.
                                The position is treated as a single integer representing the cell index
                                in a flattened version of the 2D grid (row-major order).

                Returns:
                    tuple: A tuple (i, j) where 'i' is the row index and 'j' is the column index
                           corresponding to the given move index.
                """
        grid_position = -1
        for i in range(self.Rows):
            for j in range(self.Columns):
                grid_position += 1
                if grid_position == move:
                    return i, j

    def check_winner(self, current_player, move):
        """
            Checks if the current player has won the game after making a move.

            This method checks for a win condition by examining the rows, columns, and diagonals
            affected by the latest move. It returns the symbol of the winning player if a win
            condition is met, otherwise it returns None.

            Args:
                current_player (str): The symbol representing the current player (e.g., 'x' or 'o').
                move (int): The position on the board where the player has placed their symbol.
                            The position is treated as a single integer representing the cell index
                            in a flattened version of the 2D grid (row-major order).

            Returns:
                str or None: The symbol of the winning player if a win condition is met, otherwise None.
            """
        # Check for win by only checking through the rows and columns affected by the latest move
        if move is None:
            return None

        winner = None

        latest_move_y, latest_move_x = self.get_x_and_y(move)

        # check horizontal
        for column in range(self.Rows): # cycle through each column in the row
            if self.Grid[latest_move_y][column] != current_player:
                # if the column in the row isn't the player that just made a move, break
                break
            if column == self.Rows - 1:
                # if it just checked the last column and didn't find a fault, set the winner and return
                winner = current_player
                return winner

        # check columns
        for row in range(self.Columns):
            if self.Grid[row][latest_move_x] != current_player:
                break
            if row == self.Columns - 1:
                winner = current_player
                return winner

        # check diagonal
        if latest_move_y == latest_move_y:  # checks whether we're on the first diagonal
            for i in range(self.Rows):
                if self.Grid[i][i] != current_player:
                    break
                if i == self.Rows - 1:
                    winner = current_player
                    return winner

        # check opposite diagonal
        if latest_move_x + latest_move_y == self.Rows - 1:
            for i in range(self.Rows):
                if self.Grid[i][(self.Rows-1)-i] != current_player:
                    break
                if i == self.Rows-1:
                    winner = current_player
                    return winner

        return winner

    def check_draw(self):
        """
                Checks if the game has ended in a draw.

                This method determines if the game is a draw by checking if there are no empty cells
                (represented by a space character ' ') left in the grid. If there are no empty cells,
                it means all positions on the board are occupied and no player has won, resulting in a draw.

                Returns:
                    bool: True if the game is a draw (no empty cells left), False otherwise.
                """
        return ' ' not in self.Grid

    def reset_board(self):
        self.Grid = self.create_grid()

if __name__ == '__main__':
    board = Board(3, 3)

    board.get_move('x', 6)
    board.get_move('x', 4)
    board.get_move('x', 2)

    for row in board.Grid:
        print(row)

    print(board.check_winner('x', 2))
