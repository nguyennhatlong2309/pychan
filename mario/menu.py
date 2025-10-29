import pygame as pg
import sys
import core
from sounds import theme
pg.init()

# --- Cài đặt màn hình ---
WIDTH, HEIGHT = 1000, 512
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Mario Menu Example")

# --- Màu sắc ---
WHITE = (255, 255, 255)
BLUE = (0, 72, 255)
RED = (255,0,0)

BLACK=(0,0,0)
background_game = pg.image.load("images/bg_game.png")
background_game_rect = background_game.get_rect(topleft=(0,0))

font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16)

menu_items = ["New game", "High Score","Instruct","Exit"]
selected = 0 
screen.blit(background_game, background_game_rect)
def draw_menu():

    
    screen.blit(background_game, background_game_rect)

    # Tạo lớp nền mờ
    transparent_surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 0))  # Độ mờ 150 (0 là trong suốt, 255 là đen đặc)
    screen.blit(transparent_surface, (0, 0))
    for i, item in enumerate(menu_items):
        color = RED if i == selected else WHITE
        text = font.render(item, True, color)
        rect = text.get_rect(center=(WIDTH // 2, 200 + i * 60))
        screen.blit(text, rect)
    pg.display.flip()

running = True
while running:
    draw_menu()
    theme.change_theme(0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                selected = (selected - 1) % len(menu_items)
            elif event.key == pg.K_DOWN:
                selected = (selected + 1) % len(menu_items)
            elif event.key == pg.K_RETURN:
                choice = menu_items[selected]
                if choice == "New game":
                    print("Start Game!")
                    core.run_game(screen)
                elif choice == "Instruct":
                    print()
                    core.instruct()
                elif choice == "High Score":
                    core.popup_highest()
                elif choice == "Exit":
                    running = False
        
pg.quit()
sys.exit()
