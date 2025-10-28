import pygame as pg


import sys

import game_assets as ga
import map 

pg.init()
font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16) 
object_group = map.map2()
velocity_y = 0
gravity = 0.2   

# bg = pg.image.load("images/new_bg1.png")
screen = pg.display.set_mode((1000, 512))
clock = pg.time.Clock()

mario = ga.Mario(400,200,object_group)

font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16) 

score_title = font.render("SCORE", True, (255, 255, 255))  
coins_title = font.render("COINS", True, (255, 255, 255))  
world_title = font.render("WORLD", True, (255, 255, 255))  
time_title = font.render("TIME", True, (255, 255, 255))  
lives_title = font.render("LIVES", True, (255, 255, 255))     

titles = ["SCORE","COINS","WORLD","TIME","LIVES","BLINK","AMMO"]
space_title = screen.get_width()/len(titles)
plus_title = 0
running = True
while running: 
    for event in pg.event.get():
        if event.type == pg.QUIT :
            running = False             
    
    values = [
        lambda: str(mario.score),
        lambda: str(mario.coin),
        lambda : "1-1",
        lambda: str(mario.time_over//60),
        lambda: str(mario.lives),
        lambda: mario.get_time_countdown_blink(),
        lambda: "300",
    ] 
    

    plus = 600 - mario.rect.x
    mario.update(pg.key.get_pressed())
    
        

    for x in object_group:
        if not isinstance(x,(ga.Mario,ga.bg)):
            if abs(x.rect.x - mario.rect.x) <= 600  or (x.rect.left < mario.rect.x and x.rect.right > mario.rect.right): 
                x.update()
                
            if plus < 0 :
                screen.blit(x.image, (x.rect.x+plus,x.rect.y))
            else :
                screen.blit(x.image, (x.rect.x,x.rect.y))
            # pg.draw.rect(screen,(255,0,0),x.rect,2)
        elif isinstance(x,ga.bg):
            x.update()
            if plus < 0 :
                screen.blit(x.image, (x.rect.x+plus,x.rect.y))
            else :
                screen.blit(x.image, (x.rect.x,x.rect.y))

    for i in range (0,len(titles)):
        title = font.render(titles[i], True, (255, 255, 255)) 
        value = font.render(values[i](), True, (255, 255, 255)) 
        centerx = space_title*i + space_title//2
        screen.blit(title,(centerx-title.get_width()//2,10))
        screen.blit(value,(centerx-value.get_width()//2,35))
    
    if plus < 0 :
         screen.blit(mario.image,(mario.rect.x + plus,mario.rect.y))
    else :
        screen.blit(mario.image,mario.rect)
    

    # pg.draw.rect(screen,(255,0,0),mario.rect,2)

    pg.display.update()  
    
    clock.tick(60)

pg .quit()
sys.exit() 
