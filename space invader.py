import math
import random
import pygame

sw = 800
sh = 500
psx = 370
psy = 380
esym = 50
esyma = 150
esx = 4
esy = 40
bsy = 10
cd = 27

pygame.init()

s = pygame.display.set_mode((sw, sh))

b = pygame.image.load('background.png')

pygame.display.set_caption("Space Invader")
i = pygame.image.load('ufo.png')
pygame.display.set_icon(i)

pi = pygame.image.load('player.png')
px = psx
py = psy
pxc = 0

ei = []
ex = []
ey = []
exc = []
eyc = []
noe = 6

for i in range(noe):
    ei.append(pygame.image.load('enemy.png'))
    ex.append(random.randint(0, sw - 64))

    ey.append(random.randint(esym, esyma))
    exc.append(esx)
    eyc.append(eyc)

bi = pygame.image.load('bullet.png')
bx = 0
by = psy
bxc = 0
byc = bsy
bs = "ready"

sv = 0
f = pygame.font.Font('freesansbold.ttf', 32)
tx = 10
ty = 10

of = pygame.font.Font('freesanabold.ttf', 64)

def ss(x, y):
    sc = f.render("Score : " + str(sv), True, (255, 255, 255))
    s.blit(sc, (x, y))

def got():
    ot = of.render("GAME OVER", True, (255, 255, 255))
    s.blit(ot, (200, 250))

def p(x, y):
    s.blit(pi, (x, y))

def e(x, y, i):
    s.blit(ei[i], (x, y))

def fb(x, y):
    global bs
    bs = "fire"
    s.blit(bi, (x + 16, y + 10))

def ic(ex, ey, bx, by):
    d = math.sqrt((ex - bx) ** 2 + (ey - by ** 2))
    return d < cd

r = True
while r:
    s.fill((0, 0, 0))
    s.blit(b, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxc = -5
            if event.key == pygame.K_RIGHT:
                pxc = 5
            if event.key == pygame.K_SPACE and bs == "ready":
                bx = px
                fb(bx, by)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            pxc = 0

    px += pxc
    px = max(0, min(px, sw - 64))

    for i in range(noe):
        if ey[i] > 340:
            for j in range(noe):
                ey[j] = 2000
            got()
            break

        ex[i] += exc[i]
        if ex[i] <= 0 or ex[i] >= sw - 64:
            exc[i] *= -1
            ey[i] += eyc[i]

        if ic(ex[i], ey[i], bx, by):
            by = psy
            bs = "ready"
            sv += 1
            ex[i] = random.randint(0, sw - 64)
            ey[i] = random.randint(esym, esyma)

        e(ex[i], ey[i], i)

    if by <= 0:
        by = psy
        bs = "ready"
    elif bs =="fire":
        fb(bx, by)
        by -= byc

    p(px, py)
    ss(tx, ty)
    pygame.display.update()