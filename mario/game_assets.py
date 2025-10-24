import pygame as pg

y_floor = 32*19
class object(pg.sprite.Sprite):
    def __init__(self,image,x,y,object_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.velocity_y = 0
        self.velocity_x = 1
        self.direct = -1
        self.gravity = 0.2
        self.edge_left = 0
        self.edge_right = 0
        self.lose = False
        self.on_ground = False
        self.object_group = object_group
        self.object_group.add(self)

class castle(object):
    def __init__(self, x, object_group):
        image = pg.image.load("images/castle1.png")
        y = y_floor - image.get_height()
        super().__init__(image, x, y, object_group)

class gold_flag(object):
    def __init__(self, x, object_group):
        self.image = pg.image.load("images/gold flag.png")
        y = y_floor-self.image.get_height()
        super().__init__(self.image, x, y, object_group)        

class enemy(object):
    def __init__(self, image, x, y,object_group):
        super().__init__(image,x,y,object_group)
        self.status = 1
    def update(self):
        return  

class floor(object):
    def __init__(self,width,x, y,object_group):
        image = pg.image.load("images/grounds.png").subsurface(pg.Rect(0,0,width,32))
        super().__init__(image, x, y,object_group)
    def update(self):
        return  

class peace_brick(object):
    def __init__(self, x, y,direct,object_group):
        self.frame = [pg.image.load("images/peace_brick0.png"),
                      pg.image.load("images/peace_brick1.png"),
                      pg.image.load("images/peace_brick2.png"),
                      pg.image.load("images/peace_brick3.png")]
        
        super().__init__(self.frame[0], x, y, object_group)
        self.direct = direct
        self.time = 0
        self.velocity_y = -4
    
    def move_x(self):
        self.rect.x += self.direct

    def animation(self):
        self.time += 1
        if self.time >= 40 :
            self.time = 0
        self.image = self.frame[int(self.time/10)]
    def update(self):
        fall(self)
        self.move_x()
        self.animation()
        if self.rect.y > 664 :
            self.kill()

class brick(floor):
    def __init__(self,x, y,object_group):
        x*=32
        y*=32
        super().__init__(32,x,y,object_group)
        self.default_y = y 
        self.on_ground = True
    def pop_up(self):
        self.velocity_y = -2
        self.on_ground = False
    
    def destroy(self):
        peace_brick(self.rect.left,self.rect.top,-1,self.object_group)
        peace_brick(self.rect.left,self.rect.bottom,-1,self.object_group)
        peace_brick(self.rect.right,self.rect.top,1,self.object_group)
        peace_brick(self.rect.right,self.rect.bottom,1,self.object_group)
        self.kill()
        
    def fall(self):
        if not self.on_ground :
            self.rect.y += self.velocity_y
            self.velocity_y += self.gravity
        if self.rect.y > self.default_y : 
            self.on_ground = True
            self.rect.y = self.default_y
    def update(self):
        self.fall()

class block(brick):
    def __init__(self, x, y, object_group):
        super().__init__(x, y, object_group)
        self.image = pg.image.load("images/Block.png")

class pipe(floor):
    def __init__(self,x,type, object_group):
        type -=1
        self.frame =[pg.image.load("images/pipe0.png"),
                     pg.image.load("images/pipe1.png"),
                     pg.image.load("images/pipe2.png")]
        width = self.frame[type].get_width()
        y = y_floor-(self.frame[type].get_height())
        super().__init__(width, x, y,object_group)
        
        self.image = self.frame[type]
        self.rect = self.image.get_rect(topleft = self.rect.topleft)

class coin(object):
    def __init__(self, x, y, object_group):
        self.frame=[pg.image.load("images/coin0.png"),
                    pg.image.load("images/coin1.png"),
                    pg.image.load("images/coin2.png"),
                    pg.image.load("images/coin3.png")]
        super().__init__(self.frame[0], x, y, object_group)
        self.rect.centerx = x
        self.time = 0
        self.velocity_y = -7
        self.default_y = y+1
    def animation(self):
        self.time += 1
        if self.time >= 28 :
            self.time = 0
        self.image = self.frame[int(self.time/7)]
    
    def update(self):
        if self.rect.y > self.default_y :
            self.kill()
            
        self.animation()
        fall(self)

class super_mushroom(object):
    def __init__(self,parent, object_group):
        self.frame = pg.image.load("images/Super Mushroom.png")
        super().__init__(self.frame, parent.rect.x, parent.rect.y, object_group)
        self.direct = 1
        self.start_update = False
        self.rect.centerx = parent.rect.centerx
        self.parent = parent
    def move_x(self):
        self.rect.x += self.velocity_x*self.direct  
    
    def checkcollide(self):
        for object in self.object_group :
            if self.rect.colliderect(object.rect):
                if isinstance(object,floor) and object is not self:
                    if top_to(self,object):
                        self.edge_left =getEdgeL(object) 
                        self.edge_right =getEdgeR(object) 
                        self.rect.bottom = object.rect.top
                        self.on_ground = True
                        self.velocity_y = 0

                    elif bot_to(object,self):
                        self.rect.bottom = object.rect.top
                        self.velocity_y = -3
                        self.on_ground = False
                        if self.rect.centerx < object.rect.centerx :
                            self.direct *= -1
                    elif left_to(self,object) or right_to(self,object):
                        self.direct*=-1
                                            
    def update(self):
        if self.start_update:
            self.checkcollide()
            fall(self)
            self.move_x()
            
     
        else :
            if self.rect.colliderect(self.parent.rect):
                self.rect.y -= 1
            if self.rect.bottom <= self.parent.rect.top :
                self.start_update = True

class fire_flower(object):
    def __init__(self,parent, object_group):
        self.frame = [pg.image.load("images/Fire Flower0.png"),
                      pg.image.load("images/Fire Flower1.png"),
                      pg.image.load("images/Fire Flower2.png"),
                      pg.image.load("images/Fire Flower3.png")]
        super().__init__(self.frame[0], parent.rect.centerx, parent.rect.y, object_group)
        self.rect.centerx = parent.rect.centerx
        self.start_update = False 
        self.parent = parent
        self.direct = 1
        self.time = 0

    def animation(self):
        self.time +=1 
        if self.time >= 40 :
            self.time = 0
        self.image = self.frame[int(self.time/10)]
    def update(self):
        self.animation()
        if self.rect.colliderect(self.parent.rect):
            self.rect.y -= 1
        elif self.rect.bottom >= self.parent.rect.top:
                self.rect.bottom = self.parent.rect.top

class firebar(object):
    def __init__(self, x, y,direct,object_group):
        self.frame1= [ pg.image.load("images/Firebar0.png"),
                     pg.image.load("images/Firebar1.png"),
                     pg.image.load("images/Firebar2.png"),
                     pg.image.load("images/Firebar3.png"),]
        self.frame2 = [pg.image.load("images/Firework1.png"),
                       pg.image.load("images/Firework2.png"),
                       pg.image.load("images/Firework3.png"),]
        self.frame = self.frame1
        super().__init__(self.frame[0], x, y, object_group)
        self.direct = direct
        self.velocity_x = 6
        self.limit_time = 40
        self.time = 0
        self.collideLR = False

    def move(self):
        self.rect.x += self.velocity_x*self.direct
        
    def animation(self):
        try :
            self.time += 1
            if self.time >= self.limit_time:
                self.time = 0
            self.image = self.frame[int(self.time/10)]
        except  Exception as e :
            self.kill()
    
    
    def checkcollide(self):
        for object in self.object_group : 
            if self.rect.colliderect(object.rect) and object is not self and not isinstance(object,firebar):
                if isinstance(object,floor):
                    if top_to(self,object):
                        self.velocity_y = -3
                    elif right_to(self,object) or left_to(self,object):
                        self.velocity_y = 0
                        self.velocity_x = 0
                        self.time = 0
                        self.frame = self.frame2
                        self.collideLR = True
                if not isinstance(object,(Mario,floor)):
                    object.status = 1
                    over(object)
                    self.velocity_y = 0
                    self.velocity_x = 0
                    self.time = 0
                    self.frame = self.frame2
                    self.collideLR = True
    
    def update(self):
        if not self.collideLR :
            self.checkcollide()
            self.move()
            fall(self)
            
        self.animation()
        
class question_block(brick):
    def __init__(self, x, y,award,stock, object_group):
        super().__init__(x, y, object_group)
        self.frame = [pg.image.load("images/Question Block0.png"),
                      pg.image.load("images/Question Block1.png"),
                      pg.image.load("images/Question Block2.png"),
                      pg.image.load("images/Empty Block.png")]
        self.image = self.frame[0]
        self.time = 0
        self.award = award
        self.stock = stock
    def animation(self):
        if self.stock > 0 :
            self.time += 1
            if self.time >= 30 :
                self.time = 0
            self.image = self.frame[int(self.time/10)]
        else : 
            self.image = self.frame[3]
    
    def reset_position(self):
        self.object_group.remove(self)
        self.object_group.add(self)

    def createCoin(self):
        # if self.stock > 0 :
        #     self.stock -= 1
            coin(self.rect.centerx,self.rect.y,self.object_group)
            self.reset_position()

    def createMushroom(self):
        super_mushroom(self,self.object_group)
        self.reset_position() 

    def create_fireflower(self):
        fire_flower(self,self.object_group)
        self.reset_position() 

    def create(self,object):
        if self.stock > 0 :
            self.stock -=1
            if self.award == 1:
                self.createCoin()
            else : 
                if object.status == 1:
                    self.createMushroom()
                else : 
                    self.create_fireflower()                  
    def update(self):
        if not self.image == self.frame[3] :
            self.animation()

class goomba(enemy):  
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/Goomba_frame_0.png"),pg.image.load("images/Goomba_frame_1.png")]
        super().__init__(self.frame[0], x, y,object_group)
        self.time = 0
        
        
    def over(self):
        self.on_ground = False
        self.lose = True
        self.velocity_y -=1

    def checkcollide(self):
        for object in self.object_group:
            if self.rect.colliderect(object.rect) and object is not self:
                if isinstance(object,floor):
                    if top_to(self,object):
                       self.edge_left = getEdgeL(object) 
                       self.edge_right = getEdgeR(object) 
                       self.on_ground = True
                       self.velocity_y = 0
                       self.rect.bottom = object.rect.top

                    if right_to(self,object) or left_to(self,object):
                        self.direct *= -1
                elif not isinstance(object,(Mario,hit_box,firebar,super_mushroom)):
                   if right_to(self,object) or left_to(self,object):
                       self.direct*=-1
                       object.direct *= -1
                   
                        
                       

                

    def animation(self):
        self.time +=1
        if self.time >= 20 :
            self.time = 0
        self.image = self.frame[int(self.time/10)]
    
    def move(self):
        self.rect.x += self.velocity_x * self.direct
        
    def update(self):
        if not self.lose :
            self.checkcollide()
            self.animation()
            self.move()
        fall(self)

class hit_box(object): 
    def __init__(self, image, x, y,object_group):
        super().__init__(image, x, y,object_group)
        self.object_group = object_group
        self.object_group.add(self)
    def checkcollide(self):
        for object in self.object_group:
            if isinstance(object,Mario):
                if self.rect.colliderect(object.rect):
                    object.downGrade()

class koopatroopa(enemy): # ok 
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/greenKoopaParatroopa0.png"),#1
                    pg.image.load("images/greenKoopaParatroopa1.png"),#2
                    pg.image.load("images/greenKoopaTroopa0.png"),#3
                    pg.image.load("images/greenKoopaTroopa1.png"),#4
                    pg.image.load("images/greenKoopaTroopa4.gif"),#5
                    pg.image.load("images/greenKoopaTroopa2.png"),#6
                    pg.image.load("images/greenKoopaTroopa3.png"),#7
                    pg.image.load("images/greenKoopaParatroopa2.png"),#7
                    pg.image.load("images/greenKoopaParatroopa3.png")]#8
        super().__init__(self.frame[0], x, y,object_group)
        self.status = 3
        self.velocity_y = -1
        self.time = 0
        self.velocity_x = 1
        

    def move_x(self):
        self.rect.x += self.direct * self.velocity_x

            
    def checkcollide(self):
        if not self.lose:  # update vi tri cua rua xanh 
            for object in self.object_group :
                if self.rect.colliderect(object.rect) and object is not self:
                    
                    if self.status == 1:
                        if isinstance(object,Mario):

                            if (left_to(self,object) or right_to(self,object)) and object.lose == False:
                                object.status = 0
                                over(object)

                    elif self.status == 2:
                        if isinstance(object,Mario):
                            self.direct = 1 if right_to(self,object) else -1
                        
                    elif top_to(self,object):
                        if self.status == 4 :
                            self.velocity_y = -7
                            self.on_ground = False
                        else :
                            self.rect.bottom = object.rect.top
                            self.velocity_y = 0
                            self.on_ground = True
                            self.edge_left = getEdgeL(object) 
                            self.edge_right = getEdgeR(object)
                            self.velocity_x = 1
                        
                        
                    if (left_to(self,object) or right_to(self,object)) and not isinstance(object,Mario):
                        self.direct *= -1
                        self.rect.x += self.direct
                    if bot_to(self,object):
                        self.rect.top = object.rect.bottom
                        self.velocity_y = 0
    def update(self):
        if self.status == 4 :
            self.time +=1
            if self.time >= 20 :
                self.time = 0
            
            self.image = self.frame[int(self.time/10+3)*self.direct +4]
        elif self.status == 3:
            self.time +=1
            if self.time >= 20:
                self.time = 0
            self.image = self.frame[int(self.time/10+1)*self.direct+4]
        else : 
            self.image = self.frame[4]
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
            self.velocity_x = 5 if self.status == 1 else 0
            
                 
        

        self.checkcollide()           
        self.move_x()
        fall(self)

