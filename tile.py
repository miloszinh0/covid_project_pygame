import random

class Tile:
    def __init__(self):
        self.agent = False
        self.ill = False
        self.immune = False
        self.x = None
        self.y = None

    def create_ill_agent(self):
        self.agent = True
        self.ill = True

    def create_healthy_agent(self):
        self.agent = True

    def kill(self):
        self.agent = False
        self.ill = False
        self.immune = False

    def make_ill(self):
        self.agent = True
        self.ill = True
        self.immune = False

    def make_immune(self):
        self.agent = True
        self.ill = False
        self.immune = True

    def adjacent_tiles_coords(self):
        return ((self.x - 1, self.y - 1), (self.x - 1, self.y), (self.x - 1, self.y + 1), (self.x, self.y - 1),
                (self.x, self.y + 1), (self.x + 1, self.y - 1), (self.x + 1, self.y), (self.x + 1, self.y + 1))

    def infection_zone(self):
        return ((self.x - 1, self.y - 1), (self.x - 1, self.y), (self.x - 1, self.y + 1), (self.x, self.y - 1),
                (self.x, self.y + 1), (self.x + 1, self.y - 1), (self.x + 1, self.y), (self.x + 1, self.y + 1),
                (self.x - 2, self.y), (self.x + 2, self.y), (self.x, self.y - 2), (self.x, self.y + 2),
                (self.x + 2, self.y + 2), (self.x - 2, self.y + 2), (self.x + 2, self.y - 2), (self.x - 2, self.y - 2))

    def move(self, board, board_size):
        self.possible_moves = [[self.x-1, self.y-1], [self.x-1, self.y], [self.x-1, self.y+1], [self.x, self.y-1], [self.x, self.y+1], [self.x+1, self.y-1], [self.x+1, self.y], [self.x+1, self.y+1]]
        while True:
            self.next_move = random.sample(self.possible_moves, 1)[0]
            right_cords = 0
            for cord in self.next_move:
                if 0 <= cord < board_size:
                    right_cords += 1
            if right_cords == 2:
                if board[self.next_move[0]][self.next_move[1]].agent == True:
                    pass
                else:
                    board[self.next_move[0]][self.next_move[1]].agent = self.agent
                    board[self.next_move[0]][self.next_move[1]].ill = self.ill
                    board[self.next_move[0]][self.next_move[1]].immune = self.immune
                    board[self.next_move[0]][self.next_move[1]].x = self.next_move[0]
                    board[self.next_move[0]][self.next_move[1]].y = self.next_move[1]
                    break