import pygame as pg
import game_assets as ga

def map1():
    terrrain_group = pg.sprite.Group()
    
    
    # tao san` 
    ga.floor(2200,0,608,terrrain_group)
    ga.floor(2498,2270,608,terrrain_group)
    ga.floor(498,4270,608,terrrain_group)
    ga.floor(2000,4832,608,terrrain_group)



    ga.brick(15,15,terrrain_group)  

    ga.brick(19,15,terrrain_group)
    ga.question_block(20,15,1,1,terrrain_group)
    ga.brick(21,15,terrrain_group)
    ga.question_block(21,11,1,1,terrrain_group)
    ga.question_block(22,15,1,1,terrrain_group)
    ga.brick(23,15,terrrain_group)
     
   
    
    ga.pipe(900,1,terrrain_group)
    ga.pipe(1150,2,terrrain_group)
    ga.goomba(1300,576,terrrain_group)
    ga.pipe(1400,3,terrrain_group)
    ga.goomba(1600,576,terrrain_group)
    ga.goomba(1650,576,terrrain_group)
    ga.pipe(1700,3,terrrain_group)



    ga.brick(77,15,terrrain_group)
    ga.question_block(78,15,2,1,terrrain_group)
    ga.brick(79,15,terrrain_group)
    ga.brick(79,11,terrrain_group)

    ga.brick(80,11,terrrain_group)
    ga.brick(81,11,terrrain_group)
    
    ga.brick(82,11,terrrain_group)
    ga.brick(83,11,terrrain_group)
    ga.brick(84,11,terrrain_group)
    ga.goomba(83*32,320,terrrain_group)
    ga.goomba(84*32,320,terrrain_group)
    ga.brick(85,11,terrrain_group)

    ga.brick(88,11,terrrain_group)
    ga.brick(89,11,terrrain_group)
    ga.brick(90,11,terrrain_group)
    ga.question_block(91,11,2,1,terrrain_group)
    ga.brick(91,15,terrrain_group)

    ga.goomba(90*32,18*32,terrrain_group)
    ga.goomba(83*32,18*32,terrrain_group)



    ga.brick(97,15,terrrain_group)
    ga.brick(98,15,terrrain_group)


    ga.koopatroopa(103*32,560,terrrain_group)
    ga.goomba(109*32,576,terrrain_group)


    ga.question_block(103,15,1,1,terrrain_group)
    ga.question_block(106,15,1,1,terrrain_group)
    ga.question_block(106,11,1,1,terrrain_group)
    ga.question_block(109,15,1,1,terrrain_group)

    ga.goomba(3500,544,terrrain_group)

    ga.brick(115,15,terrrain_group)
    ga.brick(118,11,terrrain_group)
    ga.brick(119,11,terrrain_group)
    ga.brick(120,11,terrrain_group)


    ga.brick(124,11,terrrain_group)
    ga.question_block(125,11,1,1,terrrain_group)
    ga.brick(125,15,terrrain_group)
    ga.question_block(126,11,1,1,terrrain_group)
    ga.brick(126,15,terrrain_group)
    ga.brick(127,11,terrrain_group)

    ga.block(130,18,terrrain_group)
    ga.block(131,18,terrrain_group)
    ga.block(131,17,terrrain_group)
    ga.block(132,18,terrrain_group)
    ga.block(132,17,terrrain_group)
    ga.block(132,16,terrrain_group)
    ga.block(133,18,terrrain_group)
    ga.block(133,17,terrrain_group)
    ga.block(133,16,terrrain_group)
    ga.block(133,15,terrrain_group)
    

    ga.block(136,18,terrrain_group)
    ga.block(136,17,terrrain_group)
    ga.block(136,16,terrrain_group)
    ga.block(136,15,terrrain_group)
    ga.block(137,18,terrrain_group)
    ga.block(137,17,terrrain_group)
    ga.block(137,16,terrrain_group)
    ga.block(138,18,terrrain_group)
    ga.block(138,17,terrrain_group)
    ga.block(139,18,terrrain_group)



    ga.block(144,18,terrrain_group)
    ga.block(145,18,terrrain_group)
    ga.block(145,17,terrrain_group)
    ga.block(146,18,terrrain_group)
    ga.block(146,17,terrrain_group)
    ga.block(146,16,terrrain_group)
    ga.block(147,18,terrrain_group)
    ga.block(147,17,terrrain_group)
    ga.block(147,16,terrrain_group)
    ga.block(147,15,terrrain_group)
    ga.block(148,18,terrrain_group)
    ga.block(148,17,terrrain_group)
    ga.block(148,16,terrrain_group)
    ga.block(148,15,terrrain_group)


    ga.block(151,18,terrrain_group)
    ga.block(151,17,terrrain_group)
    ga.block(151,16,terrrain_group)
    ga.block(151,15,terrrain_group)
    ga.block(152,18,terrrain_group)
    ga.block(152,17,terrrain_group)
    ga.block(152,16,terrrain_group)
    ga.block(153,18,terrrain_group)
    ga.block(153,17,terrrain_group)
    ga.block(154,18,terrrain_group)

    ga.pipe(5088,1,terrrain_group)

    ga.brick(164,15,terrrain_group)
    ga.brick(165,15,terrrain_group)
    ga.question_block(166,15,1,1,terrrain_group)
    ga.brick(167,15,terrrain_group)

    ga.pipe(32*174,1,terrrain_group)
    

    for i in range(0,10) :
        for j in range(0,i):
            if not j == 8:
                ga.block(175+i,18-j,terrrain_group)

    

    ga.gold_flag(193*32-16,terrrain_group)
    ga.block(193,18,terrrain_group)

    ga.castle(197*32,terrrain_group)



            

    
    






    












    








    
    
    


    
    
    
    
    
    

    return terrrain_group


