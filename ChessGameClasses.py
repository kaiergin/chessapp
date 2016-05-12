#Kai Ergin
#Final Project Chess Game
#Class list
class Piece:
	def __init__(self):
		# Initially creating blank lists to hold different types of pieces
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
		self.boolean=True # Selecting a piece vs moving a piece
		self.turn=True # Who's turn is it?
		self.pastSpot=[] # A temporary variable to hold a piece's past spot
		self.special=False # Special case for pawns turning into queens (white)
		self.special1=False # Same ^ but for black
		self.whitecastling=True # Castling variable to check if the king has moved yet (white)
		self.blackcastling=True # Same ^ but for black
	def generate(self,x,y):
		# Generates board. Places pieces in the their 'initial' starting place
		piecelist=[x,y]
		if y==6:
			self.__wpawnlist.append(piecelist) # Adds the coordinates of the piece to its piece list
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
		if y==7 and x==4:
			self.__wkinglist.append(piecelist)
			return "whiteking"
		if y==7 and x==3:
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
		# When a piece is clicked
		check=[x,y]
		if self.boolean: # If selecting
			self.boolean=False
			self.pastSpot=check
			if self.turn:
				self.turn=False
				for x in self.__wpawnlist:
					if check==x:
						self.__wpawnlist.remove(x) # Removing piece from position
						return "whitepawn" # Returns the type of piece in the square selected
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
			else:
				self.turn=True
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
			self.switcher()
			return "blank"
		else: # If moving
			# Essentially checks if the move is legal based off of the type of piece it is
			if r=="whitepawn":
				if (self.pastSpot[1]==check[1]+1 and (self.pastSpot[0]==check[0])):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]-1)=="no":
						self.switcher() # This sets the turn back the original person's turn
						self.__wpawnlist.append(self.pastSpot) # Adds the piece back to where it was previously
						return "no"
						# When no is return that means the move is illegal and the move will be reset
				elif (self.pastSpot[1]==check[1]+1 and (self.pastSpot[0]==check[0]+1)):
					if self.checklist("black",self.pastSpot[0]-1,self.pastSpot[1]-1)!="no":
						self.switcher()
						self.__wpawnlist.append(self.pastSpot)
						return "no"
				elif (self.pastSpot[1]==check[1]+1 and (self.pastSpot[0]==check[0]-1)):
					if self.checklist("black",self.pastSpot[0]+1,self.pastSpot[1]-1)!="no":
						self.switcher()
						self.__wpawnlist.append(self.pastSpot)
						return "no"
				elif (self.pastSpot[1]==6 and self.pastSpot[1]==check[1]+2 and self.pastSpot[0]==check[0]):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]-2)=="no" or self.checklist("both",self.pastSpot[0],self.pastSpot[1]-1)=="no":
						self.switcher()
						self.__wpawnlist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__wpawnlist.append(self.pastSpot)
					return "no"
				if check[1]==0: # Special case for pawn -> queen
					r="whitequeen"
					self.special=True
			elif r=="whitecastle":
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__wcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__wcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.switcher()
							self.__wcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("white",check[0],check[1])=="no":
						self.switcher()
						self.__wcastlelist.append(self.pastSpot)
						return "no"
				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()
								self.__wcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()								
								self.__wcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.switcher()
							self.__wcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("white",check[0],check[1])=="no":
						self.switcher()
						self.__wcastlelist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__wcastlelist.append(self.pastSpot)
					return "no"
			elif r=="whitehorse":
				if (self.pastSpot[0]+1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]+1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]-1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]-1==check[1]):
					if self.checklist("white",check[0],check[1])=="no":
						self.switcher()
						self.__whorselist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__whorselist.append(self.pastSpot)
					return "no"
			elif r=="whitebishop":
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.checklist("white",check[0],check[1])=="no":
					self.switcher()
					self.__wbishoplist.append(self.pastSpot)
					return "no"
				if thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__wbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__wbishoplist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__wbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__wbishoplist.append(self.pastSpot)
									return "no"
					else:
						self.switcher()
						self.__wbishoplist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__wbishoplist.append(self.pastSpot)
					return "no"
			elif r=="whiteking":
				if self.checklist("white",check[0],check[1])=="no":
					self.switcher()
					self.__wkinglist.append(self.pastSpot)
					return "no"
				if (self.pastSpot[0]+1==check[0] and self.pastSpot[1]==check[1]) or (self.pastSpot[1]+1==check[1] and self.pastSpot[0]==check[0]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]==check[1]) or (self.pastSpot[1]-1==check[1] and self.pastSpot[0]==check[0]) or (self.pastSpot[1]-1==check[1] and self.pastSpot[0]-1==check[0]) or (self.pastSpot[1]-1==check[1] and self.pastSpot[0]+1==check[0]) or (self.pastSpot[1]+1==check[1] and self.pastSpot[0]-1==check[0]) or (self.pastSpot[1]+1==check[1] and self.pastSpot[0]+1==check[0]):
					pass
				else:
					self.switcher()
					self.__wkinglist.append(self.pastSpot)
					return "no"
			elif r=="whitequeen":
				if self.checklist("white",check[0],check[1])=="no":
					self.switcher()
					self.__wqueenlist.append(self.pastSpot)
					return "no"
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__wqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__wqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.switcher()
							self.__wqueenlist.append(self.pastSpot)
							return "no"
				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()
								self.__wqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()							
								self.__wqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.switcher()
							self.__wqueenlist.append(self.pastSpot)
							return "no"
				elif thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__wqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__wqueenlist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__wqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__wqueenlist.append(self.pastSpot)
									return "no"
					else:
						self.switcher()
						self.__wqueenlist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__wqueenlist.append(self.pastSpot)
					return "no"
			elif r=="blackpawn":
				if (self.pastSpot[1]==check[1]-1 and (self.pastSpot[0]==check[0])):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]+1)=="no":
						self.switcher()
						self.__bpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==check[1]-1 and (self.pastSpot[0]==check[0]+1)):
					if self.checklist("white",self.pastSpot[0]-1,self.pastSpot[1]+1)!="no":
						self.switcher()
						self.__bpawnlist.append(self.pastSpot)
						return "no"
				elif (self.pastSpot[1]==check[1]-1 and (self.pastSpot[0]==check[0]-1)):
					if self.checklist("white",self.pastSpot[0]+1,self.pastSpot[1]+1)!="no":
						self.switcher()
						self.__bpawnlist.append(self.pastSpot)
						return "no"
				elif (self.pastSpot[1]==1 and self.pastSpot[1]==check[1]-2 and self.pastSpot[0]==check[0]):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]+2)=="no" or self.checklist("both",self.pastSpot[0],self.pastSpot[1]+1)=="no":
						self.switcher()
						self.__bpawnlist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__bpawnlist.append(self.pastSpot)
					return "no"
				if check[1]==7:
					r="blackqueen"
					self.special1=True
			elif r=="blackcastle":
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__bcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__bcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.switcher()
							self.__bcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("black",check[0],check[1])=="no":
						self.switcher()
						self.__bcastlelist.append(self.pastSpot)
						return "no"
				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()
								self.__bcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()
								self.__bcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.switcher()
							self.__bcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("black",check[0],check[1])=="no":
						self.switcher()
						self.__bcastlelist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__bcastlelist.append(self.pastSpot)
					return "no"
			elif r=="blackhorse":
				if (self.pastSpot[0]+1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]+1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]-1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]-1==check[1]):
					if self.checklist("black",check[0],check[1])=="no":
						self.switcher()
						self.__bhorselist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__bhorselist.append(self.pastSpot)
					return "no"
			elif r=="blackbishop":
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.checklist("black",check[0],check[1])=="no":
					self.switcher()
					self.__bbishoplist.append(self.pastSpot)
					return "no"
				if thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__bbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__bbishoplist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__bbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__bbishoplist.append(self.pastSpot)
									return "no"
					else:
						self.switcher()
						self.__bbishoplist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__bbishoplist.append(self.pastSpot)
					return "no"
			elif r=="blackking":
				if self.checklist("black",check[0],check[1])=="no":
					self.switcher()
					self.__bkinglist.append(self.pastSpot)
					return "no"
				if (self.pastSpot[0]+1==check[0] and self.pastSpot[1]==check[1]) or (self.pastSpot[1]+1==check[1] and self.pastSpot[0]==check[0]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]==check[1]) or (self.pastSpot[1]-1==check[1] and self.pastSpot[0]==check[0]) or (self.pastSpot[1]-1==check[1] and self.pastSpot[0]-1==check[0]) or (self.pastSpot[1]-1==check[1] and self.pastSpot[0]+1==check[0]) or (self.pastSpot[1]+1==check[1] and self.pastSpot[0]-1==check[0]) or (self.pastSpot[1]+1==check[1] and self.pastSpot[0]+1==check[0]):
					pass
				else:
					self.switcher()
					self.__bkinglist.append(self.pastSpot)
					return "no"
			elif r=="blackqueen":
				if self.checklist("black",check[0],check[1])=="no":
					self.switcher()
					self.__bqueenlist.append(self.pastSpot)
					return "no"
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__bqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.switcher()
								self.__bqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.switcher()
							self.__bqueenlist.append(self.pastSpot)
							return "no"
				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()
								self.__bqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.switcher()							
								self.__bqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.switcher()
							self.__bqueenlist.append(self.pastSpot)
							return "no"
				elif thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__bqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__bqueenlist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.switcher()
									self.__bqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.switcher()
									self.__bqueenlist.append(self.pastSpot)
									return "no"
					else:
						self.switcher()
						self.__bqueenlist.append(self.pastSpot)
						return "no"
				else:
					self.switcher()
					self.__bqueenlist.append(self.pastSpot)
					return "no"
			didremovepiece=False
			# Checks to see if a piece was taken. If piece was taken, it needs to be removed from the list
			for x in self.__wpawnlist:
				if check==x:
					self.__wpawnlist.remove(x)
					piecetaken="whitepawn"
					didremovepiece=True
			for x in self.__whorselist:
				if check==x:
					self.__whorselist.remove(x)
					piecetaken="whitehorse"
					didremovepiece=True
			for x in self.__wcastlelist:
				if check==x:
					self.__wcastlelist.remove(x)
					piecetaken="whitecastle"
					didremovepiece=True
			for x in self.__wkinglist:
				if check==x:
					self.__wkinglist.remove(x)
					piecetaken="whiteking"
					didremovepiece=True
			for x in self.__wbishoplist:
				if check==x:
					self.__wbishoplist.remove(x)
					piecetaken="whitebishop"
					didremovepiece=True
			for x in self.__wqueenlist:
				if check==x:
					self.__wqueenlist.remove(x)
					piecetaken="whitequeen"
					didremovepiece=True
			for x in self.__bpawnlist:
				if check==x:
					self.__bpawnlist.remove(x)
					piecetaken="blackpawn"
					didremovepiece=True
			for x in self.__bhorselist:
				if check==x:
					self.__bhorselist.remove(x)
					piecetaken="blackhorse"
					didremovepiece=True
			for x in self.__bcastlelist:
				if check==x:
					self.__bcastlelist.remove(x)
					piecetaken="blackcastle"
					didremovepiece=True
			for x in self.__bkinglist:
				if check==x:
					self.__bkinglist.remove(x)
					piecetaken="blackking"
					didremovepiece=True
			for x in self.__bbishoplist:
				if check==x:
					self.__bbishoplist.remove(x)
					piecetaken="blackbishop"
					didremovepiece=True
			for x in self.__bqueenlist:
				if check==x:
					self.__bqueenlist.remove(x)
					piecetaken="blackqueen"
					didremovepiece=True
			# Adds the piece moved to its new spot
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
			# For special pawn cases
			if self.special:
				self.special=False
				return "special1"
			if self.special1:
				self.special1=False
				return "special2"
			# Checks if in check
			arecheck=False
			if self.turn:
				arecheck=self.checkcheck("black")
			else:
				arecheck=self.checkcheck("white")
			if arecheck:
				# If in check, puts piece back into previous position and returns to previous game state
				print("CHECK")
				if r=="whitepawn":
					self.__wpawnlist.append(self.pastSpot)
					self.__wpawnlist.remove(check)
				elif r=="whitecastle":
					self.__wcastlelist.append(self.pastSpot)
					self.__wcastlelist.remove(check)
				elif r=="whitehorse":
					self.__whorselist.append(self.pastSpot)
					self.__whorselist.remove(check)
				elif r=="whitebishop":
					self.__wbishoplist.append(self.pastSpot)
					self.__wbishoplist.remove(check)
				elif r=="whiteking":
					self.__wkinglist.append(self.pastSpot)
					self.__wkinglist.remove(check)
				elif r=="whitequeen":
					self.__wqueenlist.append(self.pastSpot)
					self.__wqueenlist.remove(check)
				elif r=="blackpawn":
					self.__bpawnlist.append(self.pastSpot)
					self.__bpawnlist.remove(check)
				elif r=="blackcastle":
					self.__bcastlelist.append(self.pastSpot)
					self.__bcastlelist.remove(check)
				elif r=="blackhorse":
					self.__bhorselist.append(self.pastSpot)
					self.__bhorselist.remove(check)
				elif r=="blackbishop":
					self.__bbishoplist.append(self.pastSpot)
					self.__bbishoplist.remove(check)
				elif r=="blackking":
					self.__bkinglist.append(self.pastSpot)
					self.__bkinglist.remove(check)
				elif r=="blackqueen":
					self.__bqueenlist.append(self.pastSpot)
					self.__bqueenlist.remove(check)
				if didremovepiece:
					# If a piece was removed, but was in check, restores taken piece
					if piecetaken=="whitepawn":
						self.__wpawnlist.append(check)
					elif piecetaken=="whitecastle":
						self.__wcastlelist.append(check)
					elif piecetaken=="whitehorse":
						self.__whorselist.append(check)
					elif piecetaken=="whitebishop":
						self.__wbishoplist.append(check)
					elif piecetaken=="whiteking":
						self.__wkinglist.append(check)
					elif piecetaken=="whitequeen":
						self.__wqueenlist.append(check)
					elif piecetaken=="blackpawn":
						self.__bpawnlist.append(check)
					elif piecetaken=="blackcastle":
						self.__bcastlelist.append(check)
					elif piecetaken=="blackhorse":
						self.__bhorselist.append(check)
					elif piecetaken=="blackbishop":
						self.__bbishoplist.append(check)
					elif piecetaken=="blackking":
						self.__bkinglist.append(check)
					elif piecetaken=="blackqueen":
						self.__bqueenlist.append(check)
				self.switcher()
				return "no"
			if r=="blackking":
				self.blackcastling=False
			if r=="whiteking":
				self.whitecastling=False
	def checklist(self,color,a,b): 
		# This function is for checking if there is a piece on a given square
		# It is used to make sure that pieces aren't jumping over each other
		num=[a,b]
		if color=="white":
			for x in self.__wpawnlist:
				if num==x:
					return "no"
			for x in self.__whorselist:
				if num==x:
					return "no"
			for x in self.__wcastlelist:
				if num==x:
					return "no"
			for x in self.__wkinglist:
				if num==x:
					return "no"
			for x in self.__wbishoplist:
				if num==x:
					return "no"
			for x in self.__wqueenlist:
				if num==x:
					return "no"
		elif color=="both":
			for x in self.__wpawnlist:
				if num==x:
					return "no"
			for x in self.__whorselist:
				if num==x:
					return "no"
			for x in self.__wcastlelist:
				if num==x:
					return "no"
			for x in self.__wkinglist:
				if num==x:
					return "no"
			for x in self.__wbishoplist:
				if num==x:
					return "no"
			for x in self.__wqueenlist:
				if num==x:
					return "no"
			for x in self.__bpawnlist:
				if num==x:
					return "no"
			for x in self.__bhorselist:
				if num==x:
					return "no"
			for x in self.__bcastlelist:
				if num==x:
					return "no"
			for x in self.__bkinglist:
				if num==x:
					return "no"
			for x in self.__bbishoplist:
				if num==x:
					return "no"
			for x in self.__bqueenlist:
				if num==x:
					return "no"
		else:
			for x in self.__bpawnlist:
				if num==x:
					return "no"
			for x in self.__bhorselist:
				if num==x:
					return "no"
			for x in self.__bcastlelist:
				if num==x:
					return "no"
			for x in self.__bkinglist:
				if num==x:
					return "no"
			for x in self.__bbishoplist:
				if num==x:
					return "no"
			for x in self.__bqueenlist:
				if num==x:
					return "no"
	def clear(self):
		# Clears all lists for resetting the game
		self.__wpawnlist=[]
		self.__wcastlelist=[]
		self.__whorselist=[]
		self.__wbishoplist=[]
		self.__wkinglist=[]
		self.__wqueenlist=[]
		self.__wkinglist=[]
		self.__bpawnlist=[]
		self.__bcastlelist=[]
		self.__bhorselist=[]
		self.__bbishoplist=[]
		self.__bkinglist=[]
		self.__bqueenlist=[]
		self.__bkinglist=[]
		self.boolean=True
		self.turn=True
		self.pastSpot=[]
		self.whitecastling=True
		self.blackcastling=True
	def switcher(self):
		self.boolean=True
		if self.turn:
			self.turn=False
		else:
			self.turn=True
	def checkcheck(self,side):
		'''
		This function checks for check
		It essentially checks every piece on a side to see if the piece is putting the king in check
		Then it checks to see if there is anything blocking that piece check
		If the function returns True, that means the king is indeed in check and the move must be cancelled
		Otherwise, the move is a valid move
		'''
		ischeck=False
		if side=="white":
			for x in self.__wkinglist:
				for y in self.__bcastlelist:
					if y[0]==x[0]:
						print("black castle")
						ischeck=True
						if y[1]-x[1]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[1]-x[1])
						for n in self.__bpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wcastlelist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bqueenlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wqueenlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
					elif y[1]==x[1]:
						print("black castle")
						ischeck=True
						if y[0]-x[0]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[0]-x[0])
						for n in self.__bpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wcastlelist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bqueenlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wqueenlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
					if ischeck:
						return True
				for y in self.__bbishoplist:
					if x[0]-y[0]==x[1]-y[1]:
						print("black bishop")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						
					elif -1*(x[0]-y[0])==x[1]-y[1]:
						print("black bishop")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
					if ischeck:
						return True
				for y in self.__bqueenlist:
					if y[0]==x[0]:
						print("black queen")
						ischeck=True
						if y[1]-x[1]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[1]-x[1])
						for n in self.__bpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wcastlelist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bcastlelist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wqueenlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
					elif y[1]==x[1]:
						print("black queen")
						ischeck=True
						if y[0]-x[0]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[0]-x[0])
						for n in self.__bpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wcastlelist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bcastlelist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wqueenlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
					if ischeck:
						return True
					if x[0]-y[0]==x[1]-y[1]:
						print("black queen")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						
					elif -1*(x[0]-y[0])==x[1]-y[1]:
						print("black queen")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
					if ischeck:
						return True
				for y in self.__bpawnlist:
					if y[1]+1==x[1] and (y[0]+1==x[0] or y[0]-1==x[0]):
						print("black pawn")
						return True
				for y in self.__bhorselist:
					if (x[0]+2==y[0] and x[1]+1==y[1]) or (x[0]-2==y[0] and x[1]+1==y[1]) or (x[0]+2==y[0] and x[1]-1==y[1]) or (x[0]-2==y[0] and x[1]-1==y[1]) or (x[0]+1==y[0] and x[1]+2==y[1]) or (x[0]-1==y[0] and x[1]+2==y[1]) or (x[0]+1==y[0] and x[1]-2==y[1]) or (x[0]-1==y[0] and x[1]-2==y[1]):
						print("black horse")
						return True
				for y in self.__bkinglist:
					if abs(y[0]-x[0])<=1 and abs(y[1]-x[1])<=1:
						print("black king")
						return True
		if side=="black":
			for x in self.__bkinglist:
				for y in self.__wcastlelist:
					if y[0]==x[0]:
						print("white castle")
						ischeck=True
						if y[1]-x[1]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[1]-x[1])
						for n in self.__bpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bcastlelist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bqueenlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wqueenlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
					elif y[1]==x[1]:
						print("white castle")
						ischeck=True
						if y[0]-x[0]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[0]-x[0])
						for n in self.__bpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bcastlelist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bqueenlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wqueenlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
					if ischeck:
						return True
				for y in self.__wbishoplist:
					if x[0]-y[0]==x[1]-y[1]:
						print("white bishop 1")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						
					elif -1*(x[0]-y[0])==x[1]-y[1]:
						print("white bishop 2")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
					if ischeck:
						return True
				for y in self.__wqueenlist:
					if y[0]==x[0]:
						print("white queen 1")
						ischeck=True
						if y[1]-x[1]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[1]-x[1])
						for n in self.__bpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__wcastlelist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bcastlelist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bqueenlist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]<0:
								ischeck=False
							elif placement=="pos" and n[0]==y[0] and abs(n[1]-x[1])<distance and n[1]-x[1]>0:
								ischeck=False
					elif y[1]==x[1]:
						print("white queen 2")
						ischeck=True
						if y[0]-x[0]<0:
							placement="neg"
						else:
							placement="pos"
						distance=abs(y[0]-x[0])
						for n in self.__bpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wpawnlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wbishoplist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__wcastlelist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bhorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__whorselist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bcastlelist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bqueenlist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
						for n in self.__bkinglist:
							if placement=="neg" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]<0:
								ischeck=False
							elif placement=="pos" and n[1]==y[1] and abs(n[0]-x[0])<distance and n[0]-x[0]>0:
								ischeck=False
					if ischeck:
						return True
					if x[0]-y[0]==x[1]-y[1]:
						print("white queen 3")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and x[0]-n[0]==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						
					elif -1*(x[0]-y[0])==x[1]-y[1]:
						print("white queen 4")
						ischeck=True
						distance=abs(x[0]-y[0])
						if x[0]-y[0]<0:
							pos="neg"
						else:
							pos="pos"
						for n in self.__bpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wpawnlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*x([0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bqueenlist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bbishoplist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__whorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bhorselist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__wcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bcastlelist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
						for n in self.__bkinglist:
							if pos=="neg" and x[0]-n[0]<0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
							elif pos=="pos" and x[0]-n[0]>0 and -1*(x[0]-n[0])==x[1]-n[1] and abs(x[0]-n[0])<distance:
								ischeck=False
					if ischeck:
						return True
				for y in self.__wpawnlist:
					if y[1]-1==x[1] and (y[0]+1==x[0] or y[0]-1==x[0]):
						print("white pawn")
						return True
				for y in self.__whorselist:
					if (x[0]+2==y[0] and x[1]+1==y[1]) or (x[0]-2==y[0] and x[1]+1==y[1]) or (x[0]+2==y[0] and x[1]-1==y[1]) or (x[0]-2==y[0] and x[1]-1==y[1]) or (x[0]+1==y[0] and x[1]+2==y[1]) or (x[0]-1==y[0] and x[1]+2==y[1]) or (x[0]+1==y[0] and x[1]-2==y[1]) or (x[0]-1==y[0] and x[1]-2==y[1]):
						print("white horse")
						return True
				for y in self.__wkinglist:
					if abs(y[0]-x[0])<=1 and abs(y[1]-x[1])<=1:
						print("white king")
						return True
		return False
				
