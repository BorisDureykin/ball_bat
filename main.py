import pygame
import sys

from pygame.color import THECOLORS


import game
from ball import Ball
from bat import Bat
from figuer import Figuer
pygame.init()
FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 600

font = pygame.font.Font(None,25)
font1 = pygame.font.Font(None,40)

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
a = 10 # радиус Ball
lx=0 # Изменение по Х
ly=0 # Изменение по Y
j=0 # Счетчик отбиваний
jf=0 # Счетчик попаданий
s = 100 # Ширина биты
if s  >WIN_WIDTH//2:
    s = WIN_WIDTH//2
h = 5 # высота биты

xFiguer=0
yFiguer=0
widthf=0
heightf=0


color=THECOLORS['darkgreen']
color1=THECOLORS['black']
x=WIN_WIDTH//2
y=WIN_HEIGHT-h-a
# bat = Bat(sc, WIN_WIDTH, WIN_HEIGHT,s,h)
# ball = Ball(sc,color, x,y, WIN_WIDTH, WIN_HEIGHT)
# figuer= Figuer(sc,color1,xFiguer,yFiguer,widthF, heightF)





if __name__ == '__main__':
    while 1:

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        sc.fill(THECOLORS['aliceblue'])



        bat = Bat(sc, WIN_WIDTH, WIN_HEIGHT, s, h)
        ball = Ball(sc, color, x, y, WIN_WIDTH, WIN_HEIGHT)
        figuer = Figuer(sc, color1, (100, 200), 150, 20)
        xBat = bat.k
        xFiguer = figuer.xf
        yFiguer = figuer.yf
        heightf = figuer.heightFig
        widthf = figuer.widthFig


        if y == yFiguer + heightf + a and xFiguer <= x <= xFiguer + widthf:
            ly *= -1
            jf += 1
            print(xFiguer, yFiguer)
        if y == yFiguer - a and xFiguer <= x <= xFiguer + widthf:
            ly *= -1
            jf += 1

        if x == xFiguer - a and yFiguer <= y <= yFiguer + heightf:
            lx *= -1
            jf += 1
        if x == xFiguer + widthf + a and yFiguer <= y <= yFiguer + heightf:
            lx *= -1
            jf += 1

        if xBat <= x < (xBat + s // 7) and (y == WIN_HEIGHT - a - h) \
                or (xBat + s * 6 // 7) < x <= (xBat + s) and (y == WIN_HEIGHT - a - h):
            ly = (-1)
            if (xBat + s * 6 // 7) < x <= (xBat + s):
                lx = 5
            else:
                lx = (-5)
            j += 1

        if (xBat + s // 7) <= x < (xBat + s * 2 // 7) and (y == WIN_HEIGHT - a - h) \
                or (xBat + s * 5 // 7) < x <= (xBat + s * 6 // 7) and (y == WIN_HEIGHT - a - h):
            ly = (-2)
            if (xBat + s * 5 // 7) < x <= (xBat + s * 6 // 7):
                lx = 4
            else:
                lx = (-4)
            j += 1

        if (xBat + s * 2 // 7) <= x < (xBat + s * 3 // 7) and (y == WIN_HEIGHT - a - h) \
                or (xBat + s * 4 // 7) < x <= (xBat + s * 5 // 7) and (y == WIN_HEIGHT - a - h):
            ly = (-4)
            if (xBat + s * 4 // 7) < x <= (xBat + s * 5 // 7):
                lx = 2
            else:
                lx = (-2)
            j += 1

        if (xBat + s * 3 // 7) <= x <= (xBat + s * 4 // 7) and (y == WIN_HEIGHT - a - h):
            ly = (-5)
            if lx > 0:
                lx = 1
            else:
                lx = (-1)
            j += 1

        if y <= (a+20):
            ly *= (-1)

        if x <= a:
            lx *= (-1)

        if x >= WIN_WIDTH-a:
            lx *= (-1)

        if y >= WIN_HEIGHT or j == 50:

            while 2:
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        sys.exit()
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if i.button == 1:
                            sys.exit()

                sc.fill(THECOLORS['aliceblue'])
                text = font1.render("Игра Завершена!", True, THECOLORS['cadetblue4'])
                text2 = font1.render(f'Отбито мячей: {str(j)}', True, THECOLORS['cadetblue4'])
                text_rect=text.get_rect(center=[WIN_WIDTH/2, WIN_HEIGHT/2-10])
                text2_rect = text2.get_rect(center=[WIN_WIDTH / 2, WIN_HEIGHT / 2 +25])

                sc.blit(text,text_rect)
                sc.blit(text2, text2_rect)
                pygame.display.update()
                clock.tick(FPS)
            # continue

        if j>=10 and j<20:
            FPS=90
            color=THECOLORS['darkorange']
        if j>=20 and j<30:
            FPS=120
            color = THECOLORS['red4']
        if j>=30 and j<40:
            FPS=150
            color = THECOLORS['purple4']
        if j>=40 and j<50:
            FPS=180
            color = THECOLORS['brown3']
        text = font.render("Отбито мячей: ", True, THECOLORS['black'])
        text2 = font.render(str(j) + " : " + str(jf), True, THECOLORS['black'])

        sc.blit(text, [20, 5])
        sc.blit(text2, [145, 5])


        ball.x = x + lx
        ball.y = y + ly
        x = ball.x
        y = ball.y
        pygame.display.update()
        clock.tick(FPS)
        # xFiguer = figuer.xf
        # yFiguer = figuer.yf
        # continue





