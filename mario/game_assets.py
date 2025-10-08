import pygame as pg
class object(pg.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))



class enemy(object):
    def __init__(self, image, x, y):
        super().__init__(image,x,y)

class floor(object):
    def __init__(self,width,x, y):
        image = pg.image.load("images/grounds.png").subsurface(pg.Rect(0,0,width,32))
        super().__init__(image, x, y)

class brick(object):
    def __init__(self,x, y):
        image = pg.image.load("images/brick.gif")
        x*=32
        y*=32
        super().__init__(image,x,y)


class Goomba(enemy):
    def __init__(self, x, y):
        frame = [pg.image.load("images/Goomba_frame_0.png"),pg.image.load("images/Goomba_frame_0.png")]
        super().__init__(frame[0], x, y)


class Mario(object):
    
    def __init__(self, x, y):
        self.right = pg.image.load("images/Mario.png")
        self.velocity_y = 0
        self.velocity_x = 0
        self.power_jump = 12
        self.gravity = 0.2
        self.on_ground = False
        self.are_going = False
        self.lose = False
        self.status = 1 
        self.direct = 1
        self.edge_left = 1000
        self.edge_right = 1000
        
        self.left_img = pg.image.load("images/Mario_Left.png")
        self.jump_img =pg.image.load("images/Mario_jump.gif")
        self.walking_right1 = pg.image.load("images/Mario_Walking1.png")
        self.walking_right2 = pg.image.load("images/Mario_Walking2.png")
        self.walking_left1 = pg.image.load("images/Mario_Walking_Left1.png")
        self.walking_left2 = pg.image.load("images/Mario_Walking_Left2.png")
        self.animation_left = [self.left_img,self.walking_left1,self.walking_left2]
        super().__init__(self.right,x,y)
        self.last_changes = 0
        self.current_time = 0
        self.last_jump = 0

    def jump(self):
        self.image = self.jump_img
        if self.on_ground and self.current_time - self.last_jump > 500: 
            self.velocity_y =-self.power_jump
            self.on_ground=False
            self.last_jump = self.current_time

    def fall(self):
        if not self.on_ground :
            self.image = self.jump_img
            self.rect.y += self.velocity_y
            self.velocity_y += self.gravity
        else :
            self.velocity_y = 0

    def slip(self):
        self.rect.x += self.velocity_x
        if not self.are_going and self.velocity_x!=0: 
            direct = 1 if self.velocity_x < 0 else -1 
            self.velocity_x += self.gravity*direct
            self.rect.x += self.velocity_x
        if self.velocity_x == 0:
            self.are_going = False
    
    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0
    
    def check_onground(self,terrain_group):
        
        for object in terrain_group:
            if self.rect.colliderect(object.rect):
                if self.rect.bottom == object.rect.top:
                    self.on_ground = True
                    return 
            self.on_ground = False
            return 
    def top_to(self,object):
        if self.rect.top < object.rect.top and self.rect.bottom < object.rect.bottom and self.velocity_y > 0 and self.rect.bottom - object.rect.top <= self.velocity_y+1:
            return True
        return False
    def bot_to(self,object):
            if self.rect.top > object.rect.top and self.rect.bottom > object.rect.top and self.rect.top < object.rect.bottom and self.velocity_y <0 and object.rect.bottom - self.rect.top <= abs(self.velocity_y):
                return True
            return False
        
    def left_to(self,object):
        if self.rect.left < object.rect.left and self.rect.left < object.rect.left and abs(self.rect.right - object.rect.left) <= 3 :
            return True
    def right_to(self,object):
        if self.rect.left > object.rect.left and self.rect.left > object.rect.left and abs(self.rect.left - object.rect.right) <= 3 and self.velocity_x <0:
            return True

    def check_collide(self,terrain_group):
        for object in terrain_group:
            if self.rect.colliderect(object.rect):
                if isinstance(object,floor):
                    if self.left_to(object):
                        print("left_to")
                        self.rect.right = object.rect.left
                        self.velocity_x = 0

                    if self.right_to(object):
                        self.rect.left = object.rect.right
                        self.velocity_x = 0
                        print("rightt_to")

                    if self.top_to(object)and not (self.left_to(object) or self.right_to(object)):
                        self.edge_left = object.rect.left
                        self.edge_right = object.rect.right
                        self.velocity_y = 0
                        self.on_ground = True
                        self.rect.bottom = object.rect.top
                        print("top_to")
                    
                    if self.bot_to(object):
                        self.velocity_y = 0
                        self.rect.top 
                        self.rect.top = object.rect.bottom
                        print("bot_to")


    
    def over(self):
        if not self.lose :
            self.lose= True
            self.velocity_y -=3       
            self.velocity_x =0        
                
    def move_x(self):
        self.are_going = True
        if self.velocity_x < 3 and self.velocity_x > -3:
            self.velocity_x += 0.5*self.direct
        
        else :
            self.velocity_x = 3*self.direct
        
    def update(self):
        if self.rect.left > self.edge_right or self.rect.right < self.edge_left or self.lose:
            self.on_ground = False
        self.animation()
        self.slip()
        self.fall()

    def animation(self):
        if self.are_going :
            # self.status = 0 if self.status == 2 else 1 if self.status == 0 else 2

            # idx = self.status* self.direct
            # self.image = self.animation_left[idx]
            return 

        
        
        
        
