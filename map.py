import pygame as pg

_ = False

map1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.map1 = map1
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.map1):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [
            pg.draw.rect(
                self.game.screen, "white", (pos[0] * 100, pos[1] * 100, 100, 100), 2
            )
            for pos in self.world_map
        ]
