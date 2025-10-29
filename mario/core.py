import pygame as pg
import game_assets as ga
import map
import sys
from datetime import datetime
from sounds import theme,sound
def pause_game(screen):
    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 32)
    text = font.render("GAME PAUSED", True, (255, 255, 255))
    rect = text.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
    clock = pg.time.Clock()
    paused = True
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                paused = False 
        
        
        overlay = pg.Surface(screen.get_size(), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        screen.blit(text, rect)
        pg.display.flip()
        clock.tick(30)


def run_game(screen):
    game_screen = pg.display.set_mode(screen.get_size())
    object_group = map.map1()  
    clock = pg.time.Clock()
    mario = ga.Mario(200, 200, object_group)
    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16)
    titles = ["SCORE","COINS","WORLD","TIME","LIVES","BLINK","AMMO"]
    space_title = game_screen.get_width() / len(titles)
    running = True
    theme.change_theme(1)

    
    camera_x = 0
    camera_locked = False

    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False   
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause_game(game_screen)

        values = [
            lambda: str(mario.score),
            lambda: str(mario.coin),
            lambda: str(mario.map),
            lambda: str(mario.time_over // 60),
            lambda: str(mario.lives),
            lambda: mario.get_time_countdown_blink(),
            lambda: str(mario.quantity_bullet),
        ]

        
        if mario.dead:
            mario.dead = False  
            mario.rect.x = 50
            camera_x = 0
            camera_locked = True  

        
        target_camera = 500 - mario.rect.x
        if not camera_locked:
            if target_camera < camera_x:  
                camera_x = target_camera
        plus = camera_x

        
        if mario.rect.x > 500 - camera_x:
            camera_locked = False

        mario.update(pg.key.get_pressed())

        
        if mario.rect.x + plus < 0:
            mario.rect.x = -plus

        print(camera_x)

        game_screen.fill((0, 0, 0))

        
        for x in mario.object_group:
            if not isinstance(x, (ga.Mario, ga.bg)):
                if abs(x.rect.x - mario.rect.x) <= 600 or abs(abs(camera_x) - abs(x.rect.x) <= 1000):
                    x.update()
                if plus < 0:
                    game_screen.blit(x.image, (x.rect.x + plus, x.rect.y))
                else:
                    game_screen.blit(x.image, (x.rect.x, x.rect.y))
            elif isinstance(x, ga.bg):
                x.update()
                game_screen.blit(x.image, (x.rect.x + plus, x.rect.y) if plus < 0 else (x.rect.x, x.rect.y))


        for i in range(len(titles)):
            title = font.render(titles[i], True, (255, 255, 255))
            value = font.render(values[i](), True, (255, 255, 255))
            centerx = space_title * i + space_title // 2
            game_screen.blit(title, (centerx - title.get_width() // 2, 10))
            game_screen.blit(value, (centerx - value.get_width() // 2, 35))


        if plus < 0:
            game_screen.blit(mario.image, (mario.rect.x + plus, mario.rect.y))
        else:
            game_screen.blit(mario.image, mario.rect)

        
        if mario.end:
            if mario.lives > 0:
                match mario.map:
                    case 1:
                        object_group = map.map2()
                        mario.object_group = object_group
                        mario.object_group.add(mario)
                        mario.reset()
                        mario.map = 2
                        mario.rect.x = 50
                        camera_x = 0
                        camera_locked = True
                    case 2:
                        object_group = map.map3()
                        mario.object_group = object_group
                        mario.object_group.add(mario)
                        mario.reset()
                        mario.map = 3
                        mario.rect.x = 50
                        camera_x = 0
                        camera_locked = True
                    
                    
                    case _:
                        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        insert_score(f"{mario.score} {now}")
                        end_game(screen,f"{mario.score} {now}")
                        running = False
            else:
                game_over(game_screen)
                
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                insert_score(f"{mario.score} {now}")
                running = False

        pg.display.update()
        clock.tick(60)

class TextBox:
    def __init__(self, x, y, text, font):
        """
        x, y: tọa độ trên màn hình
        text: nội dung chữ hiển thị
        font: font Pygame đã tạo sẵn
        image_path: path đến hình nền textbox
        alpha: độ trong suốt của textbox (0->255)
        """
        alpha=255
        # Load hình nền
        self.base_img = pg.image.load("images/text box.png").convert_alpha()
        
        # Copy để chỉnh alpha
        self.image = self.base_img.copy()
        self.image.fill((255, 255, 255, alpha), special_flags=pg.BLEND_RGBA_MULT)
        
        # Vẽ chữ lên image
        text_surf = font.render(text, True, (0,0,0))  # chữ đen
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect)
        
        # Tọa độ để blit lên màn hình
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def get_surface(self):
        """Trả về surface đã có chữ trên hình nền"""
        return self.image

    def get_rect(self):
        """Trả về rect để blit lên màn hình"""
        return self.rect

def popup_highest():
    pg.init()
    popup_screen = pg.display.set_mode((1000, 512))
    pg.display.set_caption("Popup Message")

    popup_width, popup_height = 800, 400
    popup_rect = pg.Rect((1000 - popup_width) // 2, (512 - popup_height) // 2, popup_width, popup_height)

    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 18)

    with open("score.txt", "r", encoding="utf-8") as f:
        data_list = [line.strip() for line in f]

    popup_running = True
    scroll_y = 0
    line_height = 50
    max_scroll = max(0, len(data_list) * line_height - popup_height + 50)  # scroll tối đa
    scrollbar_width = 10
    clock = pg.time.Clock()

    while popup_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                    popup_running = False
                elif event.key == pg.K_UP:
                    scroll_y = max(scroll_y - 20, 0)
                elif event.key == pg.K_DOWN:
                    scroll_y = min(scroll_y + 20, max_scroll)
            if event.type == pg.MOUSEWHEEL:
                scroll_y = max(0, min(scroll_y - event.y * 20, max_scroll))

        popup_screen.fill((139, 247, 255))  

        pg.draw.rect(popup_screen, (139, 247, 255), popup_rect)
        pg.draw.rect(popup_screen, (0, 0, 0), popup_rect, 4)

        title = font.render("Bấm phím bất kỳ để thoát", True, (0,0,0))
        title_rect = title.get_rect(center=(popup_rect.centerx, 20))
        popup_screen.blit(title, title_rect)

        start_y = popup_rect.top + 50 - scroll_y
        for idx, data in enumerate(data_list):
            text = font.render(data, True, (0,0,0))
            text_rect = text.get_rect(topleft=(popup_rect.left + 20, start_y + idx * line_height))

            if popup_rect.top + 40 <= text_rect.bottom <= popup_rect.bottom - 10:
                popup_screen.blit(text, text_rect)

        if max_scroll > 0:
            scrollbar_height = popup_height * (popup_height / (popup_height + max_scroll))
            scrollbar_y = popup_rect.top + (scroll_y / max_scroll) * (popup_height - scrollbar_height)
            scrollbar_rect = pg.Rect(popup_rect.right - scrollbar_width - 5, scrollbar_y, scrollbar_width, scrollbar_height)
            pg.draw.rect(popup_screen, (0,0,0), scrollbar_rect)  

        pg.display.flip()
        clock.tick(60)

def end_game(screen,text_ip):
    sound.win()
    WIDTH, HEIGHT = screen.get_size()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font1 = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16)
    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 24)
    text = font.render("Not Enought Map Data Is Being Updating", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH//2, 50))
    
    text1 = font.render("Please Come Back Again", True, WHITE)
    text_rect1 = text1.get_rect(center=(WIDTH//2,100))
    
    text2 = font.render("Your score :", True, WHITE)
    text_rect2 = text2.get_rect(center=(WIDTH//2,150))

    text3 = font.render(str(text_ip), True, WHITE)
    text_rect3 = text3.get_rect(center=(WIDTH//2,200))

    text4 = font1.render("Press any key to return to the lobby", True, WHITE)
    text_rect4 = text4.get_rect(center=(WIDTH//2,HEIGHT-20))
    


    running = True
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                running = False
        overlay = pg.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        screen.blit(text, text_rect)
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
        pg.display.flip()
        clock.tick(60)

def game_over(screen):
    WIDTH, HEIGHT = screen.get_size()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 64)
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))

    running = True
    clock = pg.time.Clock()
    theme.change_theme(2)
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                running = False

        overlay = pg.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        screen.blit(text, text_rect)
        pg.display.flip()
        clock.tick(60)

def insert_score(new_line, filename="score.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    new_score = int(new_line.split()[0])
    inserted = False

    for i in range(len(lines)):
        current_score = int(lines[i].split()[0])
        if new_score >= current_score:
            lines.insert(i, new_line)
            inserted = True
            break

    if not inserted:
        lines.append(new_line)

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def instruct():
    pg.init()
    popup_screen = pg.display.set_mode((1000, 512))
    pg.display.set_caption("Popup Message")

    popup_width, popup_height = 800, 400
    popup_rect = pg.Rect((1000 - popup_width) // 2, (512 - popup_height) // 2, popup_width, popup_height)

    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 13)

    # Nội dung cố định
    data_list = [
        "Use arrows [↑→↓←] or W-A-S-D keys to move Mario",
        "To jump higher hold the button",
        "Press P to pause/unpause",
        "Press V to use blink to not be hit",
        "In level 3 you can use fire ball but attention to the ","quantity bullets"
    ]

    popup_running = True
    clock = pg.time.Clock()
    line_height = 50  # khoảng cách giữa các dòng

    while popup_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                # Bấm bất kỳ phím thoát popup
                popup_running = False

        # Background popup
        overlay = pg.Surface(popup_screen.get_size(), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  # đen mờ
        popup_screen.blit(overlay, (0, 0))

        pg.draw.rect(popup_screen, (200, 255, 255), popup_rect)
        pg.draw.rect(popup_screen, (0, 0, 0), popup_rect, 4)

        title = font.render("Bấm bất kỳ phím để thoát", True, (0, 0, 0))
        title_rect = title.get_rect(center=(popup_rect.centerx, popup_rect.top + 20))
        popup_screen.blit(title, title_rect)

        # Hiển thị hướng dẫn
        for idx, line in enumerate(data_list):
            text = font.render(line, True, (0, 0, 0))
            text_rect = text.get_rect(topleft=(popup_rect.left + 20, popup_rect.top + 60 + idx * line_height))
            popup_screen.blit(text, text_rect)

        pg.display.flip()
        clock.tick(60)

