import pygame
import random


class Creature:
    creatureCount = 0

    def __init__(self, screenWidth, screenHeight):
        self.xaxis = random.randint(0, screenWidth - 1)
        self.yaxis = random.randint(0, screenHeight - 1)
        Creature.creatureCount += 1
        self.energy = 50

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xaxis, self.yaxis, 10, 10))
