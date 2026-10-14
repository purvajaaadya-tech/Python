import pygame

pygame.init()
s = pygame.display.set_mode((400, 300))
d = False

while not d:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            d = True
    pygame.draw.rect(s, (0, 50, 255), pygame.Rect(30, 80, 30, 80))

    pygame.display.flip()