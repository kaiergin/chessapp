from tkinter import *
import ChessGameClasses as cgc
coords=cgc.Piece()
root=Tk()
white=PhotoImage(file="white.gif")
black=PhotoImage(file="black.gif")
pawnw=PhotoImage(file="pawnw.gif")
pawnb=PhotoImage(file="pawnb.gif")
pawnw2=PhotoImage(file="pawnw2.gif")
pawnb2=PhotoImage(file="pawnb2.gif")
castlew=PhotoImage(file="castlew.gif")
castleb=PhotoImage(file="castleb.gif")
castlew2=PhotoImage(file="castlew2.gif")
castleb2=PhotoImage(file="castleb2.gif")
horsew=PhotoImage(file="horsew.gif")
horseb=PhotoImage(file="horseb.gif")
horsew2=PhotoImage(file="horsew2.gif")
horseb2=PhotoImage(file="horseb2.gif")
bishopw=PhotoImage(file="bishopw.gif")
bishopb=PhotoImage(file="bishopb.gif")
bishopw2=PhotoImage(file="bishopw2.gif")
bishopb2=PhotoImage(file="bishopb2.gif")
kingw=PhotoImage(file="kingw.gif")
kingb=PhotoImage(file="kingb.gif")
kingw2=PhotoImage(file="kingw2.gif")
kingb2=PhotoImage(file="kingb2.gif")
queenw=PhotoImage(file="queenw.gif")
queenb=PhotoImage(file="queenb.gif")
queenw2=PhotoImage(file="queenw2.gif")
queenb2=PhotoImage(file="queenb2.gif")
root.title("Chess")
mainframe=Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)
mainframe.pack()
buttonList=list()
total=True
variables=""
def onClick(arg1,arg2):
    global total
    global variables
    if total:
        variables=coords.clicked(arg1,arg2)
        if arg2%2==0:
            if (arg1)%2==0:
                var=("Button(mainframe, image=white, command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
            else:
                var=("Button(mainframe, image=black, command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
        else:
            if (arg1)%2==0:
                var=("Button(mainframe, image=black, command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
            else:
                var=("Button(mainframe, image=white, command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
        exec(var)
        total=False
    else:
        this=variables
        coords.clicked(arg1,arg2,variables)
        if arg2%2==0:
            if (arg1)%2==0:
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
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
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
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
        else:
            if (arg1)%2==0:
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
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
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
                var=("Button(mainframe, image="+str(thisimage)+", command=lambda: onClick("+str(arg1)+","+str(arg2)+")).grid(column="+str(arg1)+", row="+str(arg2)+")")
        exec(var)
        total=True
    print(arg1,arg2)
    
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
root.mainloop()
