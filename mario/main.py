import pygame as pg
import game_assets as ga

pg.init()

object_group = pg.sprite.Group()
velocity_y = 0
gravity = 0.2

bg = pg.image.load("images/bg.png")
screen = pg.display.set_mode((1200, 664))
clock = pg.time.Clock()



terrain = ga.floor(2000,0,632)

mario = ga.Mario(150,200,object_group)
t = ga.floor(50,200,250)
t1 = ga.floor(50,70,600)
t2 = ga.floor(50,300,600)
t3 = ga.floor(50,600,600)
t4 = ga.floor(50,300,568)
enemy = ga.koopatroopa(450,550,object_group)


object_group.add(terrain)

object_group.add(t,t1,t2,t3,t4,enemy,mario)


running = True
while running: 
    for event in pg.event.get():
        if event.type == pg.QUIT :
            running = False
            pg.quit()
            exit()  

    
    mario.current_time = pg.time.get_ticks()
    mario.are_going = False
    
    

        

    
    
    enemy.update()
    mario.update(pg.key.get_pressed())

    screen.blit(bg, (0, 0))
    
    for x in object_group:
        screen.blit(x.image, x.rect)
        pg.draw.rect(screen,(255,0,0),x.rect,2)   
    screen.blit(mario.image,mario.rect)
    
    
    
    
    pg.draw.rect(screen,(255,0,0),mario.rect,2)
    # pg.draw.rect(screen,(255,0,0),terrain.rect,2)
    pg.display.update()

    clock.tick(60)
