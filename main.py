from Dataset import Dataset
from Agent import Agent
from Model import Model
from Driver import Driver


def main():
    game = Dataset()
    model = Model()
    player1 = Agent(game, model, False)
    player2 = Agent(game, model)
    driver = Driver(game, player1, player2, model)
    while True:
        answer = driver.play()
        if answer == 0:
            break
        driver.reset()


if __name__ == '__main__':
    main()
