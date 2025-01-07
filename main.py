from interfaces import TerminalInterface, ColorInterface
from random import choice
from sys import exit
from implementations import Terminal, Color

class Jokenpo:
    def __init__(self, terminal: TerminalInterface, colors: ColorInterface):
        self.options = ['rock', 'paper', 'scissors']
        self.terminal = terminal
        self.colors = colors
        self.playerPoints = 0
        self.computerPoints = 0
        self.rounds = 0

    def showHeader(self):
        self.terminal.drawLine(char="=", width=60)
        self.terminal.printAtCenter('Rock, paper, scissors', 60)
        self.terminal.drawLine(char="=", width=60)
    
    def computeScore(self, player, computer):
        if player == computer:
            pass
    
        if player == 'rock' and computer == 'paper':
            self.computerPoints += 1

        if player == 'paper' and computer == 'scissors':
            self.computerPoints += 1

        if player == 'scissors' and computer == 'rock':
            self.computerPoints += 1

        if player == 'paper' and computer == 'rock':
            self.playerPoints += 1

        if player == 'scissors' and computer == 'paper':
            self.playerPoints += 1

        if player == 'rock' and computer == 'scissors':
            self.playerPoints += 1

    def getComputerChoice(self):
        return choice(self.options)
    
    def getPlayerChoice(self):
        choiceMap = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors'
        }

        try:
            choice = int(input("Enter your choice: "))
        except:
            print('Your choice must be numeric.')
            exit()

        if choice == 0:
            exit()

        while (choice < 1 or choice > 3):
            print('Pick an valid choice.')
            choice = int(input("Enter your choice: "))
        
        return choiceMap[str(choice)]
  
    def playRound(self):
        self.terminal.printAtCenter(f'{self.colors.yellow}Round: {self.rounds}{self.colors.regular}', 64)
        self.terminal.printAtCenter(f"You: {self.playerPoints}   |   Computer: {self.computerPoints}", 60)
        self.terminal.drawLine(char="=", width=60)

        print(f'[1] - rock, [2] - paper, [3] - scissors  |  {self.colors.red}[0] - Quit{self.colors.regular}')
        self.terminal.drawLine(char="-", width=60)

        player = self.getPlayerChoice()
        computer = self.getComputerChoice()

        self.computeScore(player, computer)

        self.rounds += 1

    def evalWinner(self):

        self.terminal.printAtCenter(f'{self.colors.yellow}Final Score{self.colors.regular}', 66)
        self.terminal.printAtCenter(f'{self.colors.cyan}Computer: {self.computerPoints}{self.colors.regular}', 66)
        self.terminal.printAtCenter(f'{self.colors.purple}You: {self.playerPoints}{self.colors.regular}', 66)

        if self.computerPoints == self.playerPoints:
            self.terminal.printAtCenter(f"{self.colors.blue}Draw!{self.colors.regular}", 66)
        if self.computerPoints > self.playerPoints:
            self.terminal.printAtCenter(f"{self.colors.green}Computer wins!{self.colors.regular}", 66)
        if self.computerPoints < self.playerPoints:
            self.terminal.printAtCenter(f"{self.colors.green}Player wins!{self.colors.regular}", 66)

    def startGame(self):

        self.terminal.clear()

        while self.rounds <= 2:
            self.terminal.clear()
            self.showHeader()
            self.playRound()

        self.terminal.clear()
        self.showHeader()
        self.evalWinner()

        
if __name__ == '__main__':

    terminal = Terminal()
    colors = Color()

    game = Jokenpo(terminal, colors)

    game.startGame()
