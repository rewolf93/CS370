port = ''
operation = ''
number = ''
speed = 0
angle = 0

def main():

    global port
    global operation
    global number
    
    #Open racer file
    racer = open("Racer.txt", "r")

    #Define symbols
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]
    
    #Break down symbols together
    lexeme = ''
    if racer.mode == "r":
        code = racer.readlines()
        for line in code:
            port = ''
            operation = ''
            number = ''
            lexeme = ''
            for i, char in enumerate(line):
                if char != WHITESPACE:
                   lexeme += char
                if (i + 1 < len(line)):
                    if line[i + 1] == WHITESPACE or line[i + 1] == '\n':
                        if lexeme in PORTS:
                            port = lexeme
                        if lexeme in OPERATIONS:
                            operation = lexeme
                        if bool([ele for ele in NUMBERS if(ele in lexeme)]):
                            number = lexeme
                        lexeme = ''
                if (i == len(line) - 1):
                    if lexeme in PORTS:
                        port = lexeme
                    if lexeme in OPERATIONS:
                        operation = lexeme
                    if bool([ele for ele in NUMBERS if(ele in lexeme)]):
                        number = lexeme
                    lexeme = ''
                    
            oprSwitch()

def addPort():
    global port
    print("I'm gonna add", number, "to", port)
    
def subPort():
    global port
    
    print("I'm gonna subtract", number, "from", port, "!")
    
def mltPort():
    global port
    
    print("I'm gonna multiply", port, "by", number, "!")
    
    
def divPort():
    global port

    print("I'm gonna divide", port, "by", number, "!")

def setPort():
    global port

    print("I'm gonna set", port, "to", number, "!")
    
def oprSwitch():

    global port

    if port == "THROTTLE":
        port = "speed"
    if port == "TURN":
        port = "angle"
    
    oprSwitcher = {
        1: mltPort,
        2: addPort,
        4: subPort,
        6: divPort,
        20: setPort
        }

    global operation
    nOperation = ord(operation) - 41
    f = oprSwitcher.get(nOperation, "invalid operation")
    f()
main()
