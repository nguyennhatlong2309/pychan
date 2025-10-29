import pygame as pg
import game_assets as ga
import map 
import sys

pg.init()

object_group = map.map3()
velocity_y = 0
gravity = 0.2   


screen = pg.display.set_mode((1200, 512))
clock = pg.time.Clock()

mario = ga.Mario(450,200,object_group)

plus = 5100
running = True
while running: 
    for event in pg.event.get():
        if event.type == pg.QUIT :
            running = False             
    
    mario.current_time = pg.time.get_ticks()
    mario.are_going = False

    # plus = 600 - mario.rect.x

    mario.update(pg.key.get_pressed())


    
    for x in object_group:
        if not isinstance(x,ga.Mario):
            
            x.update()
            screen.blit(x.image,(x.rect.x-plus,x.rect.y))
            

        # pg.draw.rect(screen,(255,0,0),x.rect,2)

    pg.display.update()  

    clock.tick(60)

pg .quit()
sys.exit() 