class koopaParatroopa(koopatroopa): # ok
    def __init__(self, x, y, object_group):
        
        super().__init__(x, y, object_group)
        self.status = 4
    
    def update(self):
        return super().update()

class hammerBrother(enemy):#ok
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/Hammer Brother - Throw1.gif"),
                      pg.image.load("images/Hammer Brother - Throw2.gif"),
                      pg.image.load("images/Hammer Brother.gif")]
        super().__init__(self.frame[2],x,y,object_group)
        self.time = 0
        self.status = 0 
        self.default_x = x
        self.velocity_x = 1
        self.count_down_hammer = 0
        self.count_down_jump = 0
        self.count_down_combo = 0
        self.attack = False
    def move_x(self):
        if abs(self.rect.x - self.default_x) > 100 :
            self.direct *= -1
        self.rect.x += self.velocity_x * self.direct

    def jump(self):
        self.count_down_jump += 1
        if self.count_down_jump >= 170 :
            self.count_down_jump = 0
            self.velocity_y =-8 
            self.on_ground = False
    def checkcollide(self):
        if not self.lose:
            for object in self.object_group :
                if self.rect.colliderect(object.rect) and object is not self :
                    if isinstance(object,floor):
                        if top_to(self,object):
                            self.on_ground = True
                            self.velocity_y = 0
                            self.rect.bottom = object.rect.top
                            self.edge_left = getEdgeL(object) 
                            self.edge_right = getEdgeR(object)

    def animation(self):
        self.time += 1
        if self.time >=20:
            self.time = 0
        self.status = 0 if self.attack else 1
        self.image = self.frame[int(self.time/10)+self.status]
        
        
    
    def throw(self):
        self.count_down_combo += 1
        self.count_down_hammer += 1
        if self.count_down_combo >= 200 and not self.attack:
            self.count_down_combo = 0
            self.attack = True if not self.attack else False
        
        if self.count_down_combo >= 50 and self.attack :
            self.attack = False
        if self.count_down_hammer >= 20 and self.attack:
            self.count_down_hammer =0
            hammer(self.rect.x,self.rect.y,self.object_group)
        
    def update(self):
        self.throw()
        self.animation()
        self.checkcollide()
        self.move_x()
        self.jump()
        fall(self)
        
