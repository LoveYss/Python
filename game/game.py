# Author: Loveyss
# -*-coding:utf-8 -*-
# @Time     :2019/4/13   10:40
# @Author   :Loveyss
# @Site     :
# @File     :game.py
# @Software :PyCharm
import pygame
from pygame.locals import *
import random
pygame.init()
panel = pygame.display.set_mode((900, 600))
pygame.display.set_caption('毕老大战僵尸')
bg = pygame.image.load('img/grassland.jpg')
bibi = pygame.image.load('img/bb.png')
lair = pygame.image.load('img/lart.png')
bullet = pygame.image.load('img/子弹.png')
shell = pygame.image.load('img/炮弹.png')
shells = []
menus = pygame.image.load('img/menu.png')
menu1 = pygame.image.load('img/母鸡.jpg')
menu2 = pygame.image.load('img/奶牛.jpg')
menu3 = pygame.image.load('img/射手.jpg')
menu4 = pygame.image.load('img/地雷.jpg')
menu_list = [menu1, menu2, menu3, menu4]
wall = pygame.image.load('img/墙.png')
monster_informations = []
monster_xiaoxin1 = pygame.image.load('action_list/run/01.png')
monster_xiaoxin2 = pygame.image.load('action_list/run/02.png')
monster_xiaoxin3 = pygame.image.load('action_list/run/03.png')
monster_xiaoxin4 = pygame.image.load('action_list/run/04.png')
monster_xiaoxin5 = pygame.image.load('action_list/run/05.png')

monster_xiaoxin6 = pygame.image.load('action_list/attack/01.png')
monster_xiaoxin7 = pygame.image.load('action_list/attack/02.png')
monster_xiaoxin8 = pygame.image.load('action_list/attack/03.png')
monster_xiaoxin9 = pygame.image.load('action_list/attack/04.png')

monster_xiaoxin10 = pygame.image.load('action_list/die/01.png')
monster_xiaoxin11 = pygame.image.load('action_list/die/02.png')
monster_xiaoxin12 = pygame.image.load('action_list/die/03.png')
monster_xiaoxin13 = pygame.image.load('action_list/die/04.png')
ball_pos_x = 400
ball_pos_y = 300
# 移动速度
vel_x = 2
vel_y = 2
# Clock对象
clock = pygame.time.Clock()
# 速度（像素/秒）
speed = 100.
state = False

# 移动毕老


def move(ball_pos_x, ball_pos_y, vel_x, vel_y):
    keys = pygame.key.get_pressed()
    # 移动毕老
    if keys[K_w]:
        ball_pos_y -= vel_y
    if keys[K_s]:
        ball_pos_y += vel_y
    if keys[K_a]:
        ball_pos_x -= vel_x
    if keys[K_d]:
        ball_pos_x += vel_x
    if ball_pos_x > 700:
        ball_pos_x = 700
    elif ball_pos_x < 600:
        ball_pos_x = 600
    if ball_pos_y > 350:
        ball_pos_y = 350
    elif ball_pos_y < 0:
        ball_pos_y = 0
    return ball_pos_x, ball_pos_y

# 事件处理


def events(ball_pos_x, ball_pos_y, state):
    bullets_x, shell_x = ball_pos_x - 50, ball_pos_x - 50
    bullets_y, shell_y = ball_pos_y + 100, ball_pos_y + 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if pos_x < 0 and pos_y < 0:
                pass
            else:
                button1, button2, button3 = pygame.mouse.get_pressed()
                if button1:
                    shells.append([0, bullets_x, bullets_y])
                    state = 1
                if button3:
                    shells.append([1, shell_x, shell_y-10])
                    state = 3
    return state


# 子弹


def bullets(states, seconds):
    # print(seconds)
    if states:
        # print(bullets)
        for i in shells:
            if not i[0]:
                i[1] -= seconds * 300
                # print(i[1])
                panel.blit(bullet, (i[1], i[2]))
            else:
                i[1] -= seconds * 200
                panel.blit(shell, (i[1], i[2]))
            if i[1] < -100:
                shells.remove(i)


frame = 10


