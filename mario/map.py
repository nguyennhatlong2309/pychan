import pygame as pg
import game_assets as ga

y_floor= 14*32

def map1():
    print("tao map 1")
    object_group = pg.sprite.Group()

    ga.bg("new_bg1",0,0,object_group)
    ga.bg("new_bg1",1500,0,object_group)
    

    
    # ga.gold_flag(15*32-16,object_group)
    # tao san` 
    


    ga.brick(10,10,object_group)  

    ga.brick(19,10,object_group)
    ga.question_block(20,10,2,1,object_group)
    ga.brick(21,10,object_group)
    ga.question_block(21,6,2,1,object_group)
    ga.question_block(22,10,1,1,object_group)
    ga.brick(23,10,object_group)
    ga.pipe(27*32,1,object_group)
    #=============================================================================
    # ga.koopatroopa(32*30,y_floor-48,object_group)
    # ga.redkoopatroopa(25*32,y_floor-180,object_group)
    # ga.latiku(51*32,48,object_group)

    # ga.hammerBrother(32*51,8*32,object_group)
    # ga.create_multi_brick(5,49,10,object_group)

    # ga.create_multi_brick(5,49,7,object_group)
    
    #==============================================================
   

    ga.pipe(37*32,2,object_group)
    ga.goomba(1300,y_floor-32,object_group)
    ga.koopatroopa(1350,y_floor-48,object_group)
    ga.pipe(45*32,3,object_group)
    ga.goomba(58*27,y_floor-32,object_group)
    ga.goomba(1650,y_floor-32,object_group)
    ga.pipe(56*32,3,object_group)
 


    


    ga.brick(75,10,object_group)
    ga.question_block(76,10,2,1,object_group)
    ga.brick(77,10,object_group)
    
    
    for i in range(0,8):
        ga.brick(78+i,6,object_group)
    
    ga.goomba(80*32,y_floor-(32*9),object_group)
    ga.goomba(83*32,y_floor-(32*9),object_group)

    
    
    ga.floor(66*32,88*32,y_floor,object_group)
    ga.floor(66*32,88*32,y_floor+32,object_group)

    ga.create_multi_brick(3,90,6,object_group)
    ga.question_block(93,6,1,1,object_group)
    ga.brick(93,10,object_group)
    ga.create_multi_brick(2,99,10,object_group)

    ga.goomba(100*32,y_floor-32,object_group)

    


    ga.question_block(105,10,1,1,object_group)
    ga.question_block(108,10,1,1,object_group)
    ga.question_block(108,6,1,1,object_group)
    ga.question_block(111,10,1,1,object_group)

    ga.koopatroopa(108*32,y_floor-48,object_group)
    ga.goomba(112*32,y_floor-32,object_group)    

 

    ga.brick(117,10,object_group)                
    ga.create_multi_brick(3,120,6,object_group)
    
    ga.goomba(117*32,y_floor-32,object_group)  


    ga.brick(127,6,object_group)
    ga.brick(128,10,object_group)
    ga.brick(129,10,object_group)
    ga.brick(130,6,object_group)
    ga.question_block(128,6,1,1,object_group)
    ga.question_block(129,6,1,1,object_group)

    ga.goomba(32*128-10,y_floor-32,object_group)
    ga.goomba(32*129,y_floor-32,object_group)
    ga.goomba(32*132,y_floor-32,object_group)
    ga.goomba(32*133+10,y_floor-32,object_group)

       

    for i in range(0,4):
        for j in range(0,i+1):
            ga.block(135+i,13-j,object_group)

    for i in range(4,0,-1):
        for j in range(0,i):
            ga.block(145-i,13-j,object_group)

    

    for i in range(0,5):
        for j in range(0,i+1):
            if j != 4 :
                ga.block(149+i,13-j,object_group)

    

    ga.floor(2000,156*32,y_floor,object_group) 
    ga.floor(2000,156*32,y_floor+32,object_group) 

    for i in range(4,0,-1):
        for j in range(0,i):
            ga.block(160-i,13-j,object_group)


    ga.pipe(164*32,1,object_group)

    ga.brick(169,10,object_group)
    ga.brick(170,10,object_group)
    ga.question_block(171,10,1,1,object_group)
    ga.brick(172,10,object_group)

    ga.goomba(173*32,y_floor-32,object_group)
    ga.goomba(179*32,y_floor-32,object_group)


    ga.pipe(181*32,1,object_group) 

    for i in range(0,9):
        for j in range(0,i+1):
            if j != 8:
                ga.block(183+i,13-j,object_group)      
            
    ga.gold_flag(199*32,object_group)
    ga.block(199,13,object_group)

    ga.castle(204*32,object_group)


    ga.floor(10*32,69*32,y_floor,object_group)
    ga.floor(10*32,69*32,y_floor+32,object_group)
    
    ga.floor(67*32,0,y_floor,object_group)
    ga.floor(480,2270,y_floor,object_group)
    ga.floor(2000,2846,y_floor,object_group)

    ga.floor(67*32,0,y_floor+32,object_group)
    ga.floor(480,2270,y_floor+32,object_group)
    ga.floor(2000,2846,y_floor+32,object_group)

    return object_group

