import pygame as pg

pg.mixer.init()
pg.init()

class Sound():
    def __init__(self):
        self.sound_jump = pg.mixer.Sound("sounds/jump.mp3")
        self.sound_dead = pg.mixer.Sound("sounds/death.mp3")
        self.sound_coin = pg.mixer.Sound("sounds/coin.mp3")
        self.sound_firebar = pg.mixer.Sound("sounds/fireball.mp3")
        self.sound_upgrade = pg.mixer.Sound("sounds/upgrade.mp3")
        self.sound_downgrade = pg.mixer.Sound("sounds/downgrade.mp3")
        self.sound_gameover = pg.mixer.Sound("sounds/music_over.mp3")
        self.sound_enemy = pg.mixer.Sound("sounds/enemy.mp3")
        self.sound_win = pg.mixer.Sound("sounds/music_win.mp3")
        self.sound_defect_brick = pg.mixer.Sound("sounds/defect_brick.mp3")

    
    def jump(self):
        self.sound_jump.play()

    def dead(self):
        self.sound_dead.play()

    def firebar(self):
        self.sound_firebar.play()

    def coin(self):
        self.sound_coin.play()

    def upgrade(self):
        self.sound_upgrade.play()

    def downgrade(self):
        self.sound_downgrade.play()

    def enemy(self):
        self.sound_enemy.play()

    def win(self):
        self.sound_win.play()

    def defect_brick(self):
        self.sound_defect_brick.play()



class Theme():
    def __init__(self):
        self.music_list = [pg.mixer.Sound("sounds/theme_home.mp3"),
                      pg.mixer.Sound("sounds/theme_game.mp3"),
                      pg.mixer.Sound("sounds/music_over.mp3")]
        self.theme = self.music_list[0]
        self.theme.play(-1)
        self.idx = 0
        
    def change_theme(self,idx):
        if self.idx != idx :
            self.idx = idx
            self.theme.stop()
            self.theme = self.music_list[idx]
            self.theme.play(-1)
    
    def stop(self):
        self.theme.stop()
        self.idx = 4

        
sound = Sound()
theme = Theme()
    