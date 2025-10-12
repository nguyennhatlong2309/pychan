import pygame as pg
class object(pg.sprite.Sprite):
    def __init__(self,image,x,y):
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
        
    
    


class enemy(object):
    def __init__(self, image, x, y):
        super().__init__(image,x,y)
        self.status = 1
    def update(self):
        return  

class floor(object):
    def __init__(self,width,x, y):
        image = pg.image.load("images/grounds.png").subsurface(pg.Rect(0,0,width,32))
        super().__init__(image, x, y)
    def update(self):
        return  
class brick(object):
    def __init__(self,x, y):
        image = pg.image.load("images/brick.gif")
        x*=32
        y*=32
        super().__init__(image,x,y)

class goomba(enemy): # ok
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/Goomba_frame_0.png"),pg.image.load("images/Goomba_frame_1.png")]
        super().__init__(self.frame[0], x, y)
        self.object_group = object_group
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
        super().__init__(image, x, y)
        self.object_group = object_group
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
        super().__init__(self.frame[0], x, y)
        self.status = 4
        self.velocity_y = -1
        self.time = 0
        self.object_group = object_group
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
                            self.velocity_y = -5
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


class hammerBrother(enemy):
    def __init__(self, x, y,object_group):
        self.frame = [pg.image.load("images/Hammer Brother - Throw1.gif"),
                      pg.image.load("images/Hammer Brother - Throw2.gif"),
                      pg.image.load("images/Hammer Brother.gif")]
        super().__init__(self.frame[2],x,y)
        self.object_group = object_group
        self.time = 0
        self.status = 2 
        self.default_x = x
        self.velocity_x = 1
        self.d = 1
        self.count_down = 0
        self.count_down_hammer = 0
        
    def move_x(self):
        if abs(self.rect.x - self.default_x) > 200 :
            self.direct *= -1
        self.rect.x += self.velocity_x * self.direct

    def jump(self):
        self.velocity_y =-8 
        self.on_ground = False
    def checkcollide(self):
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
        self.count_down +=1
        self.time += 1
        if self.time >=20:
            self.time = 0
            
        self.image = self.frame[int(self.time/10)+self.d]
        if self.count_down == 100 :
            self.count_down = 0
            self.d = 0 if self.d == 1 else 1
            self.jump()
        
    def throw(self):
        self.count_down_hammer += 1
        if self.count_down_hammer >= 100 :
            self.count_down_hammer = 0
            Hammer = hammer(self.rect.x,self.rect.y,self.object_group)
            self.object_group.add(Hammer)
        

            
        
    def update(self):
        self.throw()
        self.animation()
        self.checkcollide()
        self.move_x()
        fall(self)
        
class hammer(hit_box): # ok 
    def __init__(self, x, y, object_group):
        self.frame =[pg.image.load("images/Hammer0.gif"),
                     pg.image.load("images/Hammer1.gif"),
                     pg.image.load("images/Hammer2.gif"),
                     pg.image.load("images/Hammer3.gif")]
        super().__init__(self.frame[0], x, y, object_group)
        self.velocity_y = -5
        self.velocity_x = -2 
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
        super().__init__(self.right,x,y)
        self.velocity_x = 0
        self.power_jump = 8
        self.are_going = False
        self.status = 1 
        self.direct = 1
        self.object_group = object_group
        
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
                        


                if isinstance(object,enemy):
                    if top_to(self,object):
                        object.status-=1 
                        self.velocity_y = -3
                        self.rect.bottom = object.rect.top
                        if object.status <= 0 :
                            over(object)
                            

                    if right_to(self,object) or left_to(self,object):
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