def map2():
    object_group = pg.sprite.Group()
    ga.bg("new_bg4",0,0,object_group)
    ga.bg("new_bg4",1500,0,object_group)

    
    
    ga.grass_terrace(19*32,y_floor-10,2,object_group)
    

    ga.grass_terrace(28*32,y_floor-(32*8),2,object_group)
    ga.grass_terrace(25*32,y_floor-(32*4),4,object_group)

    ga.redkoopatroopa(30*32,y_floor-(32*10),object_group)


    ga.grass_terrace(33*32,y_floor-(32*1),1,object_group)
    ga.static_coin(34*32,y_floor-(32*2),object_group)

    ga.grass_terrace(36*32,y_floor-(32*5),3,object_group)

    ga.grass_terrace(43*32,y_floor-(32*9),4,object_group)
    
    ga.static_coin(42*32,y_floor-(32*11),object_group)
    ga.static_coin(41*32,y_floor-(32*11),object_group)

    ga.goomba(51*32,y_floor-(32*10),object_group)
    ga.goomba(47*32,y_floor-(32*10),object_group)

    



    ga.grass_terrace(54*32,y_floor-(32*1),2,object_group)
    ga.static_coin(54*32,y_floor-(32*7),object_group)
    ga.static_coin(55*32,y_floor-(32*7),object_group)

    ga.moving_flat(60*32,y_floor-(32*4),3,2,1,object_group)




    ga.static_coin(67*32,y_floor-(32*9),object_group)
    ga.static_coin(68*32,y_floor-(32*9),object_group)
    ga.static_coin(69*32,y_floor-(32*9),object_group)
    ga.static_coin(70*32,y_floor-(32*9),object_group)
    ga.grass_terrace(67*32,y_floor-(32*8),2,object_group)
    ga.grass_terrace(65*32,y_floor-(32*1),3,object_group)

    ga.question_block(65,9,2,1,object_group)


    ga.grass_terrace(73*32,y_floor-(32*1),3,object_group)
    ga.grass_terrace(80*32,y_floor-(32*5),1,object_group)

    ga.redkoopaParatroopa(84*32,y_floor-(32*5),object_group)

    
    ga.grass_terrace(86*32,y_floor-(32*7),4,object_group)

    

    ga.moving_flat(98*32,y_floor-(32*6),3,1,1,object_group)
    ga.moving_flat(103*32,y_floor-(32*5),3,1,-1,object_group)
    

    ga.static_coin(99*32,y_floor-(32*8),object_group)
    ga.static_coin(100*32,y_floor-(32*8),object_group)

    ga.static_coin(107*32,y_floor-(32*9),object_group)
    ga.static_coin(108*32,y_floor-(32*9),object_group)

    ga.static_coin(111*32,y_floor-(32*9),object_group)
    ga.static_coin(112*32,y_floor-(32*9),object_group)

    ga.grass_terrace(112*32,y_floor-(32*2),2,object_group)
    ga.grass_terrace(116*32,y_floor-(32*4),1,object_group)

    ga.grass_terrace(119*32,y_floor-(32*7),4,object_group)
    ga.redkoopatroopa(123*32,y_floor-(32*9),object_group)
    

    ga.grass_terrace(129*32,y_floor-(32*1),1,object_group)
    ga.static_coin(129*32,y_floor-(32*2),object_group)
    ga.static_coin(130*32,y_floor-(32*2),object_group)
    ga.static_coin(131*32,y_floor-(32*2),object_group)

    ga.redkoopaParatroopa(130*32,y_floor-(32*7),object_group)


    ga.grass_terrace(132*32,y_floor-(32*5),2,object_group)

    ga.static_coin(136*32,y_floor-(32*9),object_group)
    ga.static_coin(137*32,y_floor-(32*9),object_group)

    ga.grass_terrace(138*32,y_floor-(32*5),2,object_group)

    ga.moving_flat(146*32,y_floor-(32*8),3,1,1,object_group).limit_possion_x = 128
    #===================================================================================

    
    

    ga.block(156,12,object_group)
    

    for i in range(0,6):
        for j in range(0,4):
            ga.block(156+i,13-j,object_group)

    for i in range(0,4):
        for j in range(0,2):
            ga.block(158+i,9-j,object_group)

    for i in range(0,2) :
        for j in range(0,2):
            ga.block(160+i,7-j,object_group)

    
    
    ga.create_multi_brick(4,176,5,object_group)

    ga.create_multi_brick(4,176,9,object_group)

    ga.hammerBrother(180*32,y_floor-48,object_group)

    ga.hammerBrother(179*32,y_floor-(32*5)-48,object_group)








    for i in range(0,6):
        for j in range(0,4):
            ga.block(186+i,13-j,object_group)

    for i in range(0,4):
        for j in range(0,2):
            ga.block(188+i,9-j,object_group)

    for i in range(0,2) :
        for j in range(0,2):
            ga.block(190+i,7-j,object_group)

    t=ga.gold_flag(210*32,object_group)
    t.rect.y-=32
    ga.block(210,13,object_group)
    ga.castle(215*32,object_group)

    
    ga.floor(16*32,0,y_floor,object_group)
    ga.floor(16*32,0,y_floor+32,object_group)

    ga.floor(3072,146*32,y_floor,object_group)
    ga.floor(3072,146*32,y_floor+32,object_group)














    


    



    

    







   
    


    

    
    

    


    return object_group

