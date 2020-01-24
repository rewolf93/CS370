import math


class Pysics:
    '''
    Container class for various physics calculations
    '''

    @classmethod
    def degreeprojecttoxy(cls, r: float, theta: float):
        '''
        Takes in a radius and theta in degrees
        Returns corresponding x,y values
        '''
        return cls.radianprojecttoxy(r, theta * math.pi / 180)

    @classmethod
    def radianprojecttoxy(cls, r: float, theta: float):
        '''
        Takes in a radius and theta in radians
        Returns corresponding x,y values
        '''
        return r * math.cos(theta), r * math.sin(theta)


def main():
    pass

main()
