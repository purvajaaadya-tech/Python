import pygame
pygame.init()

w = pygame.display.set_mode((400, 400))

w.fill((0, 0, 0))

wh = (255, 255, 255)

g = (0, 255, 0)

pygame.draw.circle(w, g, (300, 300), 50)

pygame.draw.circle(w, wh, (100, 100), 50, 3)

pygame.display.update()

r = True
while r:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False

pygame.quit()