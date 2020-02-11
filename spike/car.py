import pygame as pg
import numpy as np
from simulation import *


class Car(pg.sprite.Sprite, Moveable):

    def __init__(self, image, startpos=(0., 0), accel=np.array([0., 0]), vel=np.array([0., 0])):
        pg.sprite.Sprite.__init__(self, self.groups)
        Moveable.__init__(self, loc=startpos, accel=accel, vel=vel)
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (50, 50))
        self.image = pg.transform.rotate(self.image, -90)
        self._originalimage = self.image
        self.rect = self.image.get_rect()
        self.old_rect = self.image.get_rect()
        self.update()

    def move(self):
        # print('car moving')
        Moveable.move(self, dt=0.05)
        self.update()

    def update(self):
        self.old_rect.center = self.rect.center
        self.pos = Moveable.get_loc(self)
        rotation = -(Moveable.get_direction(self) / np.pi) * 180
        self.image = pg.transform.rotate(self._originalimage, rotation)
        self.rect.center = self.pos

    def accelerate(self, a_vec):
        a_vec = np.array(a_vec)
        Moveable.set_acceleration(self, a_vec)


class SuperCar(pg.sprite.Sprite, Moveable):

    def __init__(self, image, path, startpos=(0., 0)):
        pg.sprite.Sprite.__init__(self, self.groups)
        Moveable.__init__(self, loc=startpos)
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (50, 50))
        self.image = pg.transform.rotate(self.image, -90)
        self._originalimage = self.image
        self.rect = self.image.get_rect()
        self.old_rect = self.image.get_rect()
        self.cyclewait = 0
        self.lineNum = 0

        racer = open(path, "r")
        self.code = racer.readlines()
        racer.close()

        line = 0
        while line < len(self.code):
            terms = self.code[line].split()
            if len(terms) == 0:
                self.code.pop(line)
            else:
                line += 1

        self.update()

    def move(self):
        dt = 0.05
        temp = self.analyzer()
        self.theta += self.phi
        arry = np.array([self.acceleration, self.velocity])
        timevector = np.array([float(dt**2), dt])
        calc = arry*timevector
        ds = np.sum(calc)
        dv = self.acceleration * dt
        self.velocity += dv
        real_ds = Physics.rotateaxis(np.array([ds, 0]), self.theta)
        self.position += real_ds
        self.update()
        #print(self.acceleration)
        return temp

    def update(self):
        self.old_rect.center = self.rect.center
        self.pos = Moveable.get_loc(self)
        rotation = -(Moveable.get_direction(self) / np.pi) * 180
        self.image = pg.transform.rotate(self._originalimage, rotation)
        self.rect.center = self.pos

    def accelerate(self, a_vec):
        a_vec = np.array(a_vec)
        Moveable.set_acceleration(self, a_vec)

    def analyzer(self):
        #print(self.cyclewait)
        #print('In analyzer')
        if self.cyclewait > 0:
            #print('Cycling')
            self.cyclewait -= 1
            return True

        #Keep reading lines until you run out of lines
        elif self.lineNum < len(self.code):

            #Split code line into terms
            terms = self.code[self.lineNum].split()
            #print(terms)
            #Go to add function
            if terms[0] == "add":
                self.addPort(terms)

            elif terms[0] == "sub":
                self.subPort(terms)

            elif terms[0] == "mpy":
                self.mpyPort(terms)

            elif terms[0] == "div":
                self.divPort(terms)

            elif terms[0] == "set":
                self.setPort(terms)

            elif terms[0] == "jmp":
                self.jump(terms)

            elif terms[0] == "lst":
                self.lstJump(terms)

            elif terms[0] == "lte":
                self.lteJump(terms)

            elif terms[0] == "grt":
                self.grtJump(terms)

            elif terms[0] == "gte":
                self.gteJump(terms)

            elif terms[0] == "eqt":
                self.eqtJump(terms)

            elif terms[0] == "nte":
                self.nteJump(terms)

            elif terms[0] == "noop":
                self.cyclewait = int(terms[1])

            #Print speed and angle after each line read
            self.lineNum += 1
        return self.lineNum < len(self.code) or self.cyclewait > 0


    #Function to add number to port
    def addPort(self, terms):
        
        if terms[1] == "THROTTLE":
            self.acceleration[0] += int(terms[2])
            
        elif terms[1] == "TURN":
            self.acceleration[1] += int(terms[2])


    #Function to subtract number from port 
    def subPort(self, terms):

        if terms[1] == "THROTTLE":
            self.acceleration[0] -= int(terms[2])
            
        elif terms[1] == "TURN":
            self.acceleration[1] -= int(terms[2])


    #Function to multply port by number
    def mpyPort(self, terms):

        if terms[1] == "THROTTLE":
            self.acceleration[0] *= int(terms[2])
            
        elif terms[1] == "TURN":
            self.acceleration[1] *= int(terms[2])

        
    #Function to divide port by number    
    def divPort(self, terms):

        if terms[1] == "THROTTLE":
            self.acceleration[0] /= int(terms[2])
            
        elif terms[1] == "TURN":
            self.acceleration[1] /= int(terms[2])


    #Function to set port to number
    def setPort(self, terms):
        if terms[1] == "THROTTLE":
            Moveable.update_acceleration(self, magnitude=int(terms[2]))
            
        elif terms[1] == "TURN":
            Moveable.update_acceleration(self, direction=float(terms[2])/100.)


    #Function to jump to spcific line
    def jump(self, terms):

        #Find the function to jump to and then set lineNum to where it is in the txt file
        for num, i in enumerate(self.code):
            i = self.code[num].split()
            if i[0] == terms[1]:
                self.lineNum = num
                return

    #Function to change port to number
    def portToNum(self, terms):
        for i, _ in enumerate(terms):
            if terms[i] == "THROTTLE":
                terms[i] = self.acceleration[0]
            if terms[i] == "TURN":
                terms[i] = self.acceleration[1]
        
    #Function to jump if comparison is less than
    def lstJump(self, terms):
        self.portToNum(terms)
        if int(terms[1]) < int(terms[2]):
            for num, i in enumerate(self.code):
                i = self.code[num].split()
                if i[0] == terms[4]:
                    self.lineNum = num
                    return
                
    #Function to jump if comparison is less than or equal to
    def lteJump(self, terms):
        self.portToNum(terms)
        if int(terms[1]) <= int(terms[2]):
            for num, i in enumerate(self.code):
                i = self.code[num].split()
                if i[0] == terms[4]:
                    self.lineNum = num
                    return
                
    #Function to jump if comparison is greater than
    def grtJump(self, terms):
        self.portToNum(terms)
        if int(terms[1]) > int(terms[2]):
            for num, i in enumerate(self.code):
                i = self.code[num].split()
                if i[0] == terms[4]:
                    self.lineNum = num
                    return
                
    #Function to jump if comparison is less than or equal to
    def gteJump(self, terms):
        self.portToNum(terms)
        if int(terms[1]) >= int(terms[2]):
            for num, i in enumerate(self.code):
                i = self.code[num].split()
                if i[0] == terms[4]:
                    self.lineNum = num
                    return

    #Function to jump if comparison is equal to
    def eqtJump(self, terms):
        self.portToNum(terms)
        if int(terms[1]) == int(terms[2]):
            for num, i in enumerate(self.code):
                i = self.code[num].split()
                if i[0] == terms[4]:
                    self.lineNum = num
                    return

    #Function to jump if comparison is not equal to
    def nteJump(self, terms):
        self.portToNum(terms)
        if int(terms[1]) != int(terms[2]):
            for num, i in enumerate(self.code):
                i = self.code[num].split()
                if i[0] == terms[4]:
                    self.lineNum = num
                    return