class hammer(hit_box): # ok 
    def __init__(self, x, y, object_group):
        self.frame =[pg.image.load("images/Hammer0.gif"),
                     pg.image.load("images/Hammer1.gif"),
                     pg.image.load("images/Hammer2.gif"),
                     pg.image.load("images/Hammer3.gif")]
        super().__init__(self.frame[0], x, y, object_group)
        self.velocity_y = -5
        self.velocity_x = -3 
        self.time = 0
    

    def animation(self):
        self.time += 1 
        if self.time >= 40 :
            self.time = 0
        self.image = self.frame[int(self.time/10)]
    
    def update(self):
        super().checkcollide()
        self.animation()
        self.rect.x += self.velocity_x
        if self.rect.y > 600 : 
            self.kill()
        fall(self)

class latiku(enemy):
    def __init__(self, x, y,object_group):
        self.frame=[pg.image.load("images/Lakitu1.gif"),
                    pg.image.load("images/Lakitu2.gif")]
        
        super().__init__(self.frame[0], x, y,object_group) 
        self.velocity_x = 1
        self.gravity = 0.2
        self.acceleration = 0.2
        self.default_x = x
        self.count_down_throw = 0

    def move_x(self):
        for object in self.object_group :
            if isinstance(object,Mario):
                self.default_x = object.rect.x
            
        if abs(self.rect.x - self.default_x) < 100 :
            self.count_down_throw += 1
            

            if self.velocity_x >= 3:  # truong hop LAKITU dang o gan mario 
                self.velocity_x = 3
            if self.velocity_x <= -3 :
                self.velocity_x = -3

        if self.velocity_x >= 6 :  # LAKITU khong o gan mario thi tang van toc 
            self.velocity_x = 6
        if self.velocity_x <= -6:
            self.velocity_x = -6
        
         
        if self.rect.x < self.default_x -100 : 
            self.direct = 1
        if self.rect.x > self.default_x +100 :
            self.direct = -1

        self.velocity_x += self.direct*self.acceleration 
        
        self.rect.x += self.velocity_x
    
    def throw(self):
        if self.count_down_throw >= 130:
            self.image = self.frame[1]
        if self.count_down_throw >= 150:
            self.count_down_throw = 0
            spiny_egg(self.rect.x,self.rect.y,self.object_group)
            self.image = self.frame[0]
        
    

    def update(self):
        self.throw()
        self.move_x()

