import numpy as np

CALC_PRECISION = 10


class Physics:
    '''
    Container class for various physics calculations
    '''

    @classmethod
    def accelerate(cls, disp_matrix, accel_vec, heading=0):
        '''
        Takes a displacement matrix, acceleration vector, and current heading
        The heading is the angle between the standard axis and the tilted axis
        of the object
        Updates the displacement matrix in place
        '''
        if np.issubdtype(accel_vec[0], np.signedinteger):
            accel_vec = accel_vec.astype(float)
        if np.issubdtype(disp_matrix[0][0], np.signedinteger):
            disp_matrix = disp_matrix.astype(float)
        print(f'accel_vec: {accel_vec}')
        a = cls.degreeprojectxy(accel_vec, heading=heading)
        print(f'a: {a}')
        print(f'heading: {heading}')
        print(f'accel_vec: {accel_vec}')
        disp_matrix[0][0] = a[0]/2
        disp_matrix[1][0] = a[1]/2

    @classmethod
    def displacement(cls, arry, heading, dt=0.05):
        '''
        Calculates the displacement given a matrix of coefficients
        for the equation s = at^2 + bt^1 + c
        The matrix must be in the form np.array([(ax, bx, cx), (ay, by, cy)])
        The new location is stored in the original matrix and given
        by cx and cy
        Returns an updated matrix and heading
        '''
        timevector = np.array([dt**i for i in range(arry.shape[1]-1, -1, -1)])
        ds = np.flip(np.sum(arry*timevector, axis=1))
        dv = np.array([arry[1][0] * dt, arry[0][0] * dt])
        updates = np.array([(0, 0), dv, ds])
        updates = np.rot90(updates, k=1, axes=(0, 1))
        arry += updates
        arry = np.around(arry, decimals=CALC_PRECISION)
        vx = arry[0][1]
        vy = arry[1][1]

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
        return arry, heading

    @classmethod
    def degreeprojectxy(cls, vec, heading=0):
        '''
        Takes in a radius and theta in degrees
        Returns corresponding x,y values
        '''
        print(f'vec: {vec}')
        vec[1] = (vec[1] / 180.0) * np.pi
        print(f'vec: {vec}')
        return cls.radianprojectxy(vec, heading=heading)

    @classmethod
    def radianprojectxy(cls, vec, heading=0):
        '''
        Takes in a radius and theta in radians
        Returns corresponding x,y values
        '''
        xy = np.array([vec[0] * np.cos(heading+vec[1]),
                      vec[0] * np.sin(heading+vec[1])])
        return np.around(xy, decimals=CALC_PRECISION)

    @classmethod
    def rotateaxis(cls, xy, heading):
        basis = np.array([(np.cos(heading), -np.sin(heading)),
                         (np.sin(heading), np.cos(heading))])
        return np.around(np.sum(xy*basis, axis=1), decimals=CALC_PRECISION)
