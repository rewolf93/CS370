import numpy as np

CALC_PRECISION = 10


class Physics:
    '''
    Container class for various physics calculations
    '''

    @classmethod
    def accelerate(cls, disp_matrix, accel_vec):
        '''
        Takes a displacement matrix acceleration vector
        Updates the displacement matrix in place
        '''
        if np.issubdtype(accel_vec[0], np.signedinteger):
            accel_vec = accel_vec.astype(float)
        if np.issubdtype(disp_matrix[0][0], np.signedinteger):
            disp_matrix = disp_matrix.astype(float)
        a = cls.degreeprojectxy(accel_vec) / 2
        disp_matrix[0][0] = a[0]
        disp_matrix[1][0] = a[1]
        return disp_matrix

    @classmethod
    def displacement(cls, disp_mtrx, heading, dt=0.05):
        '''
        Calculates the displacement given a matrix of coefficients
        for the equation s = at^2 + bt^1 + c
        The matrix must be in the form np.array([(ax, bx, cx), (ay, by, cy)])
        The new location is stored in the original matrix and given
        by cx and  cy
        Returns an updated matrix and heading
        '''
        arry = np.copy(disp_mtrx)
        timevector = np.array([
                     dt**i for i in range(arry.shape[1]-1, -1, -1)])
        a_vec = np.array([arry[0][0], arry[1][0]])
        a_vec = cls.rotateaxis(a_vec, heading)
        arry[0][0] = a_vec[0]
        arry[1][0] = a_vec[1]
        s = np.sum(arry*timevector, axis=1)
        dv = np.array([arry[1][0] * 2 * dt, arry[0][0] * 2 * dt])
        updates = np.array([(0, 0), dv, (0, 0)])
        updates = np.rot90(updates, k=1, axes=(0, 1))
        disp_mtrx += updates
        disp_mtrx[0][2] = s[0]
        disp_mtrx[1][2] = s[1]
        disp_mtrx = np.around(disp_mtrx, decimals=CALC_PRECISION)
        vx = disp_mtrx[0][1]
        vy = disp_mtrx[1][1]

        # Figure out new heading via arctan(vy/vx)
        if vx < 0:
            if vy < 0:
                heading = np.arctan(vy/vx) - np.pi
            else:
                heading = np.arctan(vy/vx) + np.pi
        elif vx == 0:
            if vy == 0:
                pass
            elif vy > 0:
                heading = np.pi/2
            else:
                heading = np.pi/-2
        else:
            heading = np.arctan(vy/vx)
        return disp_mtrx, heading

    @classmethod
    def degreeprojectxy(cls, vec):
        '''
        Takes in a radius and theta in degrees
        Returns corresponding x,y values
        '''
        vec[1] = (vec[1] / 180.0) * np.pi
        return cls.radianprojectxy(vec)

    @classmethod
    def radianprojectxy(cls, vec):
        '''
        Takes in a radius and theta in radians
        Returns corresponding x,y values
        '''
        xy = np.array([vec[0] * np.cos(vec[1]),
                      vec[0] * np.sin(vec[1])])
        return np.around(xy, decimals=CALC_PRECISION)

    @classmethod
    def rotateaxis(cls, xy, heading):
        '''

        '''
        basis = np.array([(np.cos(heading), -np.sin(heading)),
                         (np.sin(heading), np.cos(heading))])
        return np.around(np.sum(xy*basis, axis=1), decimals=CALC_PRECISION)


class Moveable():
    '''
    A class that instanciates a moveable object and interfaces with the
    Physics object to make the simulation easier to interact with
    '''

    def __init__(self, loc=(0, 0), accel=np.array([0, 0]), disp_matrix=None):
        if disp_matrix:
            self.__disp_matrix = disp_matrix
        else:
            self.__disp_matrix = np.array([(0, 0, loc[0]), (0, 0, loc[1])])
            self.__heading = 0
            self.set_acceleration(accel)

    def move(self, count: int, dt=0.05):
        '''
        Moves the object `count` times with the interval `dt`
        Yielads the object's location at the end of each pass
        '''
        for _ in range(count):
            self.__disp_matrix, self.__heading = \
                Physics.displacement(self.__disp_matrix, self.__heading, dt=dt)
            print(self.__disp_matrix)

            yield self.get_loc()

    def get_loc(self):
        return self.__disp_matrix[0][2], self.__disp_matrix[1][2]

    def set_acceleration(self, accel):
        self.__disp_matrix = Physics.accelerate(self.__disp_matrix, accel)