class spiny_egg(enemy):
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/Spiny Egg0.png"),
                      pg.image.load("images/Spiny Egg1.png"),
                      pg.image.load("images/Spiny0.png"),
                      pg.image.load("images/Spiny1.png"),
                      pg.image.load("images/Spiny2.png"),
                      pg.image.load("images/Spiny3.png")]
        super().__init__(self.frame[0], x, y,object_group)
        self.time = 0
        self.status = 2 
        self.velocity_x = 1
        self.landmark = x
        self.first_on_ground = True

    
    def move_x(self):
        if self.status == 2 or self.status == 0:
            self.velocity_x = 0
        if self.status == 1 :
            self.velocity_x = self.direct 
        self.rect.x += self.velocity_x

    def move_y(self):
        if self.status == 2 :
            self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

    def animation(self):
        self.time += 1
        if self.time >= 20 : 
            self.time = 0 
        if self.status == 2 :
            self.image = self.frame[int(self.time/10)]
        if self.status == 1 :
            if self.direct == -1 :
                self.image = self.frame[int(self.time/10)+2]
            else :
                self.image = self.frame[int(self.time/10)+4]


    def checkcollide(self):
        if not self.lose :
            
            for object in self.object_group : 
                if isinstance(object,Mario):
                    self.landmark = object.rect.x
                    if self.rect.colliderect(object.rect):
                        over(object)
                    break
            for object in self.object_group :
                if isinstance(object,enemy):
                    if self.rect.colliderect(object.rect) and self is not object:
                        if top_to(self,object):
                            self.direct *= -1
                            object.direct *= -1
                        if left_to(self,object) and self.velocity_x > 0:
                            self.direct *= -1
                            object.direct *= -1

                        if right_to(self,object) and self.velocity_x < 0:
                            self.direct *= -1
                            object.direct *= -1

                           
                           
                        

            for object in self.object_group : 
                if isinstance(object,floor):
                    if self.rect.colliderect(object.rect):
                        if top_to(self,object):
                            self.status = 1
                            self.velocity_y = 0
                            self.on_ground = True
                            self.rect.bottom = object.rect.top
                            self.edge_left = getEdgeL(object) 
                            self.edge_right = getEdgeR(object) 
                            if self.first_on_ground :
                                self.first_on_ground = False
                                self.direct = 1 if self.rect.x < self.landmark else -1
                        elif right_to(self,object) or left_to(self,object):
                            self.direct *= -1
                            self.rect.x += self.direct
                            
                        
    def update(self):
        self.checkcollide()
        self.animation()
        self.move_x()
        fall(self)
        if self.rect.x < self.landmark - 1000 or self.rect.y > 700:
            self.kill()
     
