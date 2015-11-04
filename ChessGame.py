from tkinter import *
from tkinter import ttk
import ChessGameClasses as cgc
board=list()
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
mainframe=ttk.Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)
for y in range(8):
    insertlist=list()
    if y%2==0:
        for x in range(8):
            if x%2==0:
                insertlist.append(ttk.Label(mainframe, image=white).grid(column=x, row=y))
                this=coords.generate(x,y)
                if this=="whitepawn":
                    ttk.Label(mainframe, image=pawnw).grid(column=x, row=y)
                elif this=="whitecastle":
                    ttk.Label(mainframe, image=castlew).grid(column=x, row=y)
                elif this=="whitehorse":
                    ttk.Label(mainframe, image=horsew).grid(column=x, row=y)
                elif this=="whitebishop":
                    ttk.Label(mainframe, image=bishopw).grid(column=x, row=y)
                elif this=="whiteking":
                    ttk.Label(mainframe, image=kingw).grid(column=x, row=y)
                elif this=="whitequeen":
                    ttk.Label(mainframe, image=queenw).grid(column=x, row=y)
                elif this=="blackpawn":
                    ttk.Label(mainframe, image=pawnw2).grid(column=x, row=y)
                elif this=="blackcastle":
                    ttk.Label(mainframe, image=castlew2).grid(column=x, row=y)
                elif this=="blackhorse":
                    ttk.Label(mainframe, image=horsew2).grid(column=x, row=y)
                elif this=="blackbishop":
                    ttk.Label(mainframe, image=bishopw2).grid(column=x, row=y)
                elif this=="blackking":
                    ttk.Label(mainframe, image=kingw2).grid(column=x, row=y)
                elif this=="blackqueen":
                    ttk.Label(mainframe, image=queenw2).grid(column=x, row=y)

            else:
                insertlist.append(ttk.Label(mainframe, image=black).grid(column=x, row=y))
                this=coords.generate(x,y)
                if this=="whitepawn":
                    ttk.Label(mainframe, image=pawnb).grid(column=x, row=y)
                elif this=="whitecastle":
                    ttk.Label(mainframe, image=castleb).grid(column=x, row=y)
                elif this=="whitehorse":
                    ttk.Label(mainframe, image=horseb).grid(column=x, row=y)
                elif this=="whitebishop":
                    ttk.Label(mainframe, image=bishopb).grid(column=x, row=y)
                elif this=="whiteking":
                    ttk.Label(mainframe, image=kingb).grid(column=x, row=y)
                elif this=="whitequeen":
                    ttk.Label(mainframe, image=queenb).grid(column=x, row=y)
                elif this=="blackpawn":
                    ttk.Label(mainframe, image=pawnb2).grid(column=x, row=y)
                elif this=="blackcastle":
                    ttk.Label(mainframe, image=castleb2).grid(column=x, row=y)
                elif this=="blackhorse":
                    ttk.Label(mainframe, image=horseb2).grid(column=x, row=y)
                elif this=="blackbishop":
                    ttk.Label(mainframe, image=bishopb2).grid(column=x, row=y)
                elif this=="blackking":
                    ttk.Label(mainframe, image=kingb2).grid(column=x, row=y)
                elif this=="blackqueen":
                    ttk.Label(mainframe, image=queenb2).grid(column=x, row=y)

    else:
        for x in range(8):
            if x%2==0:
                insertlist.append(ttk.Label(mainframe, image=black).grid(column=x, row=y))
                this=coords.generate(x,y)
                if this=="whitepawn":
                    ttk.Label(mainframe, image=pawnb).grid(column=x, row=y)
                elif this=="whitecastle":
                    ttk.Label(mainframe, image=castleb).grid(column=x, row=y)
                elif this=="whitehorse":
                    ttk.Label(mainframe, image=horseb).grid(column=x, row=y)
                elif this=="whitebishop":
                    ttk.Label(mainframe, image=bishopb).grid(column=x, row=y)
                elif this=="whiteking":
                    ttk.Label(mainframe, image=kingb).grid(column=x, row=y)
                elif this=="whitequeen":
                    ttk.Label(mainframe, image=queenb).grid(column=x, row=y)
                elif this=="blackpawn":
                    ttk.Label(mainframe, image=pawnb2).grid(column=x, row=y)
                elif this=="blackcastle":
                    ttk.Label(mainframe, image=castleb2).grid(column=x, row=y)
                elif this=="blackhorse":
                    ttk.Label(mainframe, image=horseb2).grid(column=x, row=y)
                elif this=="blackbishop":
                    ttk.Label(mainframe, image=bishopb2).grid(column=x, row=y)
                elif this=="blackking":
                    ttk.Label(mainframe, image=kingb2).grid(column=x, row=y)
                elif this=="blackqueen":
                    ttk.Label(mainframe, image=queenb2).grid(column=x, row=y)
            else:
                insertlist.append(ttk.Label(mainframe, image=white).grid(column=x, row=y))
                this=coords.generate(x,y)
                if this=="whitepawn":
                    ttk.Label(mainframe, image=pawnw).grid(column=x, row=y)
                elif this=="whitecastle":
                    ttk.Label(mainframe, image=castlew).grid(column=x, row=y)
                elif this=="whitehorse":
                    ttk.Label(mainframe, image=horsew).grid(column=x, row=y)
                elif this=="whitebishop":
                    ttk.Label(mainframe, image=bishopw).grid(column=x, row=y)
                elif this=="whiteking":
                    ttk.Label(mainframe, image=kingw).grid(column=x, row=y)
                elif this=="whitequeen":
                    ttk.Label(mainframe, image=queenw).grid(column=x, row=y)
                elif this=="blackpawn":
                    ttk.Label(mainframe, image=pawnw2).grid(column=x, row=y)
                elif this=="blackcastle":
                    ttk.Label(mainframe, image=castlew2).grid(column=x, row=y)
                elif this=="blackhorse":
                    ttk.Label(mainframe, image=horsew2).grid(column=x, row=y)
                elif this=="blackbishop":
                    ttk.Label(mainframe, image=bishopw2).grid(column=x, row=y)
                elif this=="blackking":
                    ttk.Label(mainframe, image=kingw2).grid(column=x, row=y)
                elif this=="blackqueen":
                    ttk.Label(mainframe, image=queenw2).grid(column=x, row=y)

    board.append(insertlist)

root.mainloop()
