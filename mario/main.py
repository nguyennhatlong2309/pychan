import pygame as pg
import game_assets as ga

pg.init()

velocity_y = 0
gravity = 0.2

bg = pg.image.load("images/bg.png")
screen = pg.display.set_mode((1200, 664))
clock = pg.time.Clock()

mario = ga.Mario(150,200)

terrain = ga.floor(2000,0,632)
terrain_group = pg.sprite.Group()
t = ga.floor(50,200,250)
t1 = ga.floor(50,70,600)
t2 = ga.floor(50,300,600)

for x in range(0,2):
    terrain1 = ga.floor(50,500,500-(x*64))
    terrain1.image = pg.transform.scale_by(terrain1.image,2)
    terrain1.rect = terrain1.image.get_rect(topleft=terrain1.rect.topleft)
    terrain_group.add(terrain1)
terrain_group.add(terrain)
terrain_group.add(t,t1,t2)



while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()  

    
    mario.current_time = pg.time.get_ticks()
    mario.are_going = False
    
    if not mario.lose :
        keys = pg.key.get_pressed()
    
        if keys[pg.K_RIGHT]:
            mario.direct = 1
            mario.move_x()
       
        if keys[pg.K_LEFT]:
            mario.direct = -1
            mario.move_x()
        
        if keys[pg.K_UP]:
            mario.jump()

        

        mario.check_collide(terrain_group)
    
    
    mario.update()

    screen.blit(bg, (0, 0))
    
    for x in terrain_group:
        screen.blit(x.image, x.rect)
        pg.draw.rect(screen,(255,0,0),x.rect,2)   
    screen.blit(mario.image,mario.rect)
    
    
    
    pg.draw.rect(screen,(255,0,0),mario.rect,2)
    # pg.draw.rect(screen,(255,0,0),terrain.rect,2)
    pg.display.update()

    clock.tick(120)
