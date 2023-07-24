from display import Display
from game import Game

if __name__ == "__main__":
        game = Game(50, 30, 15)
        display = Display(game, 1000, 3)
        display.main()