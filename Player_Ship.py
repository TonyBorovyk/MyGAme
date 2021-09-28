import pygame as pg


class Player_Ship:
    playerPictures = pg.image.load('pict/Ship.png')
    bulletPicture = pg.image.load('pict/bullet.png')
    XO_player = 400
    YO_player = 500
    SpeedOfShip = 0
    XO_bullet = 350
    YO_bullet = 500
    bullet_speed = 2
    bullet_state = "ready"

    def ship(self, player_w, player_h, screen):
        screen.blit(self.playerPictures, (player_w, player_h))

    def set_SpeedOfShip(self, temp):
        self.SpeedOfShip = temp

    def get_player_w(self):
        return self.XO_player

    def get_player_pos(self):
        widthPlace = int(self.XO_player / 64)
        heightPlace = int(self.YO_player / 64)
        return (heightPlace, widthPlace)

    def bound_lines(self):
        if self.XO_player <= 0:
            self.XO_player = 0
        elif self.XO_player >= 740:
            self.XO_player = 740

    def bullet(self, bullet_w, bullet_h, screen):
        self.bullet_state = "not ready"
        screen.blit(self.bulletPicture, (bullet_w + 16, bullet_h + 10))

    def set_bullet_w(self, coord):
        self.XO_bullet = coord

    def get_bullet_w(self):
        return self.XO_bullet

    def set_bullet_state(self, temp):
        self.bullet_state = temp

    def bullet_h_speed(self):
        self.YO_bullet -= self.bullet_speed

    def set_bullet_h(self, change):
        self.YO_bullet = change

    def YO_change(self, change):
        self.YO_bullet += change

    def get_bullet_h_speed(self):
        return self.bullet_speed

    def set_player_w(self, x):
        self.XO_player += x

    def get_SpeedOfShip(self):
        return self.SpeedOfShip

    def get_player_h(self):
        return self.YO_player

    def get_bullet_state(self):
        return self.bullet_state

    def get_bullet_h(self):
        return self.YO_bullet
