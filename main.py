from colorama import Fore
from board import Board
from art import logo
import player

print(logo)
board = Board()
board.tutorial()

player1 = player.Human("X", "User")
player2 = player.Computer("O", "Computer")

curr_player = player2
eof_game = False

while not eof_game:

    turn = True
    while turn:
        if board.make_a_turn(curr_player):
            turn = False
        else:
            print("Invalid Move")
    if board.check_win(curr_player):
        eof_game = True
    if not board.check_eof_board():
        eof_game = True
    if curr_player == player1:
        curr_player = player2
    else:
        curr_player = player1





