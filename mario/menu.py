import pygame as pg
import sys
import core
import game_assets as ga
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
background_game = pg.image.load("images/bg_game1.png")
background_game_rect = background_game.get_rect(topleft=(0,0))

font = pg.font.Font("fonts/PressStart2P-Regular (1).ttf", 16) 

# --- Menu ---
menu_items = ["Start","Option", "High Score","Instruct","Exit"]
selected = 0  # Lựa chọn hiện tại
screen.blit(background_game, background_game_rect)
def draw_menu():

    
    screen.blit(background_game, background_game_rect)

    # Tạo lớp nền mờ
    transparent_surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 50))  # Độ mờ 150 (0 là trong suốt, 255 là đen đặc)
    screen.blit(transparent_surface, (0, 0))
    for i, item in enumerate(menu_items):
        color = RED if i == selected else WHITE
        text = font.render(item, True, color)
        rect = text.get_rect(center=(WIDTH // 2, 150 + i * 60))
        screen.blit(text, rect)
    pg.display.flip()

running = True
while running:
    draw_menu()
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
                if choice == "Start":
                    print("Start Game!")
                    core.run_game(screen)
                elif choice == "Instruct":
                    print("Continue Game!")
                    core.game_over(screen)
                elif choice == "High Score":
                    core.popup_highest()
                elif choice == "Exit":
                    running = False

pg.quit()
sys.exit()
