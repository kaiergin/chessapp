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
        self.boolean=True
    
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
    def clicked(self,x,y,r="blank"):
        check=[x,y]
        if self.boolean:
            self.boolean=False
            for x in self.__wpawnlist:
                if check==x:
                    self.__wpawnlist.remove(x)
                    return "whitepawn"
            for x in self.__whorselist:
                if check==x:
                    self.__whorselist.remove(x)
                    return "whitehorse"
            for x in self.__wcastlelist:
                if check==x:
                    self.__wcastlelist.remove(x)
                    return "whitecastle"
            for x in self.__wkinglist:
                if check==x:
                    self.__wkinglist.remove(x)
                    return "whiteking"
            for x in self.__wbishoplist:
                if check==x:
                    self.__wbishoplist.remove(x)
                    return "whitebishop"
            for x in self.__wqueenlist:
                if check==x:
                    self.__wqueenlist.remove(x)
                    return "whitequeen"
            for x in self.__bpawnlist:
                if check==x:
                    self.__bpawnlist.remove(x)
                    return "blackpawn"
            for x in self.__bhorselist:
                if check==x:
                    self.__bhorselist.remove(x)
                    return "blackhorse"
            for x in self.__bcastlelist:
                if check==x:
                    self.__bcastlelist.remove(x)
                    return "blackcastle"
            for x in self.__bkinglist:
                if check==x:
                    self.__bkinglist.remove(x)
                    return "blackking"
            for x in self.__bbishoplist:
                if check==x:
                    self.__bbishoplist.remove(x)
                    return "blackbishop"
            for x in self.__bqueenlist:
                if check==x:
                    self.__bqueenlist.remove(x)
                    return "blackqueen"
        else:
            if r=="whitepawn":
                self.__wpawnlist.append(check)
            elif r=="whitecastle":
                self.__wcastlelist.append(check)
            elif r=="whitehorse":
                self.__whorselist.append(check)
            elif r=="whitebishop":
                self.__wbishoplist.append(check)
            elif r=="whiteking":
                self.__wkinglist.append(check)
            elif r=="whitequeen":
                self.__wqueenlist.append(check)
            elif r=="blackpawn":
                self.__bpawnlist.append(check)
            elif r=="blackcastle":
                self.__bcastlelist.append(check)
            elif r=="blackhorse":
                self.__bhorselist.append(check)
            elif r=="blackbishop":
                self.__bbishoplist.append(check)
            elif r=="blackking":
                self.__bkinglist.append(check)
            elif r=="blackqueen":
                self.__bqueenlist.append(check)
            self.boolean=True
