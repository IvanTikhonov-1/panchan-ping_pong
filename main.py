import pygame
from pygame import *
pygame.init()
#Настройка текста
font_ = font.Font(None, 70)
wasted_right = font_.render("WASTED RIGHT PLAYER", True, (255,0,0))
wasted_left = font_.render("WASTED LEFT PLAYER", True, (255,0,0))
# Настройки окна
window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")

# Загрузка изображений
background = transform.scale(image.load("panchan.png"), (700, 500))
wall_1 = transform.scale(image.load("wall.png"), (25, 75))
wall_2 = transform.scale(image.load("wall.png"), (25, 75))
ball = transform.scale(image.load("ball.png"), (35, 35))

# Координаты стен
coox_1 = 10
cooy_1 = 250
coox_2 = 670
cooy_2 = 250

ball_rect = ball.get_rect()
wall_1_rect = wall_1.get_rect()
wall_2_rect = wall_2.get_rect()

# Начальные координаты шарика
ball_posx = 350
ball_posy = 250

# Скорость шарика
ball_speed_x = 3
ball_speed_y = 3

# Основной цикл игры
game = True
# pause = False
clock = time.Clock()  # Для ограничения FPS

while game:

    # Обновляем фон
    window.blit(background, (0, 0))

    keys_pressed = key.get_pressed()
    #Отображение панелей 
    window.blit(wall_1, (coox_1, cooy_1))
    window.blit(wall_2, (coox_2, cooy_2))
    #Движение панелей

    # if keys_pressed[K_ESCAPE]:
    #     ball_speed_x = 0
    #     ball_speed_y = 0

    if keys_pressed[K_UP] and cooy_2 > 5:
        cooy_2 -= 3

    if keys_pressed[K_DOWN] and cooy_2 < 420:
        cooy_2 += 3

    if keys_pressed[K_w] and cooy_1 > 5:
        cooy_1 -= 3

    if keys_pressed[K_s] and cooy_1 < 420:
        cooy_1 += 3

    # Движение шарика
    ball_posx += ball_speed_x
    ball_posy += ball_speed_y

    # Проверка столкновения с верхней и нижней границей окна
    if ball_posy <= 0 or ball_posy + ball.get_height() >= 500:
        ball_speed_y *= -1  # Отскок по Y

    ball_rect.topleft = (ball_posx, ball_posy)
    wall_1_rect.topleft = (coox_1, cooy_1)
    wall_2_rect.topleft = (coox_2, cooy_2)


    if ball_rect.colliderect(wall_1_rect) or ball_rect.colliderect(wall_2_rect):
        ball_speed_x *= -1

    if ball_posx <= 0:
        window.blit(wasted_left, (100, 100))#Проигрыш

    if ball_posx >= 700:
        window.blit(wasted_right, (100, 100),)#Проигрыш
    # Отображение шарика
    window.blit(ball, (ball_posx, ball_posy))

    # Обновление экрана
    display.update()
    clock.tick(60)  # 60 FPS

    for e in event.get():
        if e.type == QUIT:
            game = False

