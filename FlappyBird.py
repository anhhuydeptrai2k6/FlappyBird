import random
import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((432, 768))
caption = pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("assets/FlappyBird/chim_2.png")
icon = pygame.transform.scale(icon,(32,32))
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
timedoiframe = 0
frame = 0

anh_nen = pygame.image.load("assets/FlappyBird/anh_nen.png")
anh_nen = pygame.transform.scale(anh_nen, (432, 768))

mat_dat = pygame.image.load("assets/FlappyBird/mat_dat.png")
mat_dat = pygame.transform.scale(mat_dat, (672, 224))
matdatX = 0

chim = [None] * 3
chim[0] = pygame.image.load("assets/FlappyBird/chim_1.png")
chim[0] = pygame.transform.scale(chim[0], (34 * 1.5, 24*1.5))
chim[1] = pygame.image.load("assets/FlappyBird/chim_2.png")
chim[1] = pygame.transform.scale(chim[1], (34 * 1.5, 24*1.5))
chim[2] = pygame.image.load("assets/FlappyBird/chim_3.png")
chim[2] = pygame.transform.scale(chim[2], (34 * 1.5, 24*1.5))
chim_rect = chim[1].get_rect(center = (100, 350))

cot_xanh_duoi = pygame.image.load("assets/FlappyBird/cot_xanh.png")
cot_xanh_duoi = pygame.transform.scale(cot_xanh_duoi, (41*1.5, 253*1.5))
cot_xanh_tren = pygame.transform.flip(cot_xanh_duoi, False, True)
cot_xanh_tren = pygame.transform.scale(cot_xanh_tren, (41*1.5, 253*1.5))
taocot = pygame.USEREVENT
dscot = []

trongluc = 600
chimbay = 0
dangchoi = False

while True:
    delta = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            if not dangchoi:
                pygame.time.set_timer(taocot, 3000)
            dangchoi = True
            chimbay = -300
        if event.type == taocot:
            y = random.randint(200, 450)
            dscot.append([432, y])

    if dangchoi:
        chimbay += trongluc * delta
        chim_rect.centery += chimbay * delta

        timedoiframe += delta
        if timedoiframe >= 0.06:
            frame = (frame + 1) % 3
            timedoiframe = 0
        if chimbay < 0:
            goc = 45
        else:
            goc = -45
    if not dangchoi:
        frame = 1
        goc = 0

    screen.blit(anh_nen, (0, 0))

    chim_xoay = pygame.transform.rotate(chim[frame], goc)
    chim_xoay_rect = chim_xoay.get_rect(center = chim_rect.center)
    screen.blit(chim_xoay, chim_xoay_rect)


    for cot in dscot:
        cot[0] -= 3
        screen.blit(cot_xanh_duoi, (cot[0], cot[1]))
        screen.blit(cot_xanh_tren, (cot[0], cot[1] - 550))
        if cot[0] < -41*1.5:
            dscot.remove(cot)

    matdatX -= 1
    if matdatX < -672 :
        matdatX += 672
    for i in range(0,2,1):
        screen.blit(mat_dat, (matdatX + i*672, 544))

    pygame.display.update()
