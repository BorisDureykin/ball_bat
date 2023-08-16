import pygame


class Ball:
    def __init__(self, sc,color, x,y,WIN_WIDTH, WIN_HEIGHT ):
        self._x = x
        self._y = y
        self.WIN_WIDTH=WIN_WIDTH
        self.WIN_HEIGHT=WIN_HEIGHT
        self.color = color
        self.sc = sc
        self.a = 10

        self.render()


    def render(self):

        pygame.draw.circle(self.sc, self.color, [self._x, self._y], self.a)


    def get_x(self):
        return self._x
    def set_x(self, x):
            self._x =x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)