def map3():


    object_group = pg.sprite.Group()
    ga.bg("new_bg2",0,0,object_group)
    ga.bg("new_bg2",1500,0,object_group)
    
    ga.create_multi_brick(3,15,10,object_group)

    for i in range(0,5):
        for j in range(0,i+1):
            ga.block(20+i,13-j,object_group)
        
    ga.goomba(32*24,y_floor-(7*32),object_group)
    ga.create_multi_brick(3,29,6,object_group)

    ga.koopatroopa(28*32,y_floor-48,object_group)
    ga.koopatroopa(30*32,y_floor-48,object_group)

    for i in range(0,4):
        ga.block(34,13-i,object_group)
    ga.block(35,13,object_group)
    ga.block(35,12,object_group)

    
    ga.goomba(40*32,y_floor-32,object_group)
    ga.goomba(42*32,y_floor-32,object_group)
    
    ga.piranha_plant(47*32,y_floor-(32*4),object_group) 
    ga.pipe(46*32,3,object_group)

    for i in range(0,5) :
        ga.question_block(53+i,6,1,1,object_group)
        if i != 0 :
            ga.question_block(53+i,10,1,1,object_group)
   
    ga.question_block(53,10,2,1,object_group)

    ga.goomba(55*32,y_floor-32,object_group)
    ga.goomba(56*32+16,y_floor-32,object_group)

    ga.koopatroopa(68*32,y_floor-48,object_group)

    ga.goomba(70*32,y_floor-32,object_group)
    ga.goomba(71*32+16,y_floor-32,object_group)
    ga.goomba(73*32,y_floor-32,object_group)
    

    ga.brick(68,10,object_group)
    ga.create_multi_brick(4,69,6,object_group)
    
    ga.piranha_plant(76*32,y_floor-(32*4),object_group)
    ga.pipe(75*32,3,object_group)
    
    for i in range(0,4):
        ga.question_block(81+i,10,1,1,object_group)
    
    ga.create_multi_brick(5,83,6,object_group)

    for i in range(0,3):
        ga.question_block(87+i,10,1,1,object_group)

    ga.goomba(93*32,y_floor-32,object_group)
    ga.goomba(92*32-16,y_floor-32,object_group)
    ga.goomba(85*32,y_floor-32,object_group)
    ga.create_multi_brick(4,94,6,object_group)

    

    ga.piranha_plant(106*32,y_floor-(32*4),object_group)
    ga.pipe(105*32,3,object_group)
    ga.goomba(104*32,y_floor-32,object_group)

    

    ga.piranha_plant(119*32,y_floor-64,object_group)
    ga.pipe(118*32,1,object_group)

    ga.goomba(124*32,y_floor-32,object_group)

    ga.piranha_plant(126*32,y_floor-(32*4),object_group)
    ga.pipe(125*32,3,object_group)

    ga.create_multi_brick(4,128,6,object_group)

    ga.pipe(129*32,2,object_group)

    ga.piranha_plant(134*32,y_floor-(32*5),object_group)
    ga.pipe(133*32,4,object_group)

    ga.koopatroopa(141*32,y_floor-48,object_group)

    
    ga.koopaParatroopa(155*32,y_floor-48,object_group)

    

    for i in range(0,3):
        ga.block(158,13-i,object_group)
    
    ga.brick(165,10,object_group)

    ga.goomba(165*32,y_floor-32,object_group)
    ga.goomba(166*32+16,y_floor-32,object_group)

    ga.create_multi_brick(5,168,6,object_group)

    ga.question_block(174,10,1,1,object_group)
    ga.question_block(176,6,2,1,object_group)  

    ga.koopatroopa(174*32,y_floor-48,object_group)
    ga.koopatroopa(176*32,y_floor-48,object_group)

    ga.piranha_plant(181*32,y_floor-(32*3),object_group)
    ga.pipe(180*32,2,object_group)
    
    ga.create_multi_brick(2,189,10,object_group)
    ga.koopatroopa(189,y_floor-5,object_group)
    ga.question_block(190,6,1,1,object_group)

    for i in range(0,10):
        ga.block(194,13-i,object_group)
        ga.block(195,13-i,object_group)
    
    ga.gold_flag(204*32-16,object_group)
    ga.block(204,13,object_group)

    ga.castle(208*32,object_group)

    ga.floor(3008,0,y_floor,object_group)
    ga.floor(3008,0,y_floor+32,object_group)

    ga.floor(320,3136,y_floor,object_group)
    ga.floor(320,3136,y_floor+32,object_group)

    ga.floor(31*32,32*111,y_floor,object_group)
    ga.floor(31*32,32*111,y_floor+32,object_group)

    ga.floor(320,4640,y_floor,object_group)
    ga.floor(320,4640,y_floor+32,object_group)

    ga.floor(32*90,158*32,y_floor,object_group)
    ga.floor(32*90,158*32,y_floor+32,object_group)


    
    return object_group