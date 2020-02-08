import pygame as pg
import numpy as np
from simulation import Moveable


class Car(pg.sprite.Sprite, Moveable):

    def __init__(self, image, startpos=(0., 0), accel=np.array([0., 0]), vel=np.array([0., 0])):
        pg.sprite.Sprite.__init__(self, self.groups)
        Moveable.__init__(self, loc=startpos, accel=accel, vel=vel)
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (50, 50))
        self.image = pg.transform.rotate(self.image, -90)
        self._originalimage = self.image
        self.rect = self.image.get_rect()
        self.update()

    def move(self):
        # print('car moving')
        Moveable.move(self, dt=0.05)
        self.update()

    def update(self):
        self.pos = Moveable.get_loc(self)
        rotation = -(Moveable.get_direction(self) / np.pi) * 180
        self.image = pg.transform.rotate(self._originalimage, rotation)
        self.rect.center = self.pos

    def accelerate(self, a_vec):
        a_vec = np.array(a_vec)
        Moveable.set_acceleration(self, a_vec)
