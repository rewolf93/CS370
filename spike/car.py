import pygame as pg
from simulation import Moveable


class Car(pg.sprite.Sprite, Moveable):

    def __init__(self, image, startpos=(0, 0)):
        pg.sprite.Sprite.__init__(self, self.groups)
        self.pos = startpos
        (self.x, self.y) = self.pos
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()

    def update(self):
        self.pos = (self.x, self.y)
        self.rect.center = self.pos
