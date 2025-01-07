from interfaces import TerminalInterface, ColorInterface
from os import system, name

class Terminal(TerminalInterface):
    def __init__(self):
        self.osName = name
    
    def clear(self):
        if self.osName == 'nt':
            system("cls")
        else:
            system("clear")

    def drawLine(self, char: str, width: int):
        print(char * width)

    def printAtCenter(self, message: str, width: int):
        print(f'{message}'.center(width))

class Color(ColorInterface):
    def __init__(self):
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.blue = '\033[34m'
        self.yellow = '\033[33m'
        self.regular = '\033[m'
        self.cyan = '\033[36m'
        self.purple = '\033[35m'