def monsters_run(frames, info, seconds):
    frames += 10 * seconds
    # print(x)
    if info[-1] <= 0:
        if frames/2 < 10:
            panel.blit(monster_xiaoxin10, [info[0], info[1]])
        elif frames/2 < 20:
            panel.blit(monster_xiaoxin11, [info[0], info[1]])
        elif frames/2 < 30:
            panel.blit(monster_xiaoxin12, [info[0], info[1]])
        elif frames/2 < 40:
            panel.blit(monster_xiaoxin13, [info[0], info[1]])
        else:
            monster_informations.remove(info)
            frames = 10
    else:
        if info[0] < 470:
            info[0] += 20 * seconds
            if frames < 10:
                panel.blit(monster_xiaoxin1, [info[0], info[1]])
            elif frames < 20:
                panel.blit(monster_xiaoxin2, [info[0], info[1]])
            elif frames < 30:
                panel.blit(monster_xiaoxin3, [info[0], info[1]])
            elif frames < 40:
                panel.blit(monster_xiaoxin4, [info[0], info[1]])
            elif frames < 50:
                panel.blit(monster_xiaoxin5, [info[0], info[1]])
            elif frames < 60:
                panel.blit(monster_xiaoxin4, [info[0], info[1]])
            elif frames < 70:
                panel.blit(monster_xiaoxin3, [info[0], info[1]])
            elif frames < 80:
                panel.blit(monster_xiaoxin2, [info[0], info[1]])
            elif frames < 90:
                panel.blit(monster_xiaoxin1, [info[0], info[1]])
            else:
                panel.blit(monster_xiaoxin1, [info[0], info[1]])
                frames = 10
        else:
            if frames < 30:
                panel.blit(monster_xiaoxin6, [info[0], info[1]])
            elif frames < 60:
                panel.blit(monster_xiaoxin7, [info[0], info[1]])
            elif frames < 90:
                panel.blit(monster_xiaoxin8, [info[0], info[1]])
            elif frames < 120:
                panel.blit(monster_xiaoxin7, [info[0], info[1]])
            else:
                panel.blit(monster_xiaoxin6, [info[0], info[1]])
                frames = 10
    return frames, info[0]


def monster_information():
    abscissa = random.sample(range(-70, -1000, -70), 10)
    for x in range(10):
        ordinate = random.choice([60, 160, 260, 360])
        lmp = [abscissa[x], ordinate, 0, 5]
        monster_informations.append(lmp)
        # lmp.clear()
    # print(monster_informations)

    # AABB盒子是否碰撞


def pyRectCollision(aBox, bBox):
    ax = aBox[0]
    ay = aBox[1]
    Ax = aBox[2] + aBox[0]
    Ay = aBox[3] + aBox[1]

    bx = bBox[0]
    by = bBox[1]
    Bx = bBox[2] + bBox[0]
    By = bBox[3] + bBox[1]

    if (ax < Bx and bx < Ax) and (ay < By and by < Ay):
        return True
    else:
        return False


def war():
    global frame
    for i in monster_informations:
        frame, i[0] = monsters_run(frame, i, time_passed_seconds)
        monster_rect = Rect(i[0], i[1], 100, 70)
        for j in shells:
            bullet_rect = Rect(j[1], j[2], 10, 40)
            t_f = pyRectCollision(monster_rect, bullet_rect)
            if t_f:
                shells.remove(j)
                i[-1] -= 1



monster_information()
while True:
    print(monster_informations)
    ball_pos_x, ball_pos_y = move(ball_pos_x, ball_pos_y, vel_x, vel_y)
    panel.blit(bg, (0, 0))
    panel.blit(bibi, (ball_pos_x, ball_pos_y))
    for i in range(60, 610, 110):
        panel.blit(lair, (780, i))
    panel.blit(menus, (0, 470))
    lmp = 80
    for menu in menu_list:
        panel.blit(menu, (lmp, 480))
        lmp += 120
    panel.blit(wall, (550, -30))
    state = events(ball_pos_x, ball_pos_y, state)
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.
    bullets(state, time_passed_seconds)
    war()

    pygame.display.update()
