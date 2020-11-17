import pygame
import random


# Начнем с описания класса поля
class Board:
    # создание поля
    def __init__(self, width, height, screen):
        self.is_win = False
        self.opponent = True
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.screen = screen
        # значения по умолчанию
        self.count = 0
        self.left = 10
        self.top = 10
        self.cell_size = 200

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(self.screen, pygame.Color('black'),
                                 ((i * self.cell_size, j * self.cell_size), (self.cell_size, self.cell_size)), 1)

    def get_cell(self, pos):
        return pos[0] // self.cell_size, pos[1] // self.cell_size

    def get_click(self, pos):
        cell = self.get_cell(pos)
        if self.board[cell[0]][cell[1]] == 0:
            self.board[cell[0]][cell[1]] = 1 if self.opponent else 2
            score = pygame.font.SysFont('serif', 150)
            if self.opponent:
                text = score.render(str("X"), 1, pygame.Color('black'))
            else:
                text = score.render(str("0"), 1, pygame.Color('black'))
            self.screen.blit(text, (cell[0] * self.cell_size + 62, cell[1] * self.cell_size + 25))
            self.count += 1

    def change_turn(self):
        self.opponent = not self.opponent

    def reset(self):
        self.is_win = False
        screen.fill('white')
        self.count = 0
        self.board = [[0] * self.width for _ in range(self.height)]

    def check_full(self):
        if self.count == 10:
            pygame.time.wait(1200)
            self.reset()
        if self.count == 9 or self.is_win:
            self.count += 1

    def check_win(self):
        turn = 1 if self.opponent else 2
        if all(self.board[0][i] == turn for i in range(3)):
            pygame.draw.aaline(self.screen, 'red', [100, 20], [100, 550], 25)
            self.win()
        if all(self.board[1][i] == turn for i in range(3)):
            pygame.draw.aaline(self.screen, 'red', [200, 20], [200, 550], 25)
            # self.win()

    def win(self):
        pygame.draw.rect(self.screen, 'black', ((50, 100), (500, 350)))
        score = pygame.font.SysFont('serif', 50)
        end = ' Win' if self.opponent else ' Lose'
        text = score.render(str("You" + end), 1, pygame.Color('white'))
        self.screen.blit(text, (200, 250))
        self.is_win = True


size = width, height = (600, 600)
screen = pygame.display.set_mode(size)
pygame.init()

board = Board(3, 3, screen)
running = True
screen.fill('white')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            board.check_win()
            board.change_turn()
    board.render()
    board.check_full()
    pygame.display.flip()
