import pygame

def m():
    pygame.init()
    sw, sh = 500, 500
    s = pygame.display.set_mode((sw, sh))
    pygame.display.set_caption('color changing sprite')

    c = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    cc = c['white']

    x, y = 30, 30
    spw, sph = 60, 60

    cl = pygame.time.Clock()

    d = False
    while not d:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                d = True

        p = pygame.key.get_pressed()
        if p[pygame.K_LEFT]: x -= 3
        if p[pygame.K_RIGHT]: x += 3
        if p[pygame.K_UP]: y -= 3
        if p[pygame.K_DOWN]: y += 3

        x = min(max(0, x), sw - spw)
        y = min(max(0, y), sh - sph)

        if x == 0: cc = c['blue']
        elif x == sw - spw: cc = c['yellow']
        elif y == 0: cc = c['red']
        elif y == sh - sph: cc = c['green']
        else:
            cc = c['white']

        s.fill((0, 0, 0))
        pygame.draw.rect(s, cc, (x, y, spw, sph))

        pygame.display.flip()
        cl.tick(90)

    pygame.quit()

if __name__ == "__main__":
    m()