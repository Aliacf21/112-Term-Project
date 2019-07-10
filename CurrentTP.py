import dialogue
import classButton
from tkinter import *
from random import *
import copy
from stringFormating import *
from movingCircle import *



####################################
# init
####################################

#inspired from the 15-112 website
def init(data):
    data.countPaintMix=0
    data.timerCounter =0
    # There is only one init, not one-per-mode
    data.mode = "welcome"
    data.welcomeImage = PhotoImage(file="currentFarm.gif")
    data.farmerJoe = PhotoImage(file="farmer.gif")
    data.fence = PhotoImage(file="fence.gif")
    data.suzieImg = PhotoImage(file="midSuze.gif")
    data.joeList = dialogue.joeTxt()
    data.yesJoe =dialogue.yesToJoe()
    data.suzieP2 = dialogue.getSuzieTxtP2()
    data.widthRadiusPlayGameSuzie = 200
    data.heightRadiusPlayGameSuzie = 50
    data.i = 0
    data.rows, data.cols = 10, 10
    data.margin = 20
    data.cellSize = (data.width-2*data.margin)//data.rows
    data.board, data.board1 = makeBoard(), makeBoard()
    data.color =["red", "yellow", "blue", "orange", "purple", "green"]
    data.j = 0
    data.cellSizeAnimal = data.height//13
    drawFence(data)
    drawFence1(data)
    data.paintTheFenceCount=0
    data.redLevel = False
   # data.paintColors = PhotoImage(file="Paint Colors")
    data.lastPaint = []
    data.outsideTheRedLine = False
    data.outsideTheBlueLine = False 
    data.outsideTheGreenLine = False 
    data.outsideTheOrangeLine= False 
    data.outsideThePurpleLine = False 
    data.outsideTheYellowLine = False
    data.outsideTheRedLine1 = False
    data.outsideTheBlueLine1 = False 
    data.outsideTheGreenLine1 = False 
    data.outsideTheOrangeLine1= False 
    data.outsideThePurpleLine1 = False 
    data.outsideTheYellowLine1 = False
    data.suzieP2 = dialogue.getSuzieTxtP2()
    data.txt = " "
    data.animal = PhotoImage(file="dogSmall.gif")
    data.suzie = dialogue.getSuzieTxtP1()
    #init data for Animals
    data.boardAnimals = makeBoard1()
    data.numBoard = makeBoardNum()
    data.paintMixing1 = "Click on two colors to see what color they make!"
    data.paintMixing2 = " "
    #inputNum(data)
    data.num = randint(1,10)
    data.timePast = 0
    data.amoutYes=0
    data.green, data.orange, data.purple = False, False, False
    #init 
    data.welcomeButton = classButton.abstract(data, data.width//2, data.height//2+data.height//5, text="Welcome")
    
    data.helpButton = classButton.abstract(data, data.width//2, data.height//2+data.height//3, text="Help")
    
    data.countingUp=0
    data.suzieImg1 = PhotoImage(file="gSuze.gif")
    #SuzieP1
    data.yesButton = classButton.blank(data, data.width//2+data.width//4, data.height//2, text="Yes", fill="springgreen")
    data.noButton = classButton.blank(data, data.width//2++data.width//4, data.height//2+data.height//6, text="No", fill="springgreen")
    
    #click the Ball
    data.ballClicks=[]
    data.yellowCircleExists = False
    data.clickInYellow1  = False 
    data.clickInRed1 = False 
    data.clickInBlue1 = False 
    data.clickInYellow2 = False 
    data.clickInRed2 = False 
    data.clickInBlue2 = False
    data.alphabetList = []
    data.myDigit=makeGrid()
    data.saidYes=False
    data.saidNo=False
    data.computerGuess = None
    myW =data.width//2
    myH = data.height//6
    data.yellowButton= Yellow(myW//2, myH)
    data.redButton = Red(myW, myH)
    data.blueButton = Blue(myW+myW//2, myH)
    data.blue, data.red, data.yellow = False, False, False
    data.movingYellowCircle1 = Yellow(myW//4, myH*3)
    data.movingRedCircle1 = Red(myW*2-myW//4, myH*3)
    data.movingBlueCircle1 = Blue(myW*2-myW//4, myH*3)
    data.orangeCircle = Orange(myW, myH*3)
    data.greenCircle = Green(myW, myH*3)
    data.purpleCircle =Purple(myW, myH*3)
    data.timerCount=0
    data.orangeCircleMade = False
    data.greenCircleMade = False
    data.purpleCircleMade = False
    data.previousMode = None
    data.canMove = False
    data.yesSuzie = False
    data.yesSuzieTxt = dialogue.yesToSuzie()
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "welcome"): welcomeMousePressed(event, data)
    elif (data.mode == "playGameJoe"):   playGameJoeMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)
    elif (data.mode == "instructions"): instructionsMousePressed(event, data)
    elif (data.mode =="doggie"): doggieMousePressed(event,data)
    elif (data.mode == "countTheAnimal"): countTheAnimalMousePressed(event, data)
    elif (data.mode == "playGameSuzie"): playGameSuzieMousePressed(event, data)
    elif (data.mode == "paintTheFence"): paintTheFenceMousePressed(event, data)
    elif (data.mode == "playGameSuzieP2"): playGameSuzieP2MousePressed(event, data)
    elif (data.mode == "paintMixing"): paintMixingMousePressed(event, data)
    elif (data.mode == "paintTheFence2"): paintTheFence2MousePressed(event, data)
    elif (data.mode == "learnAlphabet"): learnAlphabetMousePressed(event, data)
    elif (data.mode == "goodBye"): goodByeMousePressed(event, data)
    

def keyPressed(event, data):
    if (data.mode == "welcome"): welcomeKeyPressed(event, data)
    elif (data.mode == "playGameJoe"):   playGameKeyJoePressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)
    elif (data.mode == "instructions"): instructionsKeyPressed(event, data)
    elif (data.mode =="doggie"): doggieKeyPressed(event,data)
    elif (data.mode == "countTheAnimal"): countTheAnimalKeyPressed(event, data)
    elif (data.mode == "playGameSuzie"): playGameSuzieKeyPressed(event, data)
    elif (data.mode == "paintTheFence"): paintTheFenceKeyPressed(event, data)
    elif (data.mode == "playGameSuzieP2"): playGameSuzieP2KeyPressed(event, data)
    elif (data.mode == "paintMixing"): paintMixingKeyPressed(event, data)
    elif (data.mode == "paintTheFence2"): paintTheFence2KeyPressed(event, data)
    elif (data.mode == "learnAlphabet"): learnAlphabetKeyPressed(event, data)
    elif (data.mode == "goodBye"): goodByeKeyPressed(event, data)


def mouseMoved(event, data):
    if (data.mode == "countTheAnimal"): countTheAnimalMouseMoved(event, data)

def mouseDragged(event, data):
    if (data.mode == "countTheAnimal"): countTheAnimalMouseDragged(event, data)

def timerFired(data):
    pass
    if (data.mode == "welcome"): welcomeTimerFired(data)
    elif (data.mode == "playGameJoe"):   playGameJoeTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)
    elif (data.mode =="doggie"): doggieTimerFired(data)
    elif (data.mode == "instructions"): instructionsTimerFired(data)
    elif (data.mode == "countTheAnimal"): countTheAnimalTimerFired(data)
    elif (data.mode == "playGameSuzie"): playGameSuzieTimerFired(data)
    elif (data.mode == "paintTheFence"): paintTheFenceTimerFired(data)
    elif (data.mode == "playGameSuzieP2"): playGameSuzieP2TimerFired(data)
    elif (data.mode == "paintMixing"): paintMixingTimerFired(data)
    elif (data.mode == "paintTheFence2"): paintTheFence2TimerFired(data)
    elif (data.mode == "learnAlphabet"): learnAlphabetTimerFired(data)
    elif (data.mode == "goodBye"): goodByeTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "welcome"): welcomeRedrawAll(canvas, data)
    elif (data.mode == "playGameJoe"):   playGameJoeRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    elif (data.mode == "instructions"): instructionsRedrawAll(canvas, data)
    elif (data.mode =="doggie"): doggieRedrawAll(canvas, data)
    elif (data.mode == "countTheAnimal"): countTheAnimalRedrawAll(canvas, data)
    elif (data.mode == "playGameSuzie"): playGameSuzieRedrawAll(canvas, data)
    elif (data.mode == "paintTheFence"): paintTheFenceRedrawAll(canvas, data)
    elif (data.mode == "playGameSuzieP2"): playGameSuzieP2RedrawAll(canvas, data)
    elif (data.mode == "paintMixing"): paintMixingRedrawAll(canvas, data)
    elif (data.mode == "paintTheFence2"): paintTheFence2RedrawAll(canvas, data)
    
    elif (data.mode == "learnAlphabet"): learnAlphabetRedrawAll(canvas, data)
    elif (data.mode == "goodBye"): goodByeRedrawAll(canvas, data)
    
###########
#common Helper functions
#######
def reset(data):
    data.i = 0
    data.txt = " "
    
def makeBoard():
# inspiration from tetris
    rows = 10
    cols = 10
    cellSize = 20
    margins = 25
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("white")
        board.append(row)
    return board
    
def makeBoard1():
# inspiration from tetris
    rows = 13
    cols = 13
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("white")
        board.append(row)
    return board
    
def makeBoardNum():
# inspiration from tetris
    rows = 13
    cols = 13
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("")
        board.append(row)
    return board
    
    
def drawCellAnimal(canvas, data, row, col, fill):
    # inspiration from tetris
    x = col*data.cellSizeAnimal
    y= row*data.cellSizeAnimal
    x1 = x + data.cellSizeAnimal
    y1= y + data.cellSizeAnimal
    canvas.create_oval(x,y,x1,y1, fill=fill, width = 0)
    
    
def drawCellAnimalTxt(canvas, data, row, col, text):
    # inspiration from tetris
    x = col*data.cellSizeAnimal+data.cellSizeAnimal//2
    y= row*data.cellSizeAnimal++data.cellSizeAnimal//2
    canvas.create_text(x,y,text=text, font="Arial 26 bold")

    
def drawCell(canvas, data, row, col, fill):
    # inspiration from tetris
    x = (col*data.cellSize)+data.margin
    y= (row*data.cellSize)+data.margin
    x1 = x + data.cellSize
    y1= y+data.cellSize
    canvas.create_rectangle(x,y,x1,y1, fill=fill, width = 0)
    
def doneSpeak(data):
    if data.txt[-1][-1]== "?":
        return True
       

####################################
# Welcome mode
####################################


def welcomeMousePressed(event, data):
    # print(data.helpButton.y)
    # print(data.welcomeButton.y)
    if data.helpButton.clickInButton(event.x, event.y):
        data.mode = "instructions"
        
    elif data.welcomeButton.clickInButton(event.x, event.y):
        data.mode = "playGameJoe"
        

def welcomeKeyPressed(event, data):
    pass

def welcomeTimerFired(data):
    data.timerDelay= 2500
    
def buttonClick(data):
    pass

def welcomeRedrawAll(canvas, data):
    w, h = data.width//2, data.height//2
    canvas.create_image(w, h, image = data.welcomeImage)
    data.welcomeButton.draw(canvas)
    data.helpButton.draw(canvas)

  
####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if event.keysym=="space":
        data.mode = data.previousMode

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_image(data.width//2, data.height//2+data.width//6, image=data.fence)
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2, 100,
                       text="Try and get the fence to look like this!", font="Aril 18 bold" )
    canvas.create_text(data.width//2, 130,
                       text="Work from left post to right post!", font="Aril 18 bold" )
    canvas.create_text(data.width//2, 160,
                       text="Click backspace to return", font="Aril 18 bold")
                       
####################################
# instructions mode
####################################

def instructionsMousePressed(event, data):
    pass

def instructionsKeyPressed(event, data):
    if event.keysym=="space":
        data.mode = "welcome"

def instructionsTimerFired(data):
    pass

def instructionsRedrawAll(canvas, data):
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2, 100,
                       text="Welcome to the game!", font="Aril 18 bold" )
    canvas.create_text(data.width//2, data.height//2, text="If you want to change the page, press the right arrow key",font="Aril 18 bold") 
    canvas.create_text(data.width//2, data.height//2+30,
                       text="But, make sure the characters are done speaking",font="Aril 18 bold" )  
    canvas.create_text(data.width//2, data.height//2+60, text= "Or else the page won't move", font="Aril 18 bold")
    canvas.create_text(data.width//2, 130,
                       text="Click backspace to return", font="Aril 18 bold")
                       
    

####################################
# playGameJoe mode
####################################

def playGameJoeMousePressed(event, data):
    if data.yesButton.clickInButton(event.x, event.y):
        data.txt= "That is great to hear!"
        data.nextMode = "doggie"
        data.saidYes=True
        
    elif data.noButton.clickInButton(event.x, event.y):
        data.txt="I'm sorry to hear that"
        data.nextMode = "goodBye"
        data.canMove = True
        data.saidNo=True


def playGameKeyJoePressed(event, data):
    if data.canMove:
        if (event.keysym=="Left"):
            data.mode = "welcome"
        if (event.keysym=="Right"):
            reset(data)
            data.canMove = False
            data.timerDelay= 2500
            data.saidYes = False
            data.saidNo = False
            data.j=0
            data.mode = data.nextMode
            
        if (event.keysym == 'h'):
            data.mode = "help"
    
        
        
def playGameJoeTimerFired(data):
    if data.saidYes:
        if data.j < len(data.yesJoe):
            data.txt=data.yesJoe[data.j]
            data.j+=1
        if data.txt[-1]=="continue":
            data.canMove = True
            
      #  data.canMove= True
                    
    if data.saidNo:
        data.timePast+=1
        if data.timePast==1:
            data.txt=" "
            data.mode="goodBye"
            
    if data.i < len(data.joeList):
            data.txt=data.joeList[data.i]
            data.i+=1
        
            

def playGameJoeRedrawAll(canvas, data):
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2,  100,
                       text=data.txt, font="Arial 20 bold")
    canvas.create_image(data.width//4, data.height//2+data.height//8, image = data.farmerJoe)
    if doneSpeak(data):
        data.yesButton.draw(canvas)
        data.noButton.draw(canvas)
    
###################################
# Doggie mode
###################################

def doggieMousePressed(event, data):
    pass
    
def doggieKeyPressed(event, data):
    pass
    
def doggieTimerFired(data):
    data.countingUp +=1
    if data.countingUp==2:
        data.mode="countTheAnimal"
    
def doggieRedrawAll(canvas, data): 
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2,  100,
                       text="Try and remember how many dogs there are!" , font="Aril 20 bold")
    canvas.create_text(data.width//2,  120,
                       text="On, the next screen draw the number you think there are!" , font="Aril 20 bold")
    offset=100
    offset1 = 100
    if data.num<=5:
        for i in range(data.num):
            canvas.create_image(offset, data.height//2, image=data.animal)
            offset+=100
    elif data.num%2==0:
        for i in range(data.num//2):
            canvas.create_image(offset, data.height//2, image=data.animal)
            canvas.create_image(offset, data.height//2+100, image=data.animal)
            offset+=100
    else:
        for i in range(data.num//2):
            canvas.create_image(offset, data.height//2, image=data.animal)
            offset+=100
        for i in range(data.num//2, data.num):
            canvas.create_image(offset1, data.height//2+100, image=data.animal)
            offset1+=100
    
        
    
    
####################################
# countTheAnimal mode
####################################
def makeGrid():
    board=[]
    for i in range(10):
        thisRow=[]
        for j in range(10):
            thisRow.append(0)
        board.append(thisRow)
    return board
    


    
def countTheAnimalMousePressed(event, data):
    pass
        

def countTheAnimalMouseMoved(event, data):
    return None


def countTheAnimalMouseDragged(event, data):
    x = event.x-150
    y = event.y-250
    if drewInTheBounds(data, event.x, event.y):
        cellSize = (data.width//2)//10
        row = y//(cellSize)
        col = x//(cellSize)
        data.myDigit[row][col] = 1
    

def countTheAnimalKeyPressed(event, data):
    if data.canMove:
        if event.keysym=="Right":
            data.canMove = False
            data.mode = "playGameSuzie"
    if event.keysym=="space":
        n = data.num
        d= data.myDigit
        outputfile = open("num.txt", "w")
        outputfile.write(str(data.num))
        outputfile.close()
        data.computerGuess = whereIAt(d)
        #print(data.computerGuess)
        data.canMove = True
        
   
        
    
def countTheAnimalTimerFired(data):
    pass
    
def drewInTheBounds(data, x, y):
    if 150<=x<=450 and 250<=y<=550:
        return True
    return False
            
def drawAnimal(canvas, data):
    pass
    
def drawCellAnimal(canvas, data, row, col):
    # inspiration from tetris
    cellSize = (data.width//2)//10
    x = (col*cellSize)
    y= (row*cellSize)
    x1 = x + cellSize
    y1= y+cellSize
    canvas.create_rectangle(150+x,250+y, 150+x1, 250+y1, fill="black")
   
def countTheAnimalRedrawAll(canvas, data):
    cellSize = (data.width//2)//10
    for row in range(10):
        for col in range(10):
            x,y = row*cellSize,col*cellSize,
            x1,y1= x+cellSize, y+cellSize
            canvas.create_rectangle(150+x,250+y, 150+x1, 250+y1, width=0)
   
    for i in range(len(data.myDigit)):
        for j in range(len(data.myDigit)):
            if data.myDigit[i][j]==1:
                drawCellAnimal(canvas, data,i, j)
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2,  100,
                       text="Draw the number in the box by clicking the mouse pad and dragging", font="Arial 16 bold")
    canvas.create_text(data.width//2,  120,
                       text="When you are done, click the space bar.", font="Arial 16 bold")
    canvas.create_rectangle(150,250,450,550, width=3)
    if data.computerGuess == data.num:
        canvas.create_text(data.width//2,  140, text="Well done! There were %d dogs. Press right click to continue" % (data.computerGuess), font="Arial 16 bold")
    
        
####################################
# playGameSuzie mode
####################################

def playGameSuzieMousePressed(event, data):
    if data.yesButton.clickInButton(event.x, event.y):
        data.saidYes= True 
        
        
    if data.noButton.clickInButton(event.x, event.y): 
        data.canMove = True 
        data.nextMode = "goodBye"
        
def playGameSuzieKeyPressed(event, data):
    if data.canMove:
        if (event.keysym=="Left"):
            reset(data)
            data.canMove = False 
            data.mode = "countTheAnimal"
            
        if (event.keysym=="Right"):
            reset(data)
            data.canMove = False
            data.mode = "paintTheFence"
        
        
def playGameSuzieTimerFired(data):
    data.timerDelay= 2500 
    if data.saidYes:
        if data.j < len(data.yesSuzieTxt):
            data.txt=data.yesSuzieTxt[data.j]
            data.j+=1
        if data.txt[-1]=="continue":
            data.canMove = True
            
     
                    
    if data.saidNo:
        data.timePast+=1
        if data.timePast==1:
            data.txt=" "
            data.mode="goodBye"
            
    if data.i < len(data.suzie):
            data.txt=data.suzie[data.i]
            data.i+=1
        
def playGameSuzieRedrawAll(canvas, data):
    #canvas.create_rectangle(0,0, data.width, data.height, fill="white")
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2,  100,
                       text=data.txt, font="Aril 20 bold")

    canvas.create_image(data.width//4, data.height//2+data.height//5, image = data.suzieImg)
    if doneSpeak(data):
        data.yesButton.draw(canvas)
        data.noButton.draw(canvas)
###################################
# paintTheFence mode
####################################

def gameOver(data):
    if (checkRedLevel(data) and checkBlueLevel(data) and checkYellowLevel(data)):
        return True

def paintTheFenceMousePressed(event, data):
    #intersection(data, event.x, event.y)
    row = event.y//data.cellSize
    cols = event.x//data.cellSize
    if data.board[row%10][cols%10]=="saddlebrown" and not checkRedLevel(data):
        data.board[row%10][cols%10] = "red"
        outsideLinesRed(data,row,cols)
        data.lastPaint.append((row,cols))
        
        
    if data.board[row%10][cols%10]=="saddlebrown" and not checkBlueLevel(data):
        data.board[row%10][cols%10] = "blue"
        outsideLinesBlue(data,row,cols)
        data.lastPaint.append((row,cols))
        
    if data.board[row%10][cols%10]=="saddlebrown" and not checkYellowLevel(data):
        data.board[row%10][cols%10] = "yellow"
        outsideLinesYellow(data,row, cols)
        data.lastPaint.append((row,cols))
        

def outsideLinesRed(data,row,col):
    red = []
    for row in range(4,10):
        red.append((row, 1))
    if (row,col) not in red:
        data.outsideTheRedLine = True
                 
def outsideLinesBlue(data,row,col):
    blue = []
    for row in range(4,10):
        blue.append((row, 3))
    if (row,col) not in blue:
        data.outsideTheBlueLine = True
     
def outsideLinesYellow(data,row, col):
    yellow = []
    for row in range(4,10):
        yellow.append((row, 5))
    if (row,col) not in yellow:
        data.outsideTheYellowLine = True
        
    
def outSideTheLine(data):
    if data.outsideTheYellowLine or data.outsideTheRedLine or data.outsideTheBlueLine:
        return True 
    return False
            
def insideTheLine(data):
    data.outsideTheRedLine = False
    data.outsideTheBlueLine = False 
    data.outsideTheYellowLine = False
    
     
    
def blueCheck(data,row, cols):
    if ((data.board[row%10][cols%10]=="saddlebrown" or data.board[row%10][cols%10]=="red") and (not checkBlueLevel(data))):
        data.board[row%10][cols%10] = "blue"
    

def checkYellowLevel(data):
    for i in range(4,10):
        if data.board[i][5]!="yellow":
            return False 
    return True
   

def checkRedLevel(data):
    for i in range(4,10):
        if data.board[i][1]!="red":
            return False 
    return True
         
def checkBlueLevel(data):
    for i in range(4,10):
        if data.board[i][3]!="blue":
            return False 
    return True
    


def paintTheFenceKeyPressed(event, data):
    if (event.keysym=="Left"):
        data.mode = "playGameSuzie"
    if gameOver(data):
        if (event.keysym=="Right"):
            data.mode = "playGameSuzieP2"
    if (event.keysym == "space"):
        data.previousMode = "paintTheFence"
        data.mode = "help"
    if event.keysym=="BackSpace":
        row, col = data.lastPaint.pop()
        data.board[row][col] = "saddlebrown"
        
def drawFence(data):
     for i in range(4,10):
         data.board[i][1]="saddlebrown"
         data.board[i][7]="saddlebrown"
         data.board[i][3]="saddlebrown"
         data.board[i][5]="saddlebrown"
         
     for j in range(1,7):
         data.board[5][j]="saddlebrown"
         data.board[8][j]="saddlebrown"
         
def paintTheFenceTimerFired(data):
    data.timerDelay = 50
    data.paintTheFenceCount+=1
    if checkRedLevel(data) and checkBlueLevel(data) and checkYellowLevel(data):
        data.mode = "playGameSuzieP2"
    if data.paintTheFenceCount%50==0:
        insideTheLine(data)
    


def paintTheFenceRedrawAll(canvas, data):
    # draw in canvas
    myText1 = "Click on the a part of the fence to paint." 
    myText2 = "To see a picture of what it should look like, click the spacebar."
    for i in range(data.rows):
        for j in range(data.cols):
            drawCell(canvas, data, i, j, data.board[i][j])
    if outSideTheLine(data):
        #canvas.create_text(data.width//2, 100, text= "Uh-no! You went outside the line. Press backspace and try again", font="Arial 16 bold")
        myText1 = "Uh-no! You went outside the line. Press backspace and try again"
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2, 100,
                       text="Uh-no! You went outside the line. Press backspace and try again", font="Aril 18 bold" )
    
    if gameOver(data):
        canvas.create_text(data.width//2, 100, text= "Great Job! Thank you so much for your help", font="Arial 25 bold")
        canvas.create_text(data.width//2, 120, text= "Press right click to continue", font="Arial 25 bold")
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2, 100,
                       text=myText1, font="Aril 18 bold" )
    canvas.create_text(data.width//2, 130,
                       text=myText2, font="Aril 18 bold" )
        
####################################
# playGameSuzieP2 mode
####################################
def playGameSuzieP2MousePressed(event, data):
    pass

def playGameSuzieP2KeyPressed(event, data):
    if (event.keysym=="Left"):
        reset(data)
        data.mode = "paintTheFence"
    if data.canMove:
        if (event.keysym=="Right"):
            reset(data)
            data.canMove = False
            data.timerDelay = 500
            data.mode = "paintMixing"

    

def playGameSuzieP2TimerFired(data):
    data.timerDelay= 2500 #2500
    if data.i < len(data.suzieP2):
        data.txt=data.suzieP2[data.i]
        data.i+=1
    if data.txt[-1]=="continue":
        #print(data.canMove)
        data.canMove = True
        

def playGameSuzieP2RedrawAll(canvas, data):
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2,  100,
                       text=data.txt, font="Arial 20 bold")
    canvas.create_image(data.width//4, data.height//2+data.height//5, image = data.suzieImg) 
####################################
# paintMixing mode
####################################
def paintMixingMousePressed(event, data):
    #data.lastPaint.append((event.x, event.y))
    if data.yellowButton.clickInButton(event.x, event.y):
        data.lastPaint.append("yellow")
    if data.redButton.clickInButton(event.x, event.y):
        data.lastPaint.append("red")
    if data.blueButton.clickInButton(event.x, event.y):
        data.lastPaint.append("blue")
        


def createTheCircle(canvas,data):
    myW =data.width//2
    myH = data.height//6
    data.yellowButton= Yellow(myW//2, myH+180)
    data.redButton = Red(myW, myH+180)
    data.blueButton = Blue(myW+myW//2, myH+180)
    if len(data.lastPaint)>=2:
       
        if data.lastPaint[-1] != data.lastPaint[-2]:
            if data.lastPaint[-1]=="blue":
                w, h, r = data.width//2-data.width//4, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="blue")
                
            if data.lastPaint[-1]=="yellow":
                w, h, r = data.width//2-data.width//4, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="yellow")
                
            if data.lastPaint[-1]=="red":
                    w, h, r = data.width//2-data.width//4, data.height//2+data.height//4, 50
                    canvas.create_oval(w-r, h-r, w+r, h+r, fill="red")
                
            if data.lastPaint[-2]=="blue":
                    w, h, r = data.width//2, data.height//2+data.height//4, 50
                    canvas.create_oval(w-r, h-r, w+r, h+r, fill="blue")
                
            if data.lastPaint[-2]=="red":
                w, h, r = data.width//2, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="red")
            
            if data.lastPaint[-2]=="yellow":
                w, h, r = data.width//2, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="yellow")
                
            if (data.lastPaint[-2]=="yellow" and data.lastPaint[-1]=="red")\
            or (data.lastPaint[-2]=="red" and data.lastPaint[-1]=="yellow"):
                w, h, r = data.width//2+data.width//4, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="orange")
                data.paintMixing1 = "You made orange!"
                data.orange = True
                if data.countPaintMix%10==0:
                    data.lastPaint.pop()
                    data.lastPaint.pop()
                    data.paintMixing1 = "Combine the colors to make purple, green, and orange"
            
            if (data.lastPaint[-2]=="blue" and data.lastPaint[-1]=="red")\
            or (data.lastPaint[-2]=="red" and data.lastPaint[-1]=="blue"):
                w, h, r = data.width//2+data.width//4, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="purple")
                data.paintMixing1 = "You made purple!"
                data.purple = True
                if data.countPaintMix%10==0:
                    data.lastPaint.pop()
                    data.lastPaint.pop()
                    data.paintMixing1 = "Combine the colors to make purple, green, and orange"
                
            if (data.lastPaint[-2]=="blue" and data.lastPaint[-1]=="yellow")\
            or (data.lastPaint[-2]=="yellow" and data.lastPaint[-1]=="blue"):
                w, h, r = data.width//2+data.width//4, data.height//2+data.height//4, 50
                canvas.create_oval(w-r, h-r, w+r, h+r, fill="green")
                data.paintMixing1 = "You made green!"
                data.green = True
                if data.countPaintMix%10==0:
                    data.lastPaint.pop()
                    data.lastPaint.pop()
                    data.paintMixing1 = "Combine the colors to make purple, green, and orange"
            
             
            w, h, rH, rW = data.width//2-75, data.height//2+data.height//4, 10, 2
            canvas.create_rectangle(w-rW, h-rH, w+rW, h+rH, fill="black", width=1)
            
            #Create equal sign
            w, h, rH, rW = data.width//2+75, data.height//2+data.height//4, 2, 10
            canvas.create_rectangle(w-rW, h-rH, w+rW, h+rH, fill="black", width=1)
            w, h, rH, rW = data.width//2+75, data.height//2+data.height//4+10, 2, 10
            canvas.create_rectangle(w-rW, h-rH, w+rW, h+rH, fill="black", width=1)
            
            w, h, rH, rW = data.width//2-75, data.height//2+data.height//4, 2, 10
            canvas.create_rectangle(w-rW, h-rH, w+rW, h+rH, fill="black", width=1)
            
            
        
 
#def eraseGreen():
    

def paintMixingKeyPressed(event, data):
    if (event.keysym=="Left"):
        reset(data)
        data.mode = "playGameSuzieP2"
    if data.canMove:
        if (event.keysym=="Right"):
            reset(data)
            data.canMove = False
            data.mode = "paintTheFence2"
    

def paintMixingTimerFired(data):
    data.timerDelay=500
    data.countPaintMix+=1
    #print(data.lastPaint)
    paintMixingDone(data)
    
def paintMixingDone(data):
    if data.paintMixing1=="Well done! You made all the colors":
        #data.paintingMixing2 = "Press right arrow key to continue",
        data.canMove =True
        

def paintMixingRedrawAll(canvas, data):     
    data.yellowButton.draw(canvas)
    data.redButton.draw(canvas)
    data.blueButton.draw(canvas)
    createTheCircle(canvas, data)
    if data.green and data.orange and data.purple:
        data.paintMixing1 = "Well done! You made all the colors."
        data.paintMixing2 = "Press right arrow key to continue"
        data.canMove = True
       
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2,  100, text=data.paintMixing1, font="Aril 20 bold")
    #canvas.create_text(data.width//2, 130, text= "Try and and combine the colors to make purple, green, and orange", font="Aril 20 bold")
    canvas.create_text(data.width//2, 130, text= data.paintMixing2, font="Aril 20 bold")
   
####################################
# paintTheFence2 mode
####################################
def gameOver1(data):
    if (checkRedLevel1(data) and checkBlueLevel1(data) and checkYellowLevel1(data)\
    and checkPurpleLevel1(data) and checkOrangeLevel1(data) and  checkGreenLevel1(data)):
        return True

def paintTheFence2MousePressed(event, data):
    #intersection(data, event.x, event.y)
    row = event.y//data.cellSize
    cols = event.x//data.cellSize
        
    if data.board1[row%10][cols%10]=="saddlebrown" and not checkPurpleLevel1(data):
        data.board1[row%10][cols%10] = "purple"
        outsideLinesPurple1(data,row, cols)
        data.lastPaint.append((row,cols))
        
    if data.board1[row%10][cols%10]=="saddlebrown" and not checkOrangeLevel1(data):
        data.board1[row%10][cols%10] = "orange"
        outsideLinesOrange1(data,row,cols)
        data.lastPaint.append((row,cols))
        
    if data.board1[row%10][cols%10]=="saddlebrown" and not checkGreenLevel1(data):
        data.board1[row%10][cols%10] = "green"
        outsideLinesGreen1(data,row,cols)
        data.lastPaint.append((row,cols))


        
def outsideLinesPurple1(data,row, col):
    purple = []
    for row in range(4,10):
        purple.append((row, 7))
    if (row,col) not in purple:
        data.outsideThePurpleLine1 = True
        
def outsideLinesOrange1(data,row,col):
    orange = []
    for j in range(2,7,2):
        orange.append((5, j))
    if (row, col) not in orange:
        data.outsideTheOrangeLine1 = True
        
def outsideLinesGreen1(data, row, col):
    green = []
    for j in range(2,7,2):
        green.append((8, j))
    if (row, col) not in green:
        data.outsideTheGreenLine1 = True
    
    
def outSideTheLine1(data):
    if data.outsideTheYellowLine1 or data.outsideTheRedLine1 or data.outsideTheBlueLine1 or data.outsideThePurpleLine1 or data.outsideTheOrangeLine1:
        return True 
    return False
            
def insideTheLine1(data):
    data.outsideTheRedLine1 = False
    data.outsideTheBlueLine1 = False 
    data.outsideTheGreenLine1 = False 
    data.outsideTheOrangeLine1= False 
    data.outsideThePurpleLine1 = False 
    data.outsideTheYellowLine1 = False
    
    
def blueCheck1(data,row, cols):
    if ((data.board1[row%10][cols%10]=="saddlebrown" or data.board1[row%10][cols%10]=="red") and (not checkBlueLevel1(data))):
        data.board1[row%10][cols%10] = "blue"
    
def checkGreenLevel1(data):
    for j in range(2,7,2):
        if data.board1[8][j]!="green":
            return False
    return True
    
def checkOrangeLevel1(data):
    for j in range(2,7,2):
        if data.board1[5][j]!="orange":
            return False
    return True

def checkYellowLevel1(data):
    for i in range(4,10):
        if data.board1[i][5]!="yellow":
            return False 
    return True
   
def checkPurpleLevel1(data):
    for i in range(4,10):
        if data.board1[i][7]!="purple":
            return False 
    return True
   
def checkRedLevel1(data):
    for i in range(4,10):
        if data.board1[i][1]!="red":
            return False 
    return True
         
def checkBlueLevel1(data):
    for i in range(4,10):
        if data.board1[i][3]!="blue":
            return False 
    return True
    
def paintTheFence2KeyPressed(event, data):
    if gameOver1(data):
        if (event.keysym=="Right"):
            data.mode = "goodBye"
    if (event.keysym=="Left"):
        data.mode = "paintMixing"
   
    if (event.keysym == 'space'):
        data.previousMode = "paintTheFence2"
        data.mode = "help"
    if event.keysym=="BackSpace":
        row, col = data.lastPaint.pop()
        data.board1[row][col] = "saddlebrown"
        
def drawFence1(data):         
     for j in range(1,7):
         data.board1[5][j]="saddlebrown"
         data.board1[8][j]="saddlebrown"
        
     for i in range(4,10):
         data.board1[i][1]="red"
         data.board1[i][7]="saddlebrown"
         data.board1[i][3]="blue"
         data.board1[i][5]="yellow"
         
def paintTheFence2TimerFired(data):
    if data.paintTheFenceCount%50==0:
        insideTheLine(data)
    

def paintTheFence2RedrawAll(canvas, data):
    # draw in canvas
    myText1 = "Click on a part of the fence to paint." 
    myText2 = "To see a picture of what it should look like, click the spacebar."
    for i in range(data.rows):
        for j in range(data.cols):
            drawCell(canvas, data, i, j, data.board1[i][j])
    if outSideTheLine1(data):
        myText1 = "Uh-no! You went outside the line. Press backspace and try again"
        
        insideTheLine1(data)
    if gameOver1(data):
        myText1 = "Great Job! Thank you so much for your help"
        myText2 = "Press right arrow to continue"
       
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2, 100,
                       text=myText1, font="Aril 18 bold" )
    canvas.create_text(data.width//2, 130, text=myText2, font="Aril 18 bold")
   
    

####################################
# goodBye mode
####################################
def goodByeMousePressed(event, data):
    pass

def goodByeKeyPressed(event, data):
    if (event.keysym=="Right"):
        data.mode = "welcome"
    if (event.keysym=="Left"):
        data.mode = "paintTheFence2"
    
    
def goodByeTimerFired(data):
    pass
    

def goodByeRedrawAll(canvas, data):
    canvas.create_image(data.width//4, data.height//2+data.width//6, image = data.farmerJoe)
    canvas.create_image(data.width-data.width//4, data.height//2+data.width//6, image = data.suzieImg1)
    canvas.create_rectangle(0,20, data.width+5, 200, fill="springgreen")
    canvas.create_text(data.width//2, 100,
                       text="Thank you for helping!", font="Aril 18 bold" )
    canvas.create_text(data.width//2, 130,
                       text="We hope you enjoyed your time with us", font="Aril 18 bold" )
                       
                       

####################################
# use the run function as-is
#Cited from the 112 website
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
    
    def mouseMovedWrapper(event, canvas, data):
        mouseMoved(event, data)
        redrawAllWrapper(canvas, data)
        
    def mouseDraggedWrapper(event, canvas, data):
        mouseDragged(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event, canvas, data))
    root.bind("<B1-Motion>", lambda event:
                            mouseDraggedWrapper(event, canvas, data))                        
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    ("bye!")

run(600, 600)