import random
from colorama import Fore


class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def get_move(self):
        pass


class Human(Player):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.color = Fore.RED

    def get_move(self):
        move = int(input(Fore.RED + "[+] It's your move. Take a Cell: "))
        return move


class Computer(Player):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.color = Fore.YELLOW

    def get_move(self):
        move = random.randint(1, 9)
        return move
