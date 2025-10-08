import pygame as pg

# Khởi tạo pygame
pg.init()

# Kích thước cửa sổ
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Tạo cửa sổ (screen)
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("My Pygame Screen")

# Màu nền (RGB)
WHITE = (255, 255, 255)

image = pg.image.load("images/Goomba.gif")
rect = image.get_rect(topleft=(50,50))

# Vòng lặp chính
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Tô màu nền trắng
    screen.fill(WHITE)
    screen.blit(image,rect)

    # Cập nhật hiển thị
    pg.display.flip()

# Thoát pygame
pg.quit()
