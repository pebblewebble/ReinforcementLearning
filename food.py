import random
import pygame


class Food:
    foodCount = 0
    def __init__(self, screenWidth, screenHeight):
        self.xaxis = random.randint(0, screenWidth)
        self.yaxis = random.randint(0, screenHeight)
        Food.foodCount+=1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.xaxis, self.yaxis, 5, 5))
