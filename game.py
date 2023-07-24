from tile import Tile
import random
import numpy as np

class Game:
    def __init__(self, board_size, agents, ill_agents):
        self.board_size = board_size
        self.agents = agents
        self.ill_agents = ill_agents

        self.board = [[Tile() for _ in range(self.board_size)] for _ in range(self.board_size)]

    def random_board(self):
        ill = 0
        while ill < self.agents:

            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)

            if self.board[x][y].agent == False:

                if ill < self.ill_agents:
                    self.board[x][y].create_ill_agent()

                else:
                    self.board[x][y].create_healthy_agent()

                self.board[x][y].x = x
                self.board[x][y].y = y

                ill += 1

    def print_board(self):
        printed_board = np.zeros((self.board_size, self.board_size))

        for x in range(self.board_size):
            for y in range(self.board_size):

                if self.board[x][y].agent == True:
                    printed_board[x,y] = 1

                if self.board[x][y].ill == True:
                    printed_board[x,y] = 2
        print(printed_board)

    def update(self):
        self.next_board = [[Tile() for _ in range(self.board_size)] for _ in range(self.board_size)]
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y].agent:
                    self.board[x][y].move(self.next_board, self.board_size)
        self.board = self.next_board
        self.update_illness()

    def update_illness(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y].ill:
                    self.board[x][y].illness_time += 1
                    for zone in self.board[x][y].infection_zone():
                        if 0 <= zone[0] < self.board_size and 0 <= zone[1] < self.board_size:
                            if self.board[zone[0]][zone[1]].agent and not self.board[zone[0]][zone[1]].immune:
                                self.board[zone[0]][zone[1]].ill = True

                if self.board[x][y].illness_time > 15:
                    rand = random.randint(1, 10)
                    if rand == 1:
                        self.board[x][y].kill()
                    elif rand == 2:
                        self.board[x][y].make_immune()

                if self.board[x][y].immune:
                    self.board[x][y].immune_time -= 1
                    if self.board[x][y].immune_time == 0:
                        self.board[x][y].make_healthy()