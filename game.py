import os
import random
from turtle import width
import pygame
WIN_HIEGHT = 567
WIN_WIDTH = 567
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HIEGHT))
pygame.display.set_caption("a good game")
pygame.init()

WHITE = (255, 255, 255)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(
    pygame.image.load('Assets/dvd.jpg'), (63, 50))


def draw_window(x, y):

    WIN.fill(WHITE)
    pygame.draw.rect(WIN, [255, 0, 0], [0, 0, 565, 565], 9)
    pygame.display.flip()
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (x, y))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    x, y = 0,  random.randint(0, 200)
    speed = 4
    xs, ys = speed, speed
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        shape_loc = draw_window(x, y)
        if x <= 15:
            xs = speed+random.randint(-2, 2)
        if x >= 499:
            xs = -speed+random.randint(-2, 2)
        if y <= 15:
            ys = speed+random.randint(-2, 2)
        if y >= 499:
            ys = -speed+random.randint(-2, 2)
        x += xs
        y += ys
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
