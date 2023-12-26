from colorama import Fore


class Board:
    def __init__(self):
        self.cells = {1: " ", 2: " ", 3: " ",
                      4: " ", 5: " ", 6: " ",
                      7: " ", 8: " ", 9: " "}
        self.win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                               [1, 4, 7], [2, 5, 8], [3, 6, 9],
                               [1, 5, 8], [3, 5, 7]]

    def check_valid_move(self, choice):
        return self.cells[choice] == " "

    def make_a_turn(self, player):
        choice = player.get_move()
        symbol = player.symbol
        if self.check_valid_move(choice):
            print(player.color + f"[+] {player.name} took cell {choice}")
            self.cells[choice] = symbol
            self.show_board()
            return True
        return False

    def show_board(self):
        # 3x3 Board
        print(Fore.WHITE + "====================================")
        for key, value in self.cells.items():
            row = ""
            row += f"[{value}]"
            if key % 3 == 0:
                row += "\n"
            print(row, end="")
        print(Fore.WHITE + "====================================")

    def tutorial(self):
        print(f"Game Description")
        # print(f"User has: {self.player_symbols['user']}, Computer has {self.player_symbols['computer']}")
        print("""
==================================== 
[1][2][3]
[4][5][6]
[7][8][9]
====================================""")
