import pygame

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (204, 0, 0)
GREEN = (0, 204, 0)
BLUE = (0, 0, 204)
YELLOW = (255, 255, 0)

class Display:
    def __init__(self, game, size, fps):
        '''
        Display(game: object Game, size: int, fps: int)
        game - object of class Game
        size - size of the pygame window
        fps - number of frames per second
        '''
        self.game = game
        self.size = size
        self.fps = fps
        self.window = pygame.display.set_mode((self.size ,self.size))

    def draw_window(self):
        '''
        Function draws window.
        '''
        self.window.fill(WHITE)
        for x in range(self.game.board_size):
            for y in range(self.game.board_size):
                if self.game.board[x][y].ill:
                    color = RED
                elif self.game.board[x][y].immune:
                    color = BLUE
                elif self.game.board[x][y].agent:
                    color = GREEN
                else:
                    color = YELLOW
                rect = pygame.Rect(x * self.size/self.game.board_size, y * self.size/self.game.board_size, self.size/self.game.board_size, self.size/self.game.board_size)
                pygame.draw.rect(self.window, color, rect)
        pygame.display.update()

    def main(self):
        '''
        Main function managing the project.
        '''
        self.game.random_board()
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.fps)
            self.game.update()
            self.draw_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()