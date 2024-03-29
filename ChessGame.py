#Kai Ergin
#Final Project Chess Game
#GUI script
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
#Import classes and logic for pieces
import ChessGameClasses as cgc
coords=cgc.Piece()
root=Tk()
#Create images
imageinit=PhotoImage(file="white.gif")
white=imageinit.subsample(2,2)
imageinit=PhotoImage(file="black.gif")
black=imageinit.subsample(2,2)
imageinit=PhotoImage(file="pawnw.gif")
pawnw=imageinit.subsample(2,2)
imageinit=PhotoImage(file="pawnb.gif")
pawnb=imageinit.subsample(2,2)
imageinit=PhotoImage(file="pawnw2.gif")
pawnw2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="pawnb2.gif")
pawnb2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="castlew.gif")
castlew=imageinit.subsample(2,2)
imageinit=PhotoImage(file="castleb.gif")
castleb=imageinit.subsample(2,2)
imageinit=PhotoImage(file="castlew2.gif")
castlew2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="castleb2.gif")
castleb2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="horsew.gif")
horsew=imageinit.subsample(2,2)
imageinit=PhotoImage(file="horseb.gif")
horseb=imageinit.subsample(2,2)
imageinit=PhotoImage(file="horsew2.gif")
horsew2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="horseb2.gif")
horseb2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="bishopw.gif")
bishopw=imageinit.subsample(2,2)
imageinit=PhotoImage(file="bishopb.gif")
bishopb=imageinit.subsample(2,2)
imageinit=PhotoImage(file="bishopw2.gif")
bishopw2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="bishopb2.gif")
bishopb2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="kingw.gif")
kingw=imageinit.subsample(2,2)
imageinit=PhotoImage(file="kingb.gif")
kingb=imageinit.subsample(2,2)
imageinit=PhotoImage(file="kingw2.gif")
kingw2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="kingb2.gif")
kingb2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="queenw.gif")
queenw=imageinit.subsample(2,2)
imageinit=PhotoImage(file="queenb.gif")
queenb=imageinit.subsample(2,2)
imageinit=PhotoImage(file="queenw2.gif")
queenw2=imageinit.subsample(2,2)
imageinit=PhotoImage(file="queenb2.gif")
queenb2=imageinit.subsample(2,2)
root.title("Chess")
mainframe=Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)
mainframe.pack(side="left")
buttonList=list() #List of all buttons /NOT USED
past=[] #Coordinate of where piece previously was
total=True #Tells whether piece is being selected or being moved
variables="" #Type of piece selected

#Function when a piece is clicked
def onClick(arg1,arg2):
    global total
    global variables
    global past
    if total:
        variables=coords.clicked(arg1,arg2) #Checks to see what piece is on button selected
        past=[arg1,arg2]
        if variables=="blank": #If there is no piece on button selected
            total=True
        else:
            total=False
            this=variables
            thisput=past
            #This determines whether the square has a black or white background
            #Highlights background of piece by replacing it with a new button
            if thisput[1]%2==0:
                if (thisput[0])%2==0:
                    if this=="whitepawn":
                        thisimage="pawnw"
                    elif this=="whitecastle":
                        thisimage="castlew"
                    elif this=="whitehorse":
                        thisimage="horsew"
                    elif this=="whitebishop":
                        thisimage="bishopw"
                    elif this=="whiteking":
                        thisimage="kingw"
                    elif this=="whitequeen":
                        thisimage="queenw"
                    elif this=="blackpawn":
                        thisimage="pawnw2"
                    elif this=="blackcastle":
                        thisimage="castlew2"
                    elif this=="blackhorse":
                        thisimage="horsew2"
                    elif this=="blackbishop":
                        thisimage="bishopw2"
                    elif this=="blackking":
                        thisimage="kingw2"
                    elif this=="blackqueen":
                        thisimage="queenw2"
                    else:
                        thisimage="white"
                    var=("Button(mainframe, highlightbackground='red', image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
                else:
                    if this=="whitepawn":
                        thisimage="pawnb"
                    elif this=="whitecastle":
                        thisimage="castleb"
                    elif this=="whitehorse":
                        thisimage="horseb"
                    elif this=="whitebishop":
                        thisimage="bishopb"
                    elif this=="whiteking":
                        thisimage="kingb"
                    elif this=="whitequeen":
                        thisimage="queenb"
                    elif this=="blackpawn":
                        thisimage="pawnb2"
                    elif this=="blackcastle":
                        thisimage="castleb2"
                    elif this=="blackhorse":
                        thisimage="horseb2"
                    elif this=="blackbishop":
                        thisimage="bishopb2"
                    elif this=="blackking":
                        thisimage="kingb2"
                    elif this=="blackqueen":
                        thisimage="queenb2"
                    else:
                        thisimage="black"
                    var=("Button(mainframe, highlightbackground='red', image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
            else:
                if (thisput[0])%2==0:
                    if this=="whitepawn":
                        thisimage="pawnb"
                    elif this=="whitecastle":
                        thisimage="castleb"
                    elif this=="whitehorse":
                        thisimage="horseb"
                    elif this=="whitebishop":
                        thisimage="bishopb"
                    elif this=="whiteking":
                        thisimage="kingb"
                    elif this=="whitequeen":
                        thisimage="queenb"
                    elif this=="blackpawn":
                        thisimage="pawnb2"
                    elif this=="blackcastle":
                        thisimage="castleb2"
                    elif this=="blackhorse":
                        thisimage="horseb2"
                    elif this=="blackbishop":
                        thisimage="bishopb2"
                    elif this=="blackking":
                        thisimage="kingb2"
                    elif this=="blackqueen":
                        thisimage="queenb2"
                    else:
                        thisimage="black"
                    var=("Button(mainframe, highlightbackground='red', image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
                else:
                    if this=="whitepawn":
                        thisimage="pawnw"
                    elif this=="whitecastle":
                        thisimage="castlew"
                    elif this=="whitehorse":
                        thisimage="horsew"
                    elif this=="whitebishop":
                        thisimage="bishopw"
                    elif this=="whiteking":
                        thisimage="kingw"
                    elif this=="whitequeen":
                        thisimage="queenw"
                    elif this=="blackpawn":
                        thisimage="pawnw2"
                    elif this=="blackcastle":
                        thisimage="castlew2"
                    elif this=="blackhorse":
                        thisimage="horsew2"
                    elif this=="blackbishop":
                        thisimage="bishopw2"
                    elif this=="blackking":
                        thisimage="kingw2"
                    elif this=="blackqueen":
                        thisimage="queenw2"
                    else:
                        thisimage="white"
                    var=("Button(mainframe, highlightbackground='red', image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
            exec(var)
    else:
    	#If piece has already been selected...
        this=variables
        correct=coords.clicked(arg1,arg2,variables) #Checks to see if new spot is valid. If valid, outputs nothing.
        thisput=[arg1,arg2]
        if correct=="no":
            thisput=past #If not a valid spot to move piece, sets the new coordinates to the old coordinates
            correct="yes"
        elif correct=="special1": #For when a pawn turns to queen
        	this="whitequeen"
        elif correct=="special2":
        	this="blackqueen"
        elif correct=="iscastle":
            print("refresh")
            refresh(0,7,0,0)
        elif correct=="passant":
            refresh(2,3,4,5)
        if past[1]%2==0: #Replaces previous coordinate with blank tile
            if (past[0])%2==0:
                var=("Button(mainframe, image=white, command=lambda: onClick("+str(past[0])+","+str(past[1])+")).grid(column="+str(past[0])+", row="+str(past[1])+")")
            else:
                var=("Button(mainframe, image=black, command=lambda: onClick("+str(past[0])+","+str(past[1])+")).grid(column="+str(past[0])+", row="+str(past[1])+")")
        else:
            if (past[0])%2==0:
                var=("Button(mainframe, image=black, command=lambda: onClick("+str(past[0])+","+str(past[1])+")).grid(column="+str(past[0])+", row="+str(past[1])+")")
            else:
                var=("Button(mainframe, image=white, command=lambda: onClick("+str(past[0])+","+str(past[1])+")).grid(column="+str(past[0])+", row="+str(past[1])+")")
        exec(var)
        if thisput[1]%2==0: #Creates new piece at coordinates
            if (thisput[0])%2==0:
                if this=="whitepawn":
                    thisimage="pawnw"
                elif this=="whitecastle":
                    thisimage="castlew"
                elif this=="whitehorse":
                    thisimage="horsew"
                elif this=="whitebishop":
                    thisimage="bishopw"
                elif this=="whiteking":
                    thisimage="kingw"
                elif this=="whitequeen":
                    thisimage="queenw"
                elif this=="blackpawn":
                    thisimage="pawnw2"
                elif this=="blackcastle":
                    thisimage="castlew2"
                elif this=="blackhorse":
                    thisimage="horsew2"
                elif this=="blackbishop":
                    thisimage="bishopw2"
                elif this=="blackking":
                    thisimage="kingw2"
                elif this=="blackqueen":
                    thisimage="queenw2"
                else:
                    thisimage="white"
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
            else:
                if this=="whitepawn":
                    thisimage="pawnb"
                elif this=="whitecastle":
                    thisimage="castleb"
                elif this=="whitehorse":
                    thisimage="horseb"
                elif this=="whitebishop":
                    thisimage="bishopb"
                elif this=="whiteking":
                    thisimage="kingb"
                elif this=="whitequeen":
                    thisimage="queenb"
                elif this=="blackpawn":
                    thisimage="pawnb2"
                elif this=="blackcastle":
                    thisimage="castleb2"
                elif this=="blackhorse":
                    thisimage="horseb2"
                elif this=="blackbishop":
                    thisimage="bishopb2"
                elif this=="blackking":
                    thisimage="kingb2"
                elif this=="blackqueen":
                    thisimage="queenb2"
                else:
                    thisimage="black"
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
        else:
            if (thisput[0])%2==0:
                if this=="whitepawn":
                    thisimage="pawnb"
                elif this=="whitecastle":
                    thisimage="castleb"
                elif this=="whitehorse":
                    thisimage="horseb"
                elif this=="whitebishop":
                    thisimage="bishopb"
                elif this=="whiteking":
                    thisimage="kingb"
                elif this=="whitequeen":
                    thisimage="queenb"
                elif this=="blackpawn":
                    thisimage="pawnb2"
                elif this=="blackcastle":
                    thisimage="castleb2"
                elif this=="blackhorse":
                    thisimage="horseb2"
                elif this=="blackbishop":
                    thisimage="bishopb2"
                elif this=="blackking":
                    thisimage="kingb2"
                elif this=="blackqueen":
                    thisimage="queenb2"
                else:
                    thisimage="black"
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
            else:
                if this=="whitepawn":
                    thisimage="pawnw"
                elif this=="whitecastle":
                    thisimage="castlew"
                elif this=="whitehorse":
                    thisimage="horsew"
                elif this=="whitebishop":
                    thisimage="bishopw"
                elif this=="whiteking":
                    thisimage="kingw"
                elif this=="whitequeen":
                    thisimage="queenw"
                elif this=="blackpawn":
                    thisimage="pawnw2"
                elif this=="blackcastle":
                    thisimage="castlew2"
                elif this=="blackhorse":
                    thisimage="horsew2"
                elif this=="blackbishop":
                    thisimage="bishopw2"
                elif this=="blackking":
                    thisimage="kingw2"
                elif this=="blackqueen":
                    thisimage="queenw2"
                else:
                    thisimage="white"
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(thisput[0])+","+str(thisput[1])+")).grid(column="+str(thisput[0])+", row="+str(thisput[1])+")")
        exec(var)
        total=True
    print(arg1,arg2)
    
#Function used to initially generate chessboard and place pieces. Also used for resetting the chessboard
def reStart():
    coords.clear()
    global buttonList
    global past
    global total
    global variables
    buttonList=[]
    past=[]
    total=True
    variables=""
    #Goes through each tile on chessboard and asks class file if there is a piece here initially
    for y in range(8):
        if y%2==0:
            for x in range(8):
                if x%2==0:
                    this=coords.generate(x,y)
                    if this=="whitepawn":
                        thisimage="pawnw"
                    elif this=="whitecastle":
                        thisimage="castlew"
                    elif this=="whitehorse":
                        thisimage="horsew"
                    elif this=="whitebishop":
                        thisimage="bishopw"
                    elif this=="whiteking":
                        thisimage="kingw"
                    elif this=="whitequeen":
                        thisimage="queenw"
                    elif this=="blackpawn":
                        thisimage="pawnw2"
                    elif this=="blackcastle":
                        thisimage="castlew2"
                    elif this=="blackhorse":
                        thisimage="horsew2"
                    elif this=="blackbishop":
                        thisimage="bishopw2"
                    elif this=="blackking":
                        thisimage="kingw2"
                    elif this=="blackqueen":
                        thisimage="queenw2"
                    else:
                        thisimage="white"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
                else:
                    this=coords.generate(x,y)
                    if this=="whitepawn":
                        thisimage="pawnb"
                    elif this=="whitecastle":
                        thisimage="castleb"
                    elif this=="whitehorse":
                        thisimage="horseb"
                    elif this=="whitebishop":
                        thisimage="bishopb"
                    elif this=="whiteking":
                        thisimage="kingb"
                    elif this=="whitequeen":
                        thisimage="queenb"
                    elif this=="blackpawn":
                        thisimage="pawnb2"
                    elif this=="blackcastle":
                        thisimage="castleb2"
                    elif this=="blackhorse":
                        thisimage="horseb2"
                    elif this=="blackbishop":
                        thisimage="bishopb2"
                    elif this=="blackking":
                        thisimage="kingb2"
                    elif this=="blackqueen":
                        thisimage="queenb2"
                    else:
                        thisimage="black"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
        else:
            for x in range(8):
                if x%2==0:
                    this=coords.generate(x,y)
                    if this=="whitepawn":
                        thisimage="pawnb"
                    elif this=="whitecastle":
                        thisimage="castleb"
                    elif this=="whitehorse":
                        thisimage="horseb"
                    elif this=="whitebishop":
                        thisimage="bishopb"
                    elif this=="whiteking":
                        thisimage="kingb"
                    elif this=="whitequeen":
                        thisimage="queenb"
                    elif this=="blackpawn":
                        thisimage="pawnb2"
                    elif this=="blackcastle":
                        thisimage="castleb2"
                    elif this=="blackhorse":
                        thisimage="horseb2"
                    elif this=="blackbishop":
                        thisimage="bishopb2"
                    elif this=="blackking":
                        thisimage="kingb2"
                    elif this=="blackqueen":
                        thisimage="queenb2"
                    else:
                        thisimage="black"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
                else:
                    this=coords.generate(x,y)
                    if this=="whitepawn":
                        thisimage="pawnw"
                    elif this=="whitecastle":
                        thisimage="castlew"
                    elif this=="whitehorse":
                        thisimage="horsew"
                    elif this=="whitebishop":
                        thisimage="bishopw"
                    elif this=="whiteking":
                        thisimage="kingw"
                    elif this=="whitequeen":
                        thisimage="queenw"
                    elif this=="blackpawn":
                        thisimage="pawnw2"
                    elif this=="blackcastle":
                        thisimage="castlew2"
                    elif this=="blackhorse":
                        thisimage="horsew2"
                    elif this=="blackbishop":
                        thisimage="bishopw2"
                    elif this=="blackking":
                        thisimage="kingw2"
                    elif this=="blackqueen":
                        thisimage="queenw2"
                    else:
                        thisimage="white"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
    for imagesin in buttonList:
        exec(imagesin)
def refresh(w,x,y,z):
    listnum=[w,x,y,z]
    buttonList=[]
    for y in listnum:
        if y%2==0:
            for x in range(8):
                if x%2==0:
                    this=coords.refresh(x,y)
                    if this=="whitepawn":
                        thisimage="pawnw"
                    elif this=="whitecastle":
                        thisimage="castlew"
                    elif this=="whitehorse":
                        thisimage="horsew"
                    elif this=="whitebishop":
                        thisimage="bishopw"
                    elif this=="whiteking":
                        thisimage="kingw"
                    elif this=="whitequeen":
                        thisimage="queenw"
                    elif this=="blackpawn":
                        thisimage="pawnw2"
                    elif this=="blackcastle":
                        thisimage="castlew2"
                    elif this=="blackhorse":
                        thisimage="horsew2"
                    elif this=="blackbishop":
                        thisimage="bishopw2"
                    elif this=="blackking":
                        thisimage="kingw2"
                    elif this=="blackqueen":
                        thisimage="queenw2"
                    else:
                        thisimage="white"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
                else:
                    this=coords.refresh(x,y)
                    if this=="whitepawn":
                        thisimage="pawnb"
                    elif this=="whitecastle":
                        thisimage="castleb"
                    elif this=="whitehorse":
                        thisimage="horseb"
                    elif this=="whitebishop":
                        thisimage="bishopb"
                    elif this=="whiteking":
                        thisimage="kingb"
                    elif this=="whitequeen":
                        thisimage="queenb"
                    elif this=="blackpawn":
                        thisimage="pawnb2"
                    elif this=="blackcastle":
                        thisimage="castleb2"
                    elif this=="blackhorse":
                        thisimage="horseb2"
                    elif this=="blackbishop":
                        thisimage="bishopb2"
                    elif this=="blackking":
                        thisimage="kingb2"
                    elif this=="blackqueen":
                        thisimage="queenb2"
                    else:
                        thisimage="black"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
        else:
            for x in range(8):
                if x%2==0:
                    this=coords.refresh(x,y)
                    if this=="whitepawn":
                        thisimage="pawnb"
                    elif this=="whitecastle":
                        thisimage="castleb"
                    elif this=="whitehorse":
                        thisimage="horseb"
                    elif this=="whitebishop":
                        thisimage="bishopb"
                    elif this=="whiteking":
                        thisimage="kingb"
                    elif this=="whitequeen":
                        thisimage="queenb"
                    elif this=="blackpawn":
                        thisimage="pawnb2"
                    elif this=="blackcastle":
                        thisimage="castleb2"
                    elif this=="blackhorse":
                        thisimage="horseb2"
                    elif this=="blackbishop":
                        thisimage="bishopb2"
                    elif this=="blackking":
                        thisimage="kingb2"
                    elif this=="blackqueen":
                        thisimage="queenb2"
                    else:
                        thisimage="black"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
                else:
                    this=coords.refresh(x,y)
                    if this=="whitepawn":
                        thisimage="pawnw"
                    elif this=="whitecastle":
                        thisimage="castlew"
                    elif this=="whitehorse":
                        thisimage="horsew"
                    elif this=="whitebishop":
                        thisimage="bishopw"
                    elif this=="whiteking":
                        thisimage="kingw"
                    elif this=="whitequeen":
                        thisimage="queenw"
                    elif this=="blackpawn":
                        thisimage="pawnw2"
                    elif this=="blackcastle":
                        thisimage="castlew2"
                    elif this=="blackhorse":
                        thisimage="horsew2"
                    elif this=="blackbishop":
                        thisimage="bishopw2"
                    elif this=="blackking":
                        thisimage="kingw2"
                    elif this=="blackqueen":
                        thisimage="queenw2"
                    else:
                        thisimage="white"
                    buttonList.append("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(x)+","+str(y)+")).grid(column="+str(x)+", row="+str(y)+")")
    for imagesin in buttonList:
        exec(imagesin)
reStart() #Initial generation
#Options frame with reset button, captured pieces list, undo button, etc.
optionsframe=Frame(root,padx=20)
reset=Button(optionsframe,text="Reset",command=reStart).grid(column=1,row=1)
optionsframe.pack(side="right")
root.mainloop()
