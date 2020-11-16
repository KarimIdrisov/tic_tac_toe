import pygame
import random


# Начнем с описания класса поля
class Board:
    # создание поля
    def __init__(self, width, height, screen):
        self.opponent = False;
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
            self.board[cell[0]][cell[1]] = 1
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
        screen.fill('white')
        self.count = 0
        self.board = [[0] * width for _ in range(height)]

    def check_full(self):
        if self.count == 10:
            pygame.time.wait(600)
            self.reset()
        if self.count == 9:
            self.count += 1

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
            board.change_turn()
    board.render()
    board.check_full()
    pygame.display.flip()
