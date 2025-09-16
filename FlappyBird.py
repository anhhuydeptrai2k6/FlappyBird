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
cot_xanh_duoi_rect = cot_xanh_duoi.get_rect()
cot_xanh_tren = pygame.transform.flip(cot_xanh_duoi, False, True)
cot_xanh_tren = pygame.transform.scale(cot_xanh_tren, (41*1.5, 253*1.5))
cot_xanh_tren_rect = cot_xanh_tren.get_rect()
taocot = pygame.USEREVENT
dscot = []

game_over = pygame.image.load("assets/FlappyBird/game_over.png")
game_over = pygame.transform.scale(game_over, (192*1.5, 42*1.5))

khoi_dong = pygame.image.load("assets/FlappyBird/khoi_dong.png")
khoi_dong = pygame.transform.scale(khoi_dong, (145*1.5, 210*1.5))
choilandau = 1

trongluc = 600
chimbay = 0
dangchoi = False
gameover = False

while True:
    delta = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            if gameover:
                dscot.clear()
                chim_rect.center = (100, 350)
                chimbay = 0
                matdatX = 0
                gameover = False

            if not dangchoi:
                pygame.time.set_timer(taocot, 3000)
            dangchoi = True
            gameover = False
            choilandau = 2
            chimbay = -300
        if event.type == taocot:
            y = random.randint(200, 450)
            dscot.append([432, y])

    if dangchoi and not gameover:
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

    if choilandau == 1:
        screen.blit(khoi_dong, (110, 150))

    chim_xoay = pygame.transform.rotate(chim[frame], goc)
    chim_xoay_rect = chim_xoay.get_rect(center = chim_rect.center)
    screen.blit(chim_xoay, chim_xoay_rect)

    if not gameover:
        for cot in dscot:
            cot_duoi_rect = pygame.Rect(cot[0], cot[1], 41 * 1.5, 253 * 1.5)
            cot_tren_rect = pygame.Rect(cot[0], cot[1] - 550, 41 * 1.5, 253 * 1.5)
            if (chim_rect.colliderect(cot_duoi_rect) or chim_rect.colliderect(cot_tren_rect)) and not gameover:
                gameover = True
                dangchoi = False
            if not gameover:
                cot[0] -= 3
            screen.blit(cot_xanh_duoi, (cot[0], cot[1]))
            screen.blit(cot_xanh_tren, (cot[0], cot[1] - 550))
            if cot[0] < -41*1.5:
                dscot.remove(cot)
    if (chim_rect.top < 0 or chim_rect.bottom > 544) and not gameover:
        gameover = True
        dangchoi = False
    if gameover and not dangchoi:
        chimbay = 0
        frame = 1
        for cot in dscot:
            screen.blit(cot_xanh_duoi, (cot[0], cot[1]))
            screen.blit(cot_xanh_tren, (cot[0], cot[1] - 550))
        screen.blit(game_over, (80, 280))

    if not gameover:
        matdatX -= 1
    if matdatX < -672 :
        matdatX += 672
    for i in range(0,2,1):
        screen.blit(mat_dat, (matdatX + i*672, 544))

    pygame.display.update()
