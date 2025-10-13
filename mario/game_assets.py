import pygame as pg
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

class brick(object):
    def __init__(self,x, y,object_group):
        image = pg.image.load("images/brick.gif")
        x*=32
        y*=32
        super().__init__(image,x,y,object_group)
        
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
                       self.edge_left = object.rect.left
                       self.edge_right = object.rect.right
                       self.on_ground = True
                       self.velocity_y = 0
                       self.rect.bottom = object.rect.top

                    if right_to(self,object) or left_to(self,object):
                        self.direct *= -1
                        
                       

                

    def animation(self):
        self.time +=1
        if self.time >= 70 :
            self.time = 0
        self.image = self.frame[int(self.time/35)]
    
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
                if self.rect.colliderect(object):
                    over(object)

class koopatroopa(enemy): # ok 
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/greenKoopaParatroopa0.png"),
                    pg.image.load("images/greenKoopaParatroopa1.png"),
                    pg.image.load("images/greenKoopaTroopa0.png"),
                    pg.image.load("images/greenKoopaTroopa1.png"),
                    pg.image.load("images/greenKoopaTroopa4.gif"),
                    pg.image.load("images/greenKoopaTroopa2.png"),
                    pg.image.load("images/greenKoopaTroopa3.png"),
                    pg.image.load("images/greenKoopaParatroopa2.png"),
                    pg.image.load("images/greenKoopaParatroopa3.png")]
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
                if self.rect.colliderect(object) and object is not self:
                    
                    if self.status == 1:
                        print(self.status,left_to(self,object) , right_to(self,object))
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
                            self.edge_left = object.rect.left
                            self.edge_right = object.rect.right
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
            if self.time >= 70 :
                self.time = 0
            
            self.image = self.frame[int(self.time/35+3)*self.direct +4]
        elif self.status == 3:
            self.time +=1
            if self.time >= 70:
                self.time = 0
            self.image = self.frame[int(self.time/35+1)*self.direct+4]
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
                if self.rect.colliderect(object) and object is not self :
                    if isinstance(object,floor):
                        if top_to(self,object):
                            self.on_ground = True
                            self.velocity_y = 0
                            self.rect.bottom = object.rect.top
                            self.edge_left = object.rect.left 
                            self.edge_right = object.rect.right

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
                    if self.rect.colliderect(object):
                        over(object)
                    break
            for object in self.object_group :
                if isinstance(object,enemy):
                    if self.rect.colliderect(object) and self is not object:
                        if top_to(self,object):
                            self.direct *= -1
                            object.direct *= -1
                        if left_to(self,object) and self.velocity_x > 0:
                            self.direct *= -1
                            object.direct *= -1
                            print(self.velocity_x)
                        if right_to(self,object) and self.velocity_x < 0:
                            self.direct *= -1
                            object.direct *= -1

                           
                           
                        

            for object in self.object_group : 
                if isinstance(object,floor):
                    if self.rect.colliderect(object):
                        if top_to(self,object):
                            self.status = 1
                            self.velocity_y = 0
                            self.on_ground = True
                            self.rect.bottom = object.rect.top
                            self.edge_left = object.rect.left
                            self.edge_right = object.rect.right
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
        self.right = pg.image.load("images/Mario.png")
        self.left_img = pg.image.load("images/Mario_Left.png")
        self.jump_img =pg.image.load("images/Mario_jump.gif")
        self.walking_right1 = pg.image.load("images/Mario_Walking1.png")
        self.walking_right2 = pg.image.load("images/Mario_Walking2.png")
        self.walking_left1 = pg.image.load("images/Mario_Walking_Left1.png")
        self.walking_left2 = pg.image.load("images/Mario_Walking_Left2.png")
        self.animation_left = [self.left_img,self.walking_left1,self.walking_left2]
        super().__init__(self.right,x,y,object_group)
        self.velocity_x = 0
        self.power_jump = 8
        self.are_going = False
        self.status = 1 
        self.direct = 1
        
        self.last_changes = 0
        self.current_time = 0
        self.last_jump = 0

    def jump(self):
        self.image = self.jump_img
        if self.on_ground and self.current_time - self.last_jump > 500: 
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
                    
                    if left_to(self,object):
                        
                        self.rect.right = object.rect.left
                        self.velocity_x = 0

                    if right_to(self,object):
                        self.rect.left = object.rect.right
                        self.velocity_x = 0
                        

                    if top_to(self,object)and not (left_to(self,object) or right_to(self,object)):
                        self.edge_left = object.rect.left
                        self.edge_right = object.rect.right
                        self.velocity_y = 0
                        self.on_ground = True
                        self.rect.bottom = object.rect.top
                        
                       
                    
                    if bot_to(self,object) and not (left_to(self,object) or right_to(self,object)):
                        self.velocity_y = 0
                        self.rect.top = object.rect.bottom+1
                        


                if isinstance(object,enemy) and not isinstance(object,spiny_egg):
                    if top_to(self,object):
                        object.status-=1 
                        self.velocity_y = -3
                        self.rect.bottom = object.rect.top
                        if object.status <= 0 :
                            over(object)
                            

                    if right_to(self,object) or left_to(self,object) and not top_to(self,object):
                        if isinstance(object,koopatroopa) and not object.status == 2:
                            over(self)

                    
                   

           
    def move_x(self):
        self.are_going = True
        if self.velocity_x < 3 and self.velocity_x > -3:
            self.velocity_x += 0.5*self.direct
        
        else :
            self.velocity_x = 3*self.direct
        
    def update(self,keys):

        if keys[pg.K_RIGHT] :
            self.direct = 1
            self.move_x()
        
        if keys[pg.K_LEFT]:
            self.direct = -1
            self.move_x()

        if keys[pg.K_UP]:
            self.jump()
        self.check_collide()
        self.slip()
        fall(self)
        
def top_to(self,object):
        if self.rect.top < object.rect.top and self.rect.bottom < object.rect.bottom and self.velocity_y > 0 and self.rect.bottom - object.rect.top <= self.velocity_y+1:
            return True
        return False

def bot_to(self,object):
            if self.rect.top > object.rect.top and self.rect.bottom > object.rect.top and self.rect.top < object.rect.bottom and self.velocity_y <0 and object.rect.bottom - self.rect.top <= abs(self.velocity_y):
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