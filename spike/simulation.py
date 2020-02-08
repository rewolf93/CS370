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
        v_vec = np.array([arry[0][1], arry[1][1]])
        v_vec = cls.rotateaxis(v_vec, heading)
        arry[0][1] = v_vec[0]
        arry[1][1] = v_vec[1]
        s = np.sum(arry*timevector, axis=1)
        dv = np.array([arry[1][0] * 2 * dt, arry[0][0] * 2 * dt])
        updates = np.array([(0, 0), dv, (0, 0)])
        updates = np.rot90(updates, k=1, axes=(0, 1))
        disp_mtrx[0][2] = s[0]
        disp_mtrx[1][2] = s[1]
        disp_mtrx[0][1] = v_vec[0]
        disp_mtrx[1][1] = v_vec[1]
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
        '''

        '''
        basis = np.array([(np.cos(heading), -np.sin(heading)),
                         (np.sin(heading), np.cos(heading))])
        calc = xy*basis
        #print(f'heading: {heading}')
        #print(f'basis: {basis}')
        #print(f'rotated: {calc}')
        return np.around(np.sum(calc, axis=1), decimals=CALC_PRECISION)


class Moveable():
    '''
    A class that instanciates a moveable object and interfaces with the
    Physics object to make the simulation easier to interact with
    '''

    def __init__(self, loc=np.array([0., 0]), accel=np.array([0., 0]), vel=np.array([0., 0])):
        self.heading = 0
        self.theta = 0
        self.phi = accel[1] * np.pi / 180
        self.acceleration = np.array(accel)
        self.velocity = np.array(vel)
        self.position = np.array(loc)

    def move(self, dt=0.05):
        '''
        Calculates the displacement given a matrix of coefficients
        for the equation s = at^2 + bt^1 + c
        The matrix must be in the form np.array([(ax, bx, cx), (ay, by, cy)])
        The new location is stored in the original matrix and given
        by cx and cy
        Returns an updated matrix and heading
        '''
        #print('\n')
        self.theta += self.phi
        arry = np.array([self.acceleration, self.velocity])
        #print(f'arry: {arry}')
        timevector = np.array([float(dt**2), dt])
        calc = arry*timevector
        #print(f'calc: {calc}')
        ds = np.sum(calc)
        dv = self.acceleration * dt
        #print(f'dv: {dv}')
        #print(f'vel: {self.velocity}')
        self.velocity += dv
        #print(f'velocity: {self.velocity}')
        #print(f'theta, phi: {self.theta}, {self.phi}')
        real_ds = Physics.rotateaxis(np.array([ds, 0]), self.theta)
        #print(f'ds: {ds}')
        #print(f'real_ds: {real_ds}')
        self.position += real_ds
        #print(self.position)
        # Figure out new heading via arctan(vy/vx)
        # vx, vy = Physics.rotateaxis(self.velocity, self.theta)
        '''
        if vx < 0:
            if vy < 0:
                self.theta = np.arctan(vy/vx) - np.pi
            else:
                self.theta = np.arctan(vy/vx) + np.pi
        elif vx == 0:
            if vy == 0:
                pass
            elif vy > 0:
                self.theta = np.pi/2
            else:
                self.theta = np.pi/-2
        else:
            self.theta = np.arctan(vy/vx)
        '''

    def get_loc(self):
        return int(self.position[0]), int(self.position[1])

    def set_acceleration(self, accel):
        #print(f'accelerating: {accel}')
        self.phi = accel[1] * np.pi / 180
        self.acceleration = np.array([accel[0]/2., 0])
        #print(f'finished accelerating: {self.acceleration}')

    def get_velocity(self):
        return self.velocity[0], self.velocity[1]

    def get_heading(self):
        return self.phi

    def get_direction(self):
        return self.theta
