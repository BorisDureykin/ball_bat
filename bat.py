

import pygame.draw
from pygame.color import THECOLORS


class Bat:


    self = None

    def __init__(self,sc,k,z,s,h):
        self.s = s
        self.h = h
        self.color=THECOLORS['black']
        self._k=k
        self.z=z-self.h-3
        self.sc=sc
        self.render()

    def render(self):
        pygame.mouse.set_visible(False)
        b=pygame.mouse.get_pos()[0]
        if  b <= 0:
            self._k = 0
        elif b >= self.k-self.s:
            self._k = self._k - self.s
        else:
            self._k = pygame.mouse.get_pos()[0]
        pygame.draw.rect(self.sc, self.color, [self._k, self.z, self.s, self.h])

    def get_k(self):
        return self._k
    k = property(get_k)