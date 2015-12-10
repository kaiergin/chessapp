#Kai Ergin
#Final Project Chess Game
#Class list
class Piece:
    def __init__(self):
        self.__wpawnlist=list()
        self.__wcastlelist=list()
        self.__whorselist=list()
        self.__wbishoplist=list()
        self.__wkinglist=list()
        self.__wqueenlist=list()
        self.__wkinglist=list()
        self.__bpawnlist=list()
        self.__bcastlelist=list()
        self.__bhorselist=list()
        self.__bbishoplist=list()
        self.__bkinglist=list()
        self.__bqueenlist=list()
        self.__bkinglist=list()
    
    def generate(self,x,y):
        piecelist=[x,y]
        if y==6:
            self.__wpawnlist.append(piecelist)
            return "whitepawn"
        if y==7 and (x==0 or x==7):
            self.__wcastlelist.append(piecelist)
            return "whitecastle"
        if y==7 and (x==1 or x==6):
            self.__whorselist.append(piecelist)
            return "whitehorse"
        if y==7 and (x==2 or x==5):
            self.__wbishoplist.append(piecelist)
            return "whitebishop"
        if y==7 and x==3:
            self.__wkinglist.append(piecelist)
            return "whiteking"
        if y==7 and x==4:
            self.__wqueenlist.append(piecelist)
            return "whitequeen"
        if y==1:
            self.__bpawnlist.append(piecelist)
            return "blackpawn"
        if y==0 and (x==0 or x==7):
            self.__bcastlelist.append(piecelist)
            return "blackcastle"
        if y==0 and (x==1 or x==6):
            self.__bhorselist.append(piecelist)
            return "blackhorse"
        if y==0 and (x==2 or x==5):
            self.__bbishoplist.append(piecelist)
            return "blackbishop"
        if y==0 and x==4:
            self.__bkinglist.append(piecelist)
            return "blackking"
        if y==0 and x==3:
            self.__bqueenlist.append(piecelist)
            return "blackqueen"
    def clicked(self,piece):
        print("hello")
        
