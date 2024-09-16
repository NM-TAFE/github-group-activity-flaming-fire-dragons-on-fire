class Board:
    def __init__(self, rows, cols):
        self.Rows = rows
        self.Columns = cols
        self.Grid = self.create_grid()

    def create_grid(self):
        grid = []
        for i in range(self.Rows):
            row = []
            for j in range(self.Columns):
                row.append(' ')
            grid.append(row)
        return grid

    def get_move(self, player, move):
        grid_position = -1
        for i in range(self.Rows):
            for j in range(self.Columns):
                grid_position += 1
                if grid_position == move and self.Grid[i][j] == ' ':
                    self.Grid[i][j] = player

    def convert_list(self):
        one_d_list = []
        for i in range(self.Rows):
            for j in range(self.Columns):
                one_d_list.append(self.Grid[i][j])
        return one_d_list

    def get_x_and_y(self, move):
        grid_position = -1
        for i in range(self.Rows):
            for j in range(self.Columns):
                grid_position += 1
                if grid_position == move:
                    return i, j

    def check_winner(self, current_player, move):
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
