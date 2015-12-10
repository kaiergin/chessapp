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
def onClick(arg1,arg2):
    print(arg1,arg2)
for y in range(8):
    if y%2==0:
        for x in range(8):
            if x%2==0:
                this=coords.generate(x,y)
                if this=="whitepawn":
                    buttonList.append(Button(mainframe, image=pawnw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitecastle":
                    buttonList.append(Button(mainframe, image=castlew, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitehorse":
                    buttonList.append(Button(mainframe, image=horsew, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitebishop":
                    buttonList.append(Button(mainframe, image=bishopw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whiteking":
                    buttonList.append(Button(mainframe, image=kingw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitequeen":
                    buttonList.append(Button(mainframe, image=queenw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackpawn":
                    buttonList.append(Button(mainframe, image=pawnw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackcastle":
                    buttonList.append(Button(mainframe, image=castlew2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackhorse":
                    buttonList.append(Button(mainframe, image=horsew2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackbishop":
                    buttonList.append(Button(mainframe, image=bishopw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackking":
                    buttonList.append(Button(mainframe, image=kingw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackqueen":
                    buttonList.append(Button(mainframe, image=queenw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                else:
                    buttonList.append(Button(mainframe,image=white, command=lambda: onClick(x,y)).grid(column=x,row=y))

            else:
                this=coords.generate(x,y)
                if this=="whitepawn":
                    buttonList.append(Button(mainframe, image=pawnb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitecastle":
                    buttonList.append(Button(mainframe, image=castleb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitehorse":
                    buttonList.append(Button(mainframe, image=horseb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitebishop":
                    buttonList.append(Button(mainframe, image=bishopb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whiteking":
                    buttonList.append(Button(mainframe, image=kingb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitequeen":
                    buttonList.append(Button(mainframe, image=queenb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackpawn":
                    buttonList.append(Button(mainframe, image=pawnb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackcastle":
                    buttonList.append(Button(mainframe, image=castleb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackhorse":
                    buttonList.append(Button(mainframe, image=horseb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackbishop":
                    buttonList.append(Button(mainframe, image=bishopb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackking":
                    buttonList.append(Button(mainframe, image=kingb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackqueen":
                    buttonList.append(Button(mainframe, image=queenb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                else:
                    buttonList.append(Button(mainframe,image=black, command=lambda: onClick(x,y)).grid(column=x,row=y))

    else:
        for x in range(8):
            if x%2==0:
                this=coords.generate(x,y)
                if this=="whitepawn":
                    buttonList.append(Button(mainframe, image=pawnb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitecastle":
                    buttonList.append(Button(mainframe, image=castleb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitehorse":
                    buttonList.append(Button(mainframe, image=horseb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitebishop":
                    buttonList.append(Button(mainframe, image=bishopb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whiteking":
                    buttonList.append(Button(mainframe, image=kingb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitequeen":
                    buttonList.append(Button(mainframe, image=queenb, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackpawn":
                    buttonList.append(Button(mainframe, image=pawnb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackcastle":
                    buttonList.append(Button(mainframe, image=castleb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackhorse":
                    buttonList.append(Button(mainframe, image=horseb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackbishop":
                    buttonList.append(Button(mainframe, image=bishopb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackking":
                    buttonList.append(Button(mainframe, image=kingb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackqueen":
                    buttonList.append(Button(mainframe, image=queenb2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                else:
                    buttonList.append(Button(mainframe,image=black, command=lambda: onClick(x,y)).grid(column=x,row=y))
            else:
                this=coords.generate(x,y)
                if this=="whitepawn":
                    buttonList.append(Button(mainframe, image=pawnw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitecastle":
                    buttonList.append(Button(mainframe, image=castlew, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitehorse":
                    buttonList.append(Button(mainframe, image=horsew, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitebishop":
                    buttonList.append(Button(mainframe, image=bishopw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whiteking":
                    buttonList.append(Button(mainframe, image=kingw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="whitequeen":
                    buttonList.append(Button(mainframe, image=queenw, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackpawn":
                    buttonList.append(Button(mainframe, image=pawnw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackcastle":
                    buttonList.append(Button(mainframe, image=castlew2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackhorse":
                    buttonList.append(Button(mainframe, image=horsew2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackbishop":
                    buttonList.append(Button(mainframe, image=bishopw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackking":
                    buttonList.append(Button(mainframe, image=kingw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                elif this=="blackqueen":
                    buttonList.append(Button(mainframe, image=queenw2, command=lambda: onClick(x,y)).grid(column=x, row=y))
                else:
                    buttonList.append(Button(mainframe,image=white, command=lambda: onClick(x,y)).grid(column=x,row=y))
root.mainloop()
