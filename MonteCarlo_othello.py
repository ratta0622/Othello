from othello import Othello as Ot
from othello import Stone as St
import random


def MonteCalro(board):  # determine move by Monte Carlo method
    win = {}
    for x, y in board.alljudge(board.turn):
        count = win_count(board, x, y)
        # list of wincount and where put stone at first
        win.update({count: (x, y)})
        max = win.keys()
        return win[max]


def random_play(board):  # random play and return winner
    while board.check_pass():  # loop until game end
        ls = board.alljudge  # where stone can be put
        choice = random.choice.ls  # (x,y)
        put(*(choice), board.turn)
        board.change_turn()
    return board.finish()


def win_count(board, x, y):  # repeat random_play() and count win, (x,y)is where put stone at first
    N = 100
    win = 0
    # vboard and vvboard are virtual boards for repeat random_play()
    vboard = Ot()
    vboard.put(x, y, board.turn)
    for i in xrange(N):
        vvboard.copy(vboard)
        if random_play(vboard) == board.turn:
            win += 1
    return win