class Mario(object):
    
    def __init__(self, x, y,object_group):

        self.frame1 = [pg.image.load("images/MarioR.png"),#0
                      pg.image.load("images/MarioJR.png"),#1
                      pg.image.load("images/MarioWR1.png"),#2
                      pg.image.load("images/MarioWR2.png"),#3
                      pg.image.load("images/MarioWR3.png"),#4
                      pg.image.load("images/MarioL.png"),#5
                      pg.image.load("images/MarioJL.png"),#6
                      pg.image.load("images/MarioWL1.png"),#7
                      pg.image.load("images/MarioWL2.png"),#8
                      pg.image.load("images/MarioWL3.png"),#9
                      pg.image.load("images/MarioSR.png"),#10
                      pg.image.load("images/MarioSL.png"),]#11
        
        self.frame2 = [pg.image.load("images/SuperMarioR.png"),#0
                      pg.image.load("images/SuperMarioJR.png"),#1
                      pg.image.load("images/SuperMarioWR1.png"),#2
                      pg.image.load("images/SuperMarioWR2.png"),#3
                      pg.image.load("images/SuperMarioWR3.png"),#4
                      pg.image.load("images/SuperMarioL.png"),#5
                      pg.image.load("images/SuperMarioJL.png"),#6
                      pg.image.load("images/SuperMarioWL1.png"),#7
                      pg.image.load("images/SuperMarioWL2.png"),#8
                      pg.image.load("images/SuperMarioWL3.png"),#9
                      pg.image.load("images/SuperMarioSR.png"),#10
                      pg.image.load("images/SuperMarioSL.png"),]#11
        
        self.frame3 = [pg.image.load("images/FieryMarioR.png"),#0
                      pg.image.load("images/FieryMarioJR.png"),#1
                      pg.image.load("images/FieryMarioWR1.png"),#2
                      pg.image.load("images/FieryMarioWR2.png"),#3
                      pg.image.load("images/FieryMarioWR3.png"),#4
                      pg.image.load("images/FieryMarioL.png"),#5
                      pg.image.load("images/FieryMarioJL.png"),#6
                      pg.image.load("images/FieryMarioWL1.png"),#7
                      pg.image.load("images/FieryMarioWL2.png"),#8
                      pg.image.load("images/FieryMarioWL3.png"),#9
                      pg.image.load("images/FieryMarioSR.png"),#10
                      pg.image.load("images/FieryMarioSL.png"),]#11
        
        self.frame_change = [pg.image.load("images/Mario_between_changeR.png"),
                             pg.image.load("images/Mario_between_changeL.png")]
        self.frame = self.frame1
        super().__init__(self.frame[0],x,y,object_group)
        self.velocity_x = 0
        self.power_jump = 8
        self.are_going = False
        self.status = 1 
        self.direct = 1
        self.press_up = False
        self.can_press_up = True
        self.last_jump = 0
        self.jump_countdown = 0

        self.countdown_firebar = 10

        self.status = 1
        #  of animation 
        self.time = 0
        self.current_time = 0
        self.begin_up_grade = 0
        self.are_going = False
        self.upgrade = False
        self.upgrade_time = 0
        self.blink = False
        self.blink_time = 0
        self.time_limit_blink = 200
        self.downgrade = False
    
    def jump(self):
        if (self.on_ground and self.jump_countdown <=0):  
            self.on_ground=False
            self.last_jump = self.current_time
            self.velocity_y =-self.power_jump

    def slip(self):
        if not self.are_going and self.velocity_x!=0: 
            direct = 1 if self.velocity_x < 0 else -1 
            self.velocity_x += self.gravity*direct
        if abs(self.velocity_x) <= 0.1:
            self.are_going = False
            
        self.rect.x += self.velocity_x
 
    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0
    
    def check_collide(self):
        if self.lose :
            return
        for object in self.object_group:
            if self.rect.colliderect(object.rect) and object is not self:
                if isinstance(object,floor):
                    if top_to(self,object)and not (left_to(self,object) or right_to(self,object)):
                        self.edge_left = getEdgeL(object) 
                        self.edge_right = getEdgeR(object) 
                        self.velocity_y = 0
                        self.on_ground = True
                        self.rect.bottom = object.rect.top
                        self.jump_countdown = 10
                    elif left_to(self,object):
                        self.rect.right = object.rect.left
                        self.velocity_x = 0

                    elif right_to(self,object):
                        self.rect.left = object.rect.right
                        self.velocity_x = 0
                        
                    elif bot_to(self,object) and not (left_to(self,object) or right_to(self,object)):
                        if isinstance(object,question_block):
                            object.create(self)
                        else :
                            if self.status == 1 :
                                object.pop_up()
                            else :
                                object.destroy()
                                
                        self.velocity_y = 0
                        self.rect.top = object.rect.bottom+1
                        
                if isinstance(object,enemy):
                    if top_to(self,object) and not isinstance(object,spiny_egg):
                        over(object)
                        self.velocity_y= -3
                        self.rect.bottom = object.rect.top
                        print("giet dich")
                    else :
                        print("bi ha")
                        if not (isinstance(object,koopatroopa) and object.status == 2):
                            if self.status > 1:
                                self.downGrade()
                            else :
                                over(self)
                    

                if isinstance(object,(super_mushroom,fire_flower)):
                    self.upgrade = True
                    object.kill()
    
    def move_x(self):
        self.are_going = True
        if self.velocity_x < 3 and self.velocity_x > -3:
            self.velocity_x += 0.15*self.direct
        else :
            self.velocity_x = 3*self.direct
        
    def be_blink(self):
        self.blink = True
     
    def be_hit(self):
        if self.status > 1 :
            self.status = 1
  
    def animation(self):
        self.time+=1
        if self.time >= 30 :
            self.time = 0
        if not self.on_ground :
            self.image = self.frame[1] if self.direct == 1 else self.frame[6]
        else:
            if self.are_going:
                if self.velocity_x > 0 and self.direct == -1 :
                    self.image = self.frame[10]
                elif self.velocity_x < 0 and self.direct == 1:
                    self.image = self.frame[10]
                else :
                    stt = 2 if self.direct == 1 else 7
                    self.image = self.frame[int(self.time/10)+stt]
            else :
                self.image = self.frame[0] if self.direct == 1 else self.frame[5]
            
        if self.upgrade :
            self.upgrade_time+=1
            self.upgrade_time = 0 if self.upgrade_time >= 57 else self.upgrade_time
            self.upGrade()

        if self.countdown_firebar > 0 :
            self.countdown_firebar -=1
            self.image = self.frame3[2] if self.direct == 1 else self.frame3[7]

        if self.blink :
            self.blink_time += 1
            self.Blink()
            
        if self.downgrade :
            self.downGrade()
            
    def change_image(self,img):
        bottomleft = self.rect.bottomleft
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.bottomleft = bottomleft

    def Blink(self):
        if int(self.blink_time/10)%2 == 0 :
            self.image = self.image.copy()
            self.image.set_alpha(0)
        else :
            self.image.set_alpha(255)
            
        if self.blink_time >= self.time_limit_blink :
            self.blink = False
            self.blink_time = 0
            self.image.set_alpha(255)

    def downGrade(self):
        self.downgrade = True
        self.be_blink()
        if self.blink_time >= 40:
            self.downgrade = False
            self.status = 1
            self.change_image(self.frame1[0])
            self.frame = self.frame1
        
    def upGrade(self):
        if self.status == 1 :
            direct = 0 if self.direct == 1 else 1
            image = self.frame2[0] if self.direct == 1 else self.frame2[5]
            if self.upgrade_time < 8 :
                return 
            elif self.upgrade_time < 16 : 
                self.change_image(self.frame_change[direct])

            elif self.upgrade_time < 24 :
                if self.direct == 1 :
                    self.change_image(self.frame1[0])
                else :
                    self.change_image(self.frame1[5])

            elif self.upgrade_time < 32 :
                self.change_image(self.frame_change[direct])
            
            elif self.upgrade_time < 40 :
                self.change_image(image)
            
            elif self.upgrade_time < 48 :
                self.change_image(self.frame_change[direct])
            
            elif self.upgrade_time < 56 :
                
                self.change_image(image)
                
            else :
                self.upgrade = False 
                self.upgrade_time = 0
                self.frame = self.frame2
                self.status = 2

        elif self.status == 2 :
            self.frame = self.frame3
            self.status = 3
            self.upgrade = False  
             
    def update(self,keys):

        self.jump_countdown-=1
        self.press_up = False
        
        if not self.upgrade and not self.downgrade: 
            if keys[pg.K_RIGHT] and not keys[pg.K_LEFT]:
                self.direct = 1
                self.move_x()
        
            if keys[pg.K_LEFT] and not keys[pg.K_RIGHT]:
                self.direct = -1
                self.move_x()

            if keys[pg.K_UP]:
                self.press_up = True
                self.jump()

            if keys[pg.K_c]:
                if self.status == 3 and self.countdown_firebar <= 0:
                    self.countdown_firebar = 10
                    if self.direct == 1 :
                        firebar(self.rect.right,self.rect.centery,self.direct,self.object_group)
                    else :
                        firebar(self.rect.left,self.rect.centery,self.direct,self.object_group)
            fall(self)
            self.slip()
        if not self.blink:
            self.check_collide()
               
        self.animation()
            
