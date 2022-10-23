"""
Coding a snake game in python for fun.

Zac Pentecost - 22nd October 2022
"""


import pygame 
import random 
from enum import Enum
from collections import namedtuple

#----------------------- Define Classes and other Important Functions for Game 

Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20

class Direction(Enum):
    RIGHT = 1 
    LEFT = 2 
    UP = 3 
    DOWN  = 4 


class SnakeGame:

    def __init__(self, w = 640, h = 480):
        self.w = w
        self.h = h 

        #Initialise Display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        #Initialise Game State 
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self,h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

    def play_step(self):
        #1. Collect User Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN


if __name__ == '__main__':
    
    game = SnakeGame()

    #Game Loop 
    while True: 
        game.play_step()

        #Break if game over 

    pygame.quit()