from Player_Ship import Player_Ship
from Enemies import Enemies
import pygame as pg
from graph import line_draw
from graph import Map_graph
from Enemies import Game

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Space Invaders")
game_Icon = pg.image.load('pict/space-invaders.png')
pg.display.set_icon(game_Icon)
background_picture = pg.image.load('pict/Space-Free-PNG-Image.png')
ship = Player_Ship()
enemies = Enemies()
bullet = Player_Ship()
game = Game()
aster = Enemies()
enemies.create_enemies()
BFS_algo, DFS_algo, UCS_algo = 0, 0, 0
aster.create_Asteroid()
close = True

while close:
    screen.fill((0, 0, 0))
    screen.blit(background_picture, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                ship.set_SpeedOfShip(1.5)
            if event.key == pg.K_LEFT:
                ship.set_SpeedOfShip(-1.5)
            if event.key == pg.K_SPACE:
                if bullet.get_bullet_state() == "ready":
                    bullet.set_bullet_w(ship.get_player_w())
                    bullet.bullet(bullet.get_bullet_w(), bullet.get_bullet_h(), screen)
                    bullet.YO_change(-bullet.get_bullet_h_speed())
            if event.key == pg.K_z:
                print('===========BFS==========')
                BFS_algo, DFS_algo, UCS_algo = 1, 0, 0
            if event.key == pg.K_a:
                print('===========UCS=========')
                BFS_algo, DFS_algo, UCS_algo = 0, 0, 1
            if event.key == pg.K_q:
                print('===========DFS==========')
                BFS_algo, DFS_algo, UCS_algo = 0, 1, 0
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                ship.set_SpeedOfShip(0)

    ship.set_player_w(ship.get_SpeedOfShip())
    if bullet.get_bullet_h() <= 0:
        bullet.set_bullet_state("ready")
        bullet.set_bullet_h(470)
    enemies.enemiesMove(game, bullet, screen, aster)
    aster.HealthOfAsteroid(bullet, game, screen, enemies)
    if bullet.get_bullet_state() == "not ready":
        bullet.bullet(bullet.get_bullet_w(), bullet.get_bullet_h(), screen)
        bullet.YO_change(-bullet.get_bullet_h_speed())
    ship.bound_lines()
    if enemies.get_enemies_count() == 0:
        game.win_func(screen)
        temp = False
    asteroid_xy = game.aster_XY(aster)
    if BFS_algo == 1:
        line_draw(screen, enemies, Map_graph, ship, asteroid_xy, 2)
    if DFS_algo == 1:
        line_draw(screen, enemies, Map_graph, ship, asteroid_xy, 3)
    if UCS_algo == 1:
        line_draw(screen, enemies, Map_graph, ship, asteroid_xy, 1)
    ship.ship(ship.get_player_w(), ship.get_player_h(), screen)
    game.FindScore(15, 10, screen)
    pg.display.update()
