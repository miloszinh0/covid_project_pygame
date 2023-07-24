import random

class Tile:
    def __init__(self):
        self.agent = False
        self.ill = False
        self.immune = False
        self.illness_time = 0
        self.immune_time = 0
        self.x = None
        self.y = None
        self.last_move = 0

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
        self.illness_time = 0
        self.immune_time = random.randint(30, 60)

    def make_healthy(self):
        self.agent = True
        self.ill = False
        self.immune = False
        


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
            rand_nr = random.randint(0, 3)

            if rand_nr == 0:
                self.next_move = random.sample(self.possible_moves, 1)[0]
            else:
                self.next_move = self.possible_moves[self.last_move]

            right_cords = 0
            for cord in self.next_move:

                if 0 <= cord < board_size:
                    right_cords += 1

            if right_cords == 2:

                if board[self.next_move[0]][self.next_move[1]].agent == True:
                    pass
                else:
                    for n in range(8):
                        
                        if self.possible_moves[n] == self.next_move:
                            self.last_move = n
                    
                    board[self.next_move[0]][self.next_move[1]].agent = self.agent
                    board[self.next_move[0]][self.next_move[1]].ill = self.ill
                    board[self.next_move[0]][self.next_move[1]].immune = self.immune
                    board[self.next_move[0]][self.next_move[1]].illness_time = self.illness_time    

                    board[self.next_move[0]][self.next_move[1]].x = self.next_move[0]
                    board[self.next_move[0]][self.next_move[1]].y = self.next_move[1]

                    board[self.next_move[0]][self.next_move[1]].last_move = self.last_move
                    break

                    
            