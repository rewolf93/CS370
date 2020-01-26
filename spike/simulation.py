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
        by cx and cy
        Returns an updated matrix and heading
        '''
        arry = np.copy(disp_mtrx)
        timevector = np.array([
                     dt**i for i in range(arry.shape[1]-1, -1, -1)])
        a_vec = np.array([arry[0][0], arry[1][0]])
        a_vec = cls.rotateaxis(a_vec, heading)
        arry[0][0] = a_vec[0]
        arry[1][0] = a_vec[1]
        ds = np.flip(np.sum(arry*timevector, axis=1))
        dv = np.array([arry[1][0] * dt, arry[0][0] * dt])
        updates = np.array([(0, 0), dv, ds])
        updates = np.rot90(updates, k=1, axes=(0, 1))
        disp_mtrx += updates
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
        # print(xy)
        basis = np.array([(np.cos(heading), -np.sin(heading)),
                         (np.sin(heading), np.cos(heading))])
        return np.around(np.sum(xy*basis, axis=1), decimals=CALC_PRECISION)
