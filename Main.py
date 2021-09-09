import sys
import random
import pygame
import math

# Ініціалізуємо pycharm та створюємо екран
pygame.init()

# screen_w = 1200
# screen_h = 800
screen = pygame.display.set_mode((1000, 800))

# Задній план
background = pygame.image.load('Space-Free-PNG-Image.png')

# Заголовок і іконка
pygame.display.set_caption("__Space_Ivaders__")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Гравець
playerIcon = pygame.image.load('Ship.png')
player_w, player_h = 470, 736
player_w_change = 0

# Вороги
enemyIcon = []
enemy_w = []
enemy_h = []
enemy_w_change = []
enemy_h_change = []
enemies_number = 20

# Закінчення гри
game_over = pygame.font.Font('freesansbold.ttf', 300)


def game_over_func():
    over_text = font.render("ПРОГРАШ", True, (255, 255, 255))
    screen.blit(over_text, (420, 420))

def win_func():
    over_text = font.render("ВИ ПЕРЕМОГЛИ!", True, (255, 255, 255))
    screen.blit(over_text, (350, 420))

for i in range(enemies_number):
    count = 0
    enemyIcon.append(pygame.image.load('ufo.png'))
    enemy_w.append(random.randint(0, 1000) + count)
    enemy_h.append(random.randint(30, 160))
    enemy_w_change.append(0.9)
    enemy_h_change.append(40)
    count += 64
# Куля
# ready - кулі не видно
# fire - куля рухається
bulletIcon = pygame.image.load('bullet.png')
bullet_w, bullet_h = 0, 736
bullet_w_change = 0
bullet_h_change = 4
bullet_state = "ready"

# Рахунок

score_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_w = 10
text_h = 10


def score_show(x, y):
    score = font.render("Рахунок:" + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    # створює додаткову поверхность, картинку гравця
    screen.blit(playerIcon, (x, y))


def enemy(x, y, i):
    # створює додаткову поверхность, картинку гравця
    screen.blit(enemyIcon[i], (x, y))


def bullet_fire(x, y):
    # Щоб бути доступним у середині функції
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIcon, (x + 16, y + 10))


def isCollision(enemy_w, enemy_h, bullet_w, bullet_h):
    distance = math.sqrt((math.pow(enemy_w - bullet_w, 2)) + (math.pow(enemy_h - bullet_h, 2)))
    if distance < 36:
        return True
    else:
        return False


# Запускаємо цикл програми, де будемо перехоплювати подію закриття програми
while True:

    screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # Виходимо із програми
            sys.exit()

        # Якщо стрілочки нажаті, то гравець рухається
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_w_change = -2

            if event.key == pygame.K_RIGHT:
                player_w_change = 2
            if event.key == pygame.K_SPACE:
                # Поки куля не долетить до краю то не можна стріляти
                if bullet_state is "ready":
                    # Зберігає координату корабля
                    bullet_w = player_w
                    bullet_fire(bullet_w, bullet_h)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_w_change = 0

    player_w += player_w_change

    # Тримаємо корабель і ворога в межах екрана (рух)
    if player_w <= 0:
        player_w = 0
    elif player_w >= 936:
        player_w = 936

    # Рух ворога
    for i in range(enemies_number):

        # Програш
        if enemy_h[i] > 200:
            for j in range(enemies_number):
                enemy_h[j] = 2000
                player_h = 2000
            game_over_func()
            break
        # Виграш
        if score_val >= 50:
            player_h = 2000
            win_func()
            break

        enemy_w[i] += enemy_w_change[i]
        if enemy_w[i] <= 0:
            enemy_w_change[i] = 0.9
            enemy_h[i] += enemy_h_change[i]
        elif enemy_w[i] >= 936:
            enemy_w_change[i] = -0.9

        # Зіткнення(колізія),як тільки зіткнувся то куля пропадає
        collision = isCollision(enemy_w[i], enemy_h[i], bullet_w, bullet_h)
        if collision:
            bullet_h = 736
            bullet_state = "ready"
            score_val += 10
            enemy_w[i], enemy_h[i] = 2000, -1000
        enemy(enemy_w[i], enemy_h[i], i)

    # Рух кулі та множинний вогонь
    if bullet_h <= 0:
        bullet_h = 736
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_fire(bullet_w, bullet_h)
        bullet_h -= bullet_h_change

    player(player_w, player_h)
    score_show(text_w, text_h)
    pygame.display.update()
