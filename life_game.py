# -*- coding: utf-8 -*-
#
# @author SEMOOC

from game_map import GameMap
import os


class LifeGame(object):
    """
    Game of life.

    This class controls a game cycle triggered by timer.

    Attributes:
        game_map: GameMap instance.
    """

    def __init__(self, map_rows=10, map_cols=10, life_init_possibility=0.5):
        self.game_map = GameMap(map_rows, map_cols)
        self.game_map.reset(life_init_possibility)

    def print_map(self):
        """Clear the console, then print the map"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.game_map.print_map()

    def game_cycle(self):
        nc_map = self.game_map.get_neighbor_count_map()
        for row in range(self.game_map.rows):
            for col in range(self.game_map.cols):
                nc = nc_map[row][col]
                if nc < 2 or nc > 3:
                    self.game_map.set(row, col, 0)
                elif nc == 3:
                    self.game_map.set(row, col, 1)
        self.print_map()
