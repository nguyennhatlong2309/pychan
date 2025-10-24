import pygame as pg
import game_assets as ga
import map 
import sys

pg.init()

object_group = map.map1()
velocity_y = 0
gravity = 0.2   

bg = pg.image.load("images/bg.png")
screen = pg.display.set_mode((1200, 664))
clock = pg.time.Clock()

mario = ga.Mario(450,200,object_group)



running = True
while running: 
    for event in pg.event.get():
        if event.type == pg.QUIT :
            running = False
             
    
    mario.current_time = pg.time.get_ticks()
    mario.are_going = False

    plus = 600 - mario.rect.x

    mario.update(pg.key.get_pressed())

    screen.blit(bg, (0, 0))
    
    for x in object_group:
        if not isinstance(x,ga.Mario):
            if abs(x.rect.x - mario.rect.x) <= 600 : 
                x.update()
            if plus < 0:
                screen.blit(x.image, (x.rect.x+plus,x.rect.y))
            else :
                screen.blit(x.image, (x.rect.x,x.rect.y))

        # pg.draw.rect(screen,(255,0,0),x.rect,2)
    if plus < 0 :
         screen.blit(mario.image,(mario.rect.x + plus,mario.rect.y))
    else :
        screen.blit(mario.image,mario.rect)
    
    
    # pg.draw.rect(screen,(255,0,0),mario.rect,2)

   

    clock.tick(60)

pg .quit()
sys.exit() 
