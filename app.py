from flask import Flask, render_template, request, redirect, url_for
from src.game import Game
from src.board import Board


app = Flask(__name__)

# Initialise game board and current player
game = Game()
board = Board(3, 3)

# NOTE: you cannot use this answer in Portfolio Part 2

@app.route('/')
def index():
    winner = board.check_winner(game.CurrentPlayer, None)
    draw = board.check_draw()
    current_player = game.CurrentPlayer
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()

    board.get_move(game.CurrentPlayer, cell)
    if not board.check_winner(game.CurrentPlayer, cell):
        game.CurrentPlayer = 'O' if game.CurrentPlayer == 'X' else 'X'
    return redirect(url_for('index'))



@app.route('/reset')
def reset():

    board.reset_board()
    game.CurrentPlayer = 'X'
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
