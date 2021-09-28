import pygame as pg
import random
import math


class Enemies:
    Enemies_count = 5
    numOfEnemiesforalgo = 5
    enemiesXO_line = []
    enemyYO_line = []
    enemyPictures = []
    enemiesChange_speed = []
    enemiesYO_line_change = []
    asteroidsPicture = []
    XO_asteroid = []
    YO_asteroid = []
    healthOfAsteroid = []
    asteroids_counter = 3

    def create_enemies(self):
        for i in range(self.Enemies_count):
            self.enemyPictures.append(pg.image.load('pict/ufo.png'))
            self.enemiesXO_line.append(random.randint(0, 700))
            self.enemyYO_line.append(random.randint(50, 150))

            self.enemiesChange_speed.append(0.2)
            self.enemiesYO_line_change.append(50)

    def enemies(self, enemy_w, enemy_h, i, screen):
        screen.blit(self.enemyPictures[i], (enemy_w, enemy_h))

    def get_Enemies_position(self, i):
        if self.enemiesXO_line[i] <= 800 and self.enemyYO_line[i] <= 512:
            XO_coordinate = int(self.enemiesXO_line[i] / 64)
            YO_coordinate = int(self.enemyYO_line[i] / 64)
        else:
            XO_coordinate = -1
            YO_coordinate = -1
        return (YO_coordinate, XO_coordinate)


    def HealthOfAsteroid(self, bullet, game, screen, enemies):
        for i in range(self.asteroids_counter):

            self.aster(screen, i, self.XO_asteroid[i], self.YO_asteroid[i])

            isCollision = game.Colision_of_aster(self.XO_asteroid[i], self.YO_asteroid[i], bullet.get_bullet_w(),
                                                 bullet.get_bullet_h())
            if isCollision:
                bullet.set_bullet_h(470)
                bullet.set_bullet_state("ready")
                self.asteroidsPicture[i] = pg.image.load('pict/earth.png')
                self.healthOfAsteroid[i] -= 1

            if self.healthOfAsteroid[i] == 0:
                self.YO_asteroid[i] = 2700
            self.aster(screen, i, self.XO_asteroid[i], self.YO_asteroid[i])
            if enemies.get_enemies_count() == 0:
                for i in range(self.asteroids_counter):
                    self.YO_asteroid[i] = 2700

    def enemiesMove(self, game, bullet, screen, asteroids):

        for i in range(self.Enemies_count):
            self.enemiesXO_line[i] += self.enemiesChange_speed[i]
            if self.enemiesXO_line[i] <= 0:
                self.enemiesChange_speed[i] = 0.5
                self.enemyYO_line[i] += self.enemiesYO_line_change[i]
            elif self.enemiesXO_line[i] >= 740:
                self.enemiesChange_speed[i] = -0.5
                self.enemyYO_line[i] += self.enemiesYO_line_change[i]
            self.enemies(self.enemiesXO_line[i], self.enemyYO_line[i], i, screen)

            isCollision = game.Colision(self.enemiesXO_line[i], self.enemyYO_line[i], bullet.get_bullet_w(),
                                        bullet.get_bullet_h())
            if isCollision:
                bullet.set_bullet_h(470)
                bullet.set_bullet_state("ready")
                game.set_score(100)
                self.enemyYO_line[i] = 3000
            self.enemies(self.enemiesXO_line[i], self.enemyYO_line[i], i, screen)
            if game.score == 500:
                for i in range(asteroids.asteroids_counter):
                    asteroids.XO_asteroid[i] = 1500
                game.win_func(screen)
                break
            if self.enemyYO_line[i] >= 500 and self.enemyYO_line[i] <= 600:
                for j in range(self.Enemies_count):
                    self.enemyYO_line[j] = 1500
                    self.enemiesChange_speed[i] = 0
                for i in range(asteroids.asteroids_counter):
                    asteroids.YO_asteroid[i] = 1500
                game.lose_func(screen)
                break

    def get_enemies_count(self):
        return self.Enemies_count

    def aster(self, screen, i, XO_aster_coordinate, YO_aster_coordinate):
        screen.blit(self.asteroidsPicture[i], (XO_aster_coordinate, YO_aster_coordinate))

    def aster_pos(self, i):
        if self.XO_asteroid[i] <= 800 and self.YO_asteroid[i] <= 512:
            XO = int(self.XO_asteroid[i] / 64)
            YO = int(self.YO_asteroid[i] / 64)
        else:
            XO = 0
            YO = 8
        return (YO, XO)

    def create_Asteroid(self):
        temp = 1
        for i in range(self.asteroids_counter):
            if temp == 1:
                self.XO_asteroid.append(60)
                self.YO_asteroid.append(360)
            if temp == 2:
                self.XO_asteroid.append(340)
                self.YO_asteroid.append(360)
            if temp == 3:
                self.XO_asteroid.append(650)
                self.YO_asteroid.append(360)
            if temp == 4:
                self.XO_asteroid.append(180)
                self.YO_asteroid.append(250)
            self.asteroidsPicture.append(pg.image.load('pict/jupiter.png'))
            self.healthOfAsteroid.append(2)
            temp += 1

class Game:
    # Рахунок, шрифти і лічильник для кількості ворогів
    pg.init()
    fonts = pg.font.Font('freesansbold.ttf', 30)
    lose = pg.font.Font('freesansbold.ttf', 50)
    score = 0
    countofEnemies = 0

    def FindScore(self, XO_score, YO_score, screen):
        main_score = self.fonts.render("Рахунок: " + str(self.score), True, (255, 255, 255))
        screen.blit(main_score, (XO_score, YO_score))

    # Функція яка перевіряє чи доторкались вороги та пулі
    def Colision(self, enemies_w, enemies_h, bullet_w, bullet_h):
        isCollision = math.sqrt((math.pow(enemies_w - bullet_w, 2)) + (math.pow(enemies_h - bullet_h, 2)))
        if isCollision < 30:
            return True
        else:
            return False

    def Colision_of_aster(self, aster_w, aster_h, bullet_w, bullet_h):
        isCollision = math.sqrt((math.pow(aster_w - bullet_w, 2)) + (math.pow(aster_h - bullet_h, 2)))
        if isCollision < 55:
            return True
        else:
            return False

    def set_score(self, temp):
        self.score += temp

    def aster_XY(self, asteroids):
        asteroid_XY = []
        for i in range(asteroids.asteroids_counter):
            asteroid_XY.append(asteroids.aster_pos(i))

        return asteroid_XY

    def win_func(self, screen):
        gameOverTitle = self.lose.render("Ви Виграли!", True, (255, 255, 255))
        screen.blit(gameOverTitle, (250, 250))


    def lose_func(self, screen):
        gameOvertitle = self.lose.render("Ви прогали!", True, (255, 255, 255))
        screen.blit(gameOvertitle, (250, 250))