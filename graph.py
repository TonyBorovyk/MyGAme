import time

from algoritms import BreadthFirstSearch,DepthFirstSearch,UniformCostSearch
import pygame as pg

Map_graph = {
    (0, 0): set([(0, 1)]),
    (0, 1): set([(0, 0), (0, 2)]),
    (0, 2): set([(0, 1), (0, 3)]),
    (0, 3): set([(0, 2), (0, 4)]),
    (0, 4): set([(0, 3), (0, 5)]),
    (0, 5): set([(0, 4), (0, 6)]),
    (0, 6): set([(0, 5), (0, 7)]),
    (0, 7): set([(0, 6), (0, 8)]),
    (0, 8): set([(0, 7), (0, 9)]),
    (0, 9): set([(0, 8), (0, 10)]),
    (0, 10): set([(0, 9), (0, 11)]),
    (0, 11): set([(0, 10)]),
    (1, 0): set([(1, 1), (0, 0), ]),
    (1, 1): set([(1, 0), (1, 2), (0, 1)]),
    (1, 2): set([(1, 1), (0, 2), (1, 3)]),
    (1, 3): set([(0, 3), (1, 4), (1, 2)]),
    (1, 4): set([(1, 3), (0, 4), (1, 5)]),
    (1, 5): set([(1, 4), (1, 6), (0, 5)]),
    (1, 6): set([(1, 5), (0, 6), (1, 7)]),
    (1, 7): set([(1, 6), (0, 7), (1, 8)]),
    (1, 8): set([(1, 7), (1, 9), (0, 8)]),
    (1, 9): set([(1, 8), (0, 9), (1, 10)]),
    (1, 10): set([(1, 9), (1, 11), (0, 10)]),
    (1, 11): set([(1, 10), (0, 11)]),
    (2, 0): set([(2, 1), (1, 0)]),
    (2, 1): set([(2, 0), (2, 2), (1, 1)]),
    (2, 2): set([(2, 1), (1, 2), (2, 3)]),
    (2, 3): set([(1, 3), (2, 4), (2, 2)]),
    (2, 4): set([(2, 3), (1, 4), (2, 5)]),
    (2, 5): set([(2, 4), (1, 5), (2, 6)]),
    (2, 6): set([(2, 5), (1, 6), (2, 7)]),
    (2, 7): set([(2, 6), (1, 7), (2, 8)]),
    (2, 8): set([(2, 7), (2, 9), (1, 8)]),
    (2, 9): set([(2, 8), (2, 10), (1, 9)]),
    (2, 10): set([(2, 9), (1, 10), (2, 11)]),
    (2, 11): set([(2, 10), (1, 11), ]),
    (3, 0): set([(3, 1), (2, 0)]),
    (3, 1): set([(2, 1), (3, 2), (3, 0)]),
    (3, 2): set([(3, 1), (3, 3), (2, 2)]),
    (3, 3): set([(3, 2), (3, 4), (2, 3)]),
    (3, 4): set([(3, 3), (2, 4), (3, 5)]),
    (3, 5): set([(3, 4), (3, 6), (2, 5)]),
    (3, 6): set([(2, 6), (3, 7), (3, 5)]),
    (3, 7): set([(3, 6), (2, 7), (3, 8)]),
    (3, 8): set([(3, 7), (3, 9), (2, 8)]),
    (3, 9): set([(3, 8), (2, 9), (3, 10)]),
    (3, 10): set([(3, 9), (3, 11), (2, 10)]),
    (3, 11): set([(2, 11), (3, 10)]),
    (4, 0): set([(3, 0), (4, 1)]),
    (4, 1): set([(3, 1), (4, 0), (4, 2)]),
    (4, 2): set([(3, 2), (4, 1), (4, 3)]),
    (4, 3): set([(3, 3), (4, 4), (4, 2)]),
    (4, 4): set([(3, 4), (4, 3), (4, 5)]),
    (4, 5): set([(4, 4), (3, 5), (4, 6)]),
    (4, 6): set([(4, 5), (3, 6), (4, 7)]),
    (4, 7): set([(3, 7), (4, 6), (4, 8)]),
    (4, 8): set([(3, 8), (4, 7), (4, 9)]),
    (4, 9): set([(4, 8), (3, 9), (4, 10)]),
    (4, 10): set([(4, 9), (3, 10), (4, 11)]),
    (4, 11): set([(4, 10), (3, 11)]),
    (5, 0): set([(5, 1), (4, 0)]),
    (5, 1): set([(5, 0), (4, 1), (5, 2)]),
    (5, 2): set([(5, 1), (5, 3), (4, 2)]),
    (5, 3): set([(4, 3), (5, 4), (5, 2)]),
    (5, 4): set([(5, 3), (4, 4), (5, 5)]),
    (5, 5): set([(5, 4), (4, 5), (5, 6)]),
    (5, 6): set([(5, 5), (4, 6), (5, 7)]),
    (5, 7): set([(5, 6), (5, 8), (4, 7)]),
    (5, 8): set([(4, 8), (5, 9), (5, 7)]),
    (5, 9): set([(5, 8), (4, 9), (5, 10)]),
    (5, 10): set([(5, 9), (4, 10), (5, 11)]),
    (5, 11): set([(5, 10), (4, 11)]),
    (6, 0): set([(6, 1), (5, 0)]),
    (6, 1): set([(6, 0), (5, 1), (6, 2)]),
    (6, 2): set([(6, 1), (6, 3), (5, 2)]),
    (6, 3): set([(6, 2), (5, 3), (6, 4)]),
    (6, 4): set([(6, 3), (5, 4), (6, 5)]),
    (6, 5): set([(6, 4), (5, 5), (6, 6)]),
    (6, 6): set([(6, 5), (5, 6), (6, 7)]),
    (6, 7): set([(6, 6), (6, 8), (5, 7)]),
    (6, 8): set([(6, 7), (5, 8), (6, 9)]),
    (6, 9): set([(6, 8), (5, 9), (6, 10)]),
    (6, 10): set([(6, 9), (5, 10), (6, 11)]),
    (6, 11): set([(6, 10), (5, 11), (7, 11)]),
    (7, 0): set([(7, 1), (6, 0)]),
    (7, 1): set([(7, 0), (6, 1), (7, 2)]),
    (7, 2): set([(7, 1), (6, 2), (7, 3)]),
    (7, 3): set([(7, 2), (6, 3), (7, 4)]),
    (7, 4): set([(7, 3), (6, 4), (7, 5)]),
    (7, 5): set([(7, 4), (6, 5), (7, 6)]),
    (7, 6): set([(7, 5), (6, 6), (7, 7)]),
    (7, 7): set([(7, 6), (6, 7), (7, 8)]),
    (7, 8): set([(7, 7), (6, 8), (7, 9)]),
    (7, 9): set([(7, 8), (6, 9), (7, 10)]),
    (7, 10): set([(7, 9), (6, 10), (7, 11)]),
    (7, 11): set([(7, 10), (6, 11)]),
    (8, 0): set([(8, 1), (6, 0)]),
    (8, 1): set([(8, 0), (6, 1), (7, 2)]),
    (8, 2): set([(8, 1), (6, 2), (7, 3)]),
    (8, 3): set([(8, 2), (6, 3), (7, 4)]),
    (8, 4): set([(8, 3), (6, 4), (7, 5)]),
    (8, 5): set([(8, 4), (6, 5), (7, 6)]),
    (8, 6): set([(8, 5), (6, 6), (7, 7)]),
    (8, 7): set([(8, 6), (6, 7), (7, 8)]),
    (8, 8): set([(8, 7), (6, 8), (7, 9)]),
    (8, 9): set([(8, 8), (6, 9), (7, 10)]),
    (8, 10): set([(8, 9), (6, 10), (7, 11)]),
    (8, 11): set([(8, 10), (6, 11)]),
}
# ===================== Побудова шляху ===========================#
def line_draw(screen, enemies, map, ship, aster, num_algo):
    line_to_enemy = []
    previous_line = []
    if num_algo == 1:
        for i in range(enemies.get_enemies_count()):
            line_to_enemy.append(UniformCostSearch(map, ship.get_player_pos(), enemies.get_Enemies_position(i)))
    if num_algo == 2:
        for i in range(enemies.get_enemies_count()):
            line_to_enemy.append(BreadthFirstSearch(map, ship.get_player_pos(), enemies.get_Enemies_position(i), aster))
    if num_algo == 3:
        for i in range(enemies.get_enemies_count()):
            line_to_enemy.append(DepthFirstSearch(map, ship.get_player_pos(), enemies.get_Enemies_position(i), aster))

    if previous_line != line_to_enemy:
        for i in range(len(previous_line)):
            previous_line.pop(i)
        previous_line = line_to_enemy

    if len(line_to_enemy) == 1:
        for j in range(len(previous_line[0]) - 1):
            (y, x) = previous_line[0][j]
            x, y = x * 64, y * 64
            if num_algo ==1:
                pg.draw.rect(screen, (190, 200, 100), pg.Rect(x, y, 18, 18))
            if num_algo ==2:
                pg.draw.rect(screen, (200, 0, 0), pg.Rect(x, y, 18, 18))
            if num_algo ==3:
                pg.draw.rect(screen, (0, 0, 0), pg.Rect(x, y, 18, 18))

    else:
        for i in range(len(line_to_enemy)):
            for j in range(len(line_to_enemy[i]) - 1):
                (y, x) = previous_line[i][j]
                x, y = x * 64, y * 64
                if num_algo == 1:
                    pg.draw.rect(screen, (190, 200, 100), pg.Rect(x, y, 18, 18))
                if num_algo == 2:
                    pg.draw.rect(screen, (200, 0, 0), pg.Rect(x, y, 18, 18))
                if num_algo == 3:
                    pg.draw.rect(screen, (0, 0, 0), pg.Rect(x, y, 18, 18))

