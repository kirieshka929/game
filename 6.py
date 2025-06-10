import pygame as pg
from random import *

pg.init()
disp = pg.display.set_mode((800, 480))
pg.display.set_caption('RONALDO')
pg.display.update()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


game_ower = False
clock = pg.time.Clock()
font = pg.font.Font(None, 40)
direction = "right"

x = 200
y = 320
apple_x = 400
apple_y = 120
score = 0
snake = [(x, y)]

while not game_ower:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_ower = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and direction != 'right':
                direction = 'left'
            if event.key == pg.K_RIGHT and direction != 'left':
                direction = 'right'
            if event.key == pg.K_UP and direction != 'down':
                direction = 'up'
            if event.key == pg.K_DOWN and direction != 'up':
                direction = 'down'
    if direction == "left":
        x -= 40
    if direction == 'right':
        x += 40
    if direction == 'up':
        y -= 40
    if direction == 'down':
        y += 40

    for i in range(len(snake) - 1):
        snake[i] = snake[i + 1]
    snake[-1] = [x, y]

    if x == apple_x and y == apple_y:
        snake = [snake[0]] + snake
        score += 1
        while [apple_x, apple_y] in snake:
             apple_x = randint(1, 19) * 40
             apple_y = randint(1, 11) * 40
            
    if x < 0 or x >= 800 or y >= 480 or y < 0:
        game_ower = True
        mess = font.render('Ты проиграл', True, RED)
        disp.blit(mess, [300, 0])
        pg.display.update()
        pg.time.delay(2000)
        break
      
    if len(snake) > 4 and snake[-1] in snake[:-1]:
       game_ower = True
       mess = font.render('Ты проиграл', True, RED)
       disp.blit(mess, [300, 240])
       pg.display.update()
       pg.time.delay(2000)
       break

    disp.fill(BLACK)
    for i in range(len(snake)):
        pg.draw.rect(disp, GREEN, [snake[i][0], snake[i][1], 40, 40])
    pg.draw.rect(disp, RED, (apple_x, apple_y, 40, 40))

    mess = font.render('Счет:' + str(score), True, RED)
    disp.blit(mess, [0, 0])
    pg.display.update()
pg.quit()
quit()
