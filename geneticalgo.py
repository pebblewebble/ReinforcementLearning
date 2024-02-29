import pygame
import random
import food
import creature

pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True
while run:
    # pygame.draw.rect(
    #     screen,
    #     (255, 0, 0),
    #     pygame.Rect((random.randint(0, 799), random.randint(0, 749), 5, 5)),
    # )
    # pygame.draw.rect(screen,(255,0,0),randomRect)
    if creature.Creature.creatureCount < 5:
        creature.Creature(SCREEN_WIDTH, SCREEN_HEIGHT).draw(screen)
    if food.Food.foodCount < 5:
        food.Food(SCREEN_WIDTH, SCREEN_HEIGHT).draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
