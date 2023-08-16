import pygame.draw


class Figuer:


    def __init__(self,sc, color,pos, widthF, heightF):
        self._xf, self._yf = pos

        self.color = color
        self.sc=sc
        self._widthF=widthF
        self._heightF=heightF
        self.render()

    def render(self):
        pygame.draw.rect(self.sc, self.color,[ self._xf,self._yf,self._widthF,self._heightF])

    def get_xf(self):
        return self._xf
    xf = property(get_xf)

    def get_yf(self):
        return self._yf
    yf = property(get_yf)

    def get_widthF(self):
        return self._widthF
    widthFig = property(get_widthF)

    def get_heightF(self):
        return self._heightF
    heightFig = property(get_heightF)