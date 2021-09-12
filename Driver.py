from Dataset import Dataset
from Agent import Agent
from Model import Model


class Driver:
    def __init__(self, dataset: Dataset, player1: Agent, player2: Agent, model: Model):
        self.game = dataset
        self.player1 = player1
        self.player2 = player2
        self.model = model

    def play(self):
        self.game.display()

        while not self.game.end or len(self.game.get_actions(self.game.get_state()[0])) == 0:
            self.player1.action()
            self.game.display()
            self.player2.action()
            self.game.display()

        print("Game Over!")
        if self.game.victor == -1:
            print("Player 2 wins!")
        elif self.game.victor == 1:
            print("Player 1 wins!")
        else:
            print("Draw!")

        again = int(input("Play again, swapping player play order? 1 for yes / 0 for no: "))
        return again

    def reset(self):
        # Reset game
        self.game.reset()

        # Swap player order
        temp = self.player1
        self.player1 = self.player2
        self.player2 = temp
