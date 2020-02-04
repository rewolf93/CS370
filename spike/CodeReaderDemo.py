class CodeParser():

    #Parsing variables
    SPEED = 0
    ANGLE = 0

    lineNum = 0

    #Parsing libraries (or "keywords")
    PORTS = ["THROTTLE", "TURN"]


#Initialize the CodeParser
    def __init__(self, path):
        path = "Racer.txt"
        self.SPEED = 0
        self.ANGLE = 0

        #Open racer file
        racer = open(path, "r")

        #Read lines in
        self.code = racer.readlines()
        racer.close()

        #Remove whitespace from file
        line = 0
        while line < len(self.code):
            terms = self.code[line].split()
            if len(terms) == 0:
                self.code.pop(line)
            else:
                line += 1

        #self.analyzer()

#Analyze
    def analyzer(self):

        #Keep reading lines until you run out of lines
        while self.lineNum < len(self.code):

            #Split code line into terms
            terms = self.code[self.lineNum].split()

            #Go to add function
            if terms[0] == "add":
                self.addPort(terms)

            if terms[0] == "sub":
                self.subPort(terms)

            if terms[0] == "mpy":
                self.mpyPort(terms)

            if terms[0] == "div":
                self.divPort(terms)

            if terms[0] == "set":
                self.setPort(terms)

            if terms[0] == "jmp":
                self.jump(terms)

            if terms[0] == "lst":
                self.lstJump(terms)

            if terms[0] == "lte":
                self.lteJump(terms)

            if terms[0] == "grt":
                self.grtJump(terms)

            if terms[0] == "gte":
                self.gteJump(terms)

            if terms[0] == "eqt":
                self.eqtJump(terms)

            if terms[0] == "nte":
                self.nteJump(terms)

            #Print speed and angle after each line read
            print("Speed:", self.SPEED)
            print("Angle:", self.ANGLE)
            self.lineNum += 1

#Function to add number to port
    def addPort(self, terms):
        
        if terms[1] == "THROTTLE":
            self.SPEED = self.SPEED + int(terms[2])
            
        if terms[1] == "TURN":
            self.ANGLE = self.ANGLE + int(terms[2])


#Function to subtract number from port 
    def subPort(self, terms):

        if terms[1] == "THROTTLE":
            self.SPEED = self.SPEED - int(terms[2])
            
        if terms[1] == "TURN":
            self.ANGLE = self.ANGLE - int(terms[2])


#Function to multply port by number
    def mpyPort(self, terms):

        if terms[1] == "THROTTLE":
            self.SPEED = self.SPEED * int(terms[2])
            
        if terms[1] == "TURN":
            self.ANGLE = self.ANGLE * int(terms[2])

        
#Function to divide port by number    
    def divPort(self, terms):

        if terms[1] == "THROTTLE":
            self.SPEED = self.SPEED / int(terms[2])
            
        if terms[1] == "TURN":
            self.ANGLE = self.ANGLE / int(terms[2])


#Function to set port to number
    def setPort(self, terms):

        if terms[1] == "THROTTLE":
            self.SPEED = int(terms[2])
            
        if terms[1] == "TURN":
            self.ANGLE = int(terms[2])

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
        for i, term in enumerate(terms):
            if terms[i] == "THROTTLE":
                terms[i] = self.SPEED
            if terms[i] == "TURN":
                terms[i] = self.ANGLE
        
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

#This is just for testing and running the code
#green = CodeParser("racer.txt")
#CodeParser.__init__
