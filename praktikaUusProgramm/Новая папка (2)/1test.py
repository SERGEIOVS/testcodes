import pygame as pg
import sys
 
sc = pg.display.set_mode((400, 400))
 
rect1 = pg.Rect((0, 0, 30, 30))

#узнаем нужные данные области rect  
print(rect1.topleft)  # (30, 30)
print(rect1.topright)  # (30, 30)
print(rect1.width)  # 70

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()