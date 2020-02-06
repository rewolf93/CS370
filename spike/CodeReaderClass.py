class CodeParser():

    #Parsing variables
    PORT = ''
    OPERATION = ''
    NUMBER = ''

    #Parsing libraries (or "keywords" if you wanna not sound like an arrogant prick)
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]

    #Initialize the CodeParser
    def __init__(self):
        self.PATH = "Racer.txt"
        self.SPEED = 0
        self.ANGLE = 0
        self.analyzer()

    #Analyze
    def analyzer(self):

        #Open racer file
        self.racer = open(self.PATH, "r")

        #Break down lines into individual parts
        self.lexeme = ''

        #Check if file is readable and then read lines
        if self.racer.mode == "r":
            self.code = self.racer.readlines()

            #For each line in the .txt file reset all stored variables then...
            for self.line in self.code:
                self.PORT = ''
                self.OPERATION = ''
                self.NUMBER = ''
                self.lexeme = ''

                #For each character in the line...
                for self.i, self.char in enumerate(self.line):

                    #If the character does not equal whitespace add it to the word
                    if self.char != self.WHITESPACE:
                       self.lexeme += self.char

                    #If the character index is less than the length of the line and...
                    if (self.i + 1 < len(self.line)):

                        #If the character after i is whitespace or a newline check if the word is in "keywords"
                        if self.line[self.i + 1] == self.WHITESPACE or self.line[self.i + 1] == '\n':
                            if self.lexeme in self.PORTS:
                                self.PORT = self.lexeme
                            if self.lexeme in self.OPERATIONS:
                                self.OPERATION = self.lexeme
                            if bool([self.ele for self.ele in self.NUMBERS if(self.ele in self.lexeme)]):
                                self.NUMBER = self.lexeme

                            #Reset the word stored
                            self.lexeme = ''
                            
                    #If the index of the character is one less than the length of the line check if the word is in "keywords"
                    if (self.i == len(self.line) - 1):
                        if self.lexeme in self.PORTS:
                            self.PORT = self.lexeme
                        if self.lexeme in self.OPERATIONS:
                            self.OPERATION = self.lexeme
                        if bool([self.ele for self.ele in self.NUMBERS if(self.ele in self.lexeme)]):
                            self.NUMBER = self.lexeme

                        #Reset the word stored
                        self.lexeme = ''

                #Parse the line of code   
                self.oprSwitch()

                
                print('Speed: %d' % self.SPEED)
                print('Angle: %d' % self.ANGLE)

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

        #Cast variables to ints cause Python is a little garbo
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

#This is just for testing and running the code
#green = CodeParser()
#CodeParser.__init__
