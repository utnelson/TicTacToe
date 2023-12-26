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

    #curr_turn = True
    #while curr_turn:
    move_valid = board.make_a_turn(curr_player)
    if move_valid:
        curr_turn = False
    else:
        print("Invalid Move")
        curr_turn = False
    if curr_player == player1:
        curr_player = player2
    else:
        curr_player = player1

    #eof_game = True

