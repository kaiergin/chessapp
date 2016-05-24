import ChessGameClasses as cgc
class Bot(cgc.Piece):

	def __init__(self):
		self.rankp = 1
		self.rankb = 3
		self.rankr = 5
		self.rankq = 9
		self.rankk = 1000

	def evaluate(self):
		cgc.coords.tempSave()
		num = list()
		currentScore = self.scoreAfter()
		for a in range(8):
			for b in range(8):
				for x in cgc.coords.__bpawnlist:
					cgc.coords.tempLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"black")
					if legalmove!="no":
						cgc.coords.botSave()
						num.append([self.whiteCheck(),a,b,x,"blackpawn"])
				for x in cgc.coords.__bbishoplist:
					cgc.coords.tempLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"black")
					if legalmove!="no":
						cgc.coords.botSave()
						num.append([self.whiteCheck(),a,b,x,"blackbishop"])
				for x in cgc.coords.__bhorselist:
					cgc.coords.tempLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"black")
					if legalmove!="no":
						cgc.coords.botSave()
						num.append([self.whiteCheck(),a,b,x,"blackhorse"])
				for x in cgc.coords.__bcastlelist:
					cgc.coords.tempLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"black")
					if legalmove!="no":
						cgc.coords.botSave()
						num.append([self.whiteCheck(),a,b,x,"blackcastle"])
				for x in cgc.coords.__bkinglist:
					cgc.coords.tempLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"black")
					if legalmove!="no":
						cgc.coords.botSave()
						num.append([self.whiteCheck(),a,b,x,"blackking"])
				for x in cgc.coords.__bqueenlist:
					cgc.coords.tempLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"black")
					if legalmove!="no":
						cgc.coords.botSave()
						num.append([self.whiteCheck(),a,b,x,"blackqueen"])
		cgc.coords.tempLoad()
		largest=num[0]
		for x in num:
			if x[0]>largest[0]:
				largest=x
		return largest
		
	def whiteCheck(self):
		largest=0
		nextScore = self.scoreAfter()
		for a in range(8):
			for b in range(8):
				for x in cgc.coords.__wpawnlist:
					cgc.coords.botLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"white")
					if legalmove!="no":
						if largest<self.scoreAfter():
							largest=self.scoreAfter()
				for x in cgc.coords.__wbishoplist:
					cgc.coords.botLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"white")
					if legalmove!="no":
						if largest<self.scoreAfter():
							largest=self.scoreAfter()
				for x in cgc.coords.__whorselist:
					cgc.coords.botLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"white")
					if legalmove!="no":
						if largest<self.scoreAfter():
							largest=self.scoreAfter()
				for x in cgc.coords.__wcastlelist:
					cgc.coords.botLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"white")
					if legalmove!="no":
						if largest<self.scoreAfter():
							largest=self.scoreAfter()
				for x in cgc.coords.__wkinglist:
					cgc.coords.botLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"white")
					if legalmove!="no":
						if largest<self.scoreAfter():
							largest=self.scoreAfter()
				for x in cgc.coords.__wqueenlist:
					cgc.coords.botLoad()
					legalmove = cgc.coords.isLegal(a,b,x,"white")
					if legalmove!="no":
						if largest<self.scoreAfter():
							largest=self.scoreAfter()
		return nextScore-largest
	
	def scoreAfter(self):
		black = 0
		white = 0
		for x in cgc.coords.__bpawnlist.length():
			black += self.rankp
		for x in cgc.coords.__wpawnlist.length():
			white += self.rankp
		for x in cgc.coords.__bbishoplist.length():
			black += self.rankb
		for x in cgc.coords.__wbishoplist.length():
			white += self.rankb
		for x in cgc.coords.__bhorselist.length():
			black += self.rankb
		for x in cgc.coords.__whorselist.length():
			white += self.rankb
		for x in cgc.coords.__bqueenlist.length():
			black += self.rankq
		for x in cgc.coords.__wqueenlist.length():
			white += self.rankq
		for x in cgc.coords.__brooklist.length():
			black += self.rankr
		for x in cgc.coords.__wrooklist.length():
			white += self.rankr
		current = black-white
		return current
