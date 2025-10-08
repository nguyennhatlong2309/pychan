import pygame as pg
import game_assets as ga

def map1():
    terrrain_group = pg.sprite.Group()

    # tao san` 
    terrrain_group.add(ga.floor(2000,0,600))

    for x in range(0,10):
        terrrain_group.add(ga.floor(50,100,450-(x*32)))

  

    return terrrain_group