def top_to(self,object):
        if self.rect.top < object.rect.top and self.rect.bottom < object.rect.bottom and self.velocity_y > 0 and self.rect.bottom - object.rect.top <= self.velocity_y+1:
            return True
        return False

def bot_to(self,object):
            if self.rect.top > object.rect.top and self.rect.bottom > object.rect.top and self.rect.top < object.rect.bottom and self.velocity_y <0 and object.rect.bottom - self.rect.top <= abs(self.velocity_y)+1:
                return True
            return False
        
def left_to(self,object):
        if self.rect.left < object.rect.left and self.rect.right < object.rect.right and abs(self.rect.right - object.rect.left) <= abs(self.velocity_x)+1 : 
            return True
        return False

def right_to(self,object):
        if self.rect.left > object.rect.left and self.rect.right > object.rect.right and abs(self.rect.left - object.rect.right) <= abs(self.velocity_x)+1 :
            return True
        return False

def fall(self):
    if self.rect.left > self.edge_right or self.rect.right < self.edge_left :
        self.on_ground = False
    if not self.on_ground :
        self.rect.y += self.velocity_y
        self.velocity_y += self.gravity
        if self.velocity_y > 5:
            self.velocity_ = 5
    else :
        self.velocity_y = 0
    
def over(self):
    if not self.lose :
        self.lose = True
        self.on_ground = False
        self.velocity_y =-3 if isinstance(self,Mario) else 0 
        self.velocity_x =0 

def getEdgeR(self):
        for object in self.object_group :
            if isinstance(object,floor) and object.rect.left == self.rect.right and self.rect.y == object.rect.y:
                return getEdgeR(object)
        return self.rect.right

def getEdgeL(self):
        for object in self.object_group :
            if isinstance(object,floor) and self.rect.left == object.rect.right and self.rect.y == object.rect.y:
                return getEdgeL(object)
        return self.rect.left
    
