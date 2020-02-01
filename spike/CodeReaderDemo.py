class CodeParser():

    #Parsing variables
    PORT = ''
    OPERATION = ''
    NUMBER = ''
    JUMP = ''
    FUNC = ''
    T1 = ''
    T2 = ''
    #FUNCTIONS = []

    path = ''
    SPEED = 0
    ANGLE = 0

    lineNum = 0

    #Parsing libraries (or "keywords" if you wanna not sound like an arrogant prick)
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]


    #Initialize the CodeParser
    def __init__(self, path):
        self.path = "Racer.txt"
        self.SPEED = 0
        self.ANGLE = 0

        #Open racer file
        self.racer = open(self.path, "r")

        #Read lines in
        if self.racer.mode == "r":
            self.code = self.racer.readlines()
            self.racer.close()

        #Remove whitespace from file
        line = 0
        while line < len(self.code):
            terms = self.code[line].split()
            if len(terms) == 0:
                self.code.pop(line)
            line += 1
                    
        self.analyzer()


    #Analyze
    def analyzer(self):

        #Keep reading lines until you run out of lines
        while self.lineNum < len(self.code):

            #Split code line into terms
            terms = self.code[self.lineNum].split()

            #If there are 5 terms go to conditional jumping
            if len(terms) == 5:
                self.JUMP = terms[0]
                self.FUNC = terms[1]
                self.T1 = terms[2]
                self.OPERATION = terms[3]
                self.T2 = terms[4]

                print("Conditonally jumping")
                self.cndJump()

            #If there are 3 terms go to math
            if len(terms) == 3:   
                self.PORT = terms[0]
                self.OPERATION = terms[1]
                self.NUMBER = terms[2]
                
                print("Mathing")
                self.oprSwitch()

            #If there are 2 terms go to jumping
            if len(terms) == 2:
                self.JUMP = terms[0]
                self.FUNC = terms[1]
                
                print("Jumping")
                self.jump()

            #If there is 1 term recognize that it is a function
            if len(terms) == 1:
                
                print("Function")
                #self.FUNCTIONS.append(terms[0])

            #Print speed and angle after each line read
            print("Speed:", self.SPEED)
            print("Angle:", self.ANGLE)
            self.lineNum += 1

    #Function to add number to port
    def addPort(self):
        
        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED + int(self.NUMBER)
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE + int(self.NUMBER)


    #Function to subtract number from port 
    def subPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED - self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE - self.NUMBER


    #Function to multply port by number
    def mltPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED * self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE * self.NUMBER

        
    #Function to divide port by number    
    def divPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED / self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE / self.NUMBER


    #Function to set port to number
    def setPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.NUMBER


    #Switch to correct function
    def oprSwitch(self):

        #Cast variables to ints
        self.NUMBER = int(self.NUMBER)
        self.ANGLE = int(self.ANGLE)
        self.SPEED = int(self.SPEED)

        #Switcherrrrr
        oprSwitcher = {
            1: self.mltPort,
            2: self.addPort,
            4: self.subPort,
            6: self.divPort,
            20: self.setPort
            }

        #Turn ascii operation into numeral and then go to the switch
        self.nOperation = ord(self.OPERATION) - 41
        f = oprSwitcher.get(self.nOperation, "invalid operation")
        f()

    #Function to jump to spcific line
    def jump(self):

        #Find the function to jump to and then set lineNum to where it is in the txt file
        for num, i in enumerate(self.code):
            terms = self.code[num].split()
            if self.FUNC == terms[0]:
                self.lineNum = num
                return


    #Function to jump to specific line conditionally
    def cndJump(self):

        #Set T1 and T2 to their ports
        if self.T1 == "THROTTLE":
            self.T1 = self.SPEED
        if self.T1 == "TURN":
            self.T1 = self.ANGLE

        if self.T2 == "THROTTLE":
            self.T2 = self.SPEED
        if self.T2 == "TURN":
            self.T2 = self.ANGLE

        #Make T1 and T2 ints for comparison
        self.T1 = int(self.T1)
        self.T2 = int(self.T2)

        #If T1 is less than T2, jump
        if self.OPERATION == "<":
            if self.T1 < self.T2:
                for num, i in enumerate(self.code):
                    terms = self.code[num].split()
                    if self.FUNC == terms[0]:
                        self.lineNum = num
                        return

        #If T1 is less than or equal to T2, jump    
        if self.OPERATION == "<=":
            if self.T1 <= self.T2:
                for num, i in enumerate(self.code):
                    terms = self.code[num].split()
                    if self.FUNC == terms[0]:
                        self.lineNum = num
                        return

        #If T1 is greater than T2, jump
        if self.OPERATION == ">":
            if self.T1 > self.T2:
                for num, i in enumerate(self.code):
                    terms = self.code[num].split()
                    if self.FUNC == terms[0]:
                        self.lineNum = num
                        return
                    
        #If T1 is greater than or equal to T2, jump
        if self.OPERATION == ">=":
            if self.T1 >= self.T2:
                for num, i in enumerate(self.code):
                    terms = self.code[num].split()
                    if self.FUNC == terms[0]:
                        self.lineNum = num
                        return

        #If T1 is equal to T2, jump
        if self.OPERATION == "=":
            if self.T1 == self.T2:
                for num, i in enumerate(self.code):
                    terms = self.code[num].split()
                    if self.FUNC == terms[0]:
                        self.lineNum = num
                        return

        #If T1 is not equal to T2, jump
        if self.OPERATION == "!=":
            if self.T1 != self.T2:
                for num, i in enumerate(self.code):
                    terms = self.code[num].split()
                    if self.FUNC == terms[0]:
                        self.lineNum = num
                        return
        

#This is just for testing and running the code
green = CodeParser("racer.txt")
CodeParser.__init__
