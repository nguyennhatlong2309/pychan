import pygame as pg
import game_assets as ga
import map
import sys

def run_game(screen):
    pg.init()
    game_screen = pg.display.set_mode((screen.get_size()))
    object_group = map.map1()  
    clock = pg.time.Clock()

    mario = ga.Mario(200,200,object_group)
    font  = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16) 

    titles = ["SCORE","COINS","WORLD","TIME","LIVES","BLINK","AMMO"]
    space_title = game_screen.get_width()/len(titles)

    running = True
    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT :
                running = False             
        
        values = [
            lambda: str(mario.score),
            lambda: str(mario.coin),
            lambda: "1-1",
            lambda: str(mario.time_over//60),
            lambda: str(mario.lives),
            lambda: mario.get_time_countdown_blink(),
            lambda: "300",
        ] 
        
        plus = 600 - mario.rect.x
        mario.update(pg.key.get_pressed())
        game_screen.fill((0,0,0))  # Xóa khung hình cũ mỗi loop

        

        for x in object_group:
            if not isinstance(x,(ga.Mario,ga.bg)):
                # pg.draw.rect(game_screen,(255,0,0),x.rect,2)
                if abs(x.rect.x - mario.rect.x) <= 600: 
                    x.update()
                if plus < 0 :
                    game_screen.blit(x.image, (x.rect.x+plus,x.rect.y))
                else :
                    game_screen.blit(x.image, (x.rect.x,x.rect.y))
            elif isinstance(x,ga.bg):
                x.update()
                game_screen.blit(x.image, (x.rect.x+plus,x.rect.y) if plus < 0 else (x.rect.x,x.rect.y))

        for i in range(len(titles)):
            title = font.render(titles[i], True, (255, 255, 255)) 
            value = font.render(values[i](), True, (255, 255, 255)) 
            centerx = space_title*i + space_title//2
            game_screen.blit(title,(centerx-title.get_width()//2,10))
            game_screen.blit(value,(centerx-value.get_width()//2,35))

        if plus < 0 :
            game_screen.blit(mario.image,(mario.rect.x + plus,mario.rect.y))
        else :
            game_screen.blit(mario.image,mario.rect)
        # pg.draw.rect(game_screen,(255,0,0),mario.rect,2)
        if mario.end :
            if mario.lives > 0 :
                match mario.map :
                    case 1: 
                        object_group = map.map2()
                        mario.object_group = object_group
                        mario.object_group.add(mario)
                        mario.reset()
                        mario.map = 2

                        mario.rect.x = 50
                    case 2 :
                        object_group = map.map3()
                        mario.object_group = object_group
                        mario.object_group.add(mario)
                        mario.reset()
                        mario.map = 3
                        
                        mario.rect.x = 50
                    case _:
                        print("end")
            else :
                game_over((game_screen))
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



def game_over(screen):
    WIDTH, HEIGHT = screen.get_size()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 64)
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))

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
        pg.display.flip()
        clock.tick(60)
