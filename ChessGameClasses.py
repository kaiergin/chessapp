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
		self.turn=True
		self.pastSpot=[]
	
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
		check=[x,y]
		if self.boolean:
			self.boolean=False
			self.pastSpot=check
			if self.turn:
				self.turn=False
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
			if self.turn:
				self.turn=False
			else:
				self.turn=True
			self.boolean=True
			return "blank"
		else:
			if r=="whitepawn":
				if (self.pastSpot[1]==check[1]+1 and (self.pastSpot[0]==check[0])):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]-1)=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__wpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==check[1]+1 and (self.pastSpot[0]==check[0]+1)):
					if self.checklist("black",self.pastSpot[0]-1,self.pastSpot[1]-1)!="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__wpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==check[1]+1 and (self.pastSpot[0]==check[0]-1)):
					if self.checklist("black",self.pastSpot[0]+1,self.pastSpot[1]-1)!="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__wpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==6 and self.pastSpot[1]==check[1]+2 and self.pastSpot[0]==check[0]):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]-2)=="no" or self.checklist("both",self.pastSpot[0],self.pastSpot[1]-1)=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__wpawnlist.append(self.pastSpot)
						return "no"
					pass
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					
					self.__wpawnlist.append(self.pastSpot)
					return "no"
			elif r=="whitecastle":
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__wcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__wcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__wcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("white",check[0],check[1])=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						
						self.__wcastlelist.append(self.pastSpot)
						return "no"

				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__wcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True								
								self.__wcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__wcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("white",check[0],check[1])=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						
						self.__wcastlelist.append(self.pastSpot)
						return "no"
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					
					self.__wcastlelist.append(self.pastSpot)
					return "no"
			elif r=="whitehorse":
				if (self.pastSpot[0]+1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]+1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]-1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]-1==check[1]):
					if self.checklist("white",check[0],check[1])=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__whorselist.append(self.pastSpot)
						return "no"
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__whorselist.append(self.pastSpot)
					return "no"
			elif r=="whitebishop":
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.checklist("white",check[0],check[1])=="no":
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__wbishoplist.append(self.pastSpot)
					return "no"
				if thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wbishoplist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wbishoplist.append(self.pastSpot)
									return "no"
					else:
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__wbishoplist.append(self.pastSpot)
						return "no"
						
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__wbishoplist.append(self.pastSpot)
					return "no"
			elif r=="whiteking":
				if self.checklist("white",check[0],check[1])=="no":
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__wkinglist.append(self.pastSpot)
					return "no"
				if self.pastSpot[0]+1==check[0] or self.pastSpot[1]+1==check[1] or self.pastSpot[0]-1==check[0] or self.pastSpot[1]-1==check[1]:
					pass
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__wkinglist.append(self.pastSpot)
					return "no"
			elif r=="whitequeen":
				if self.checklist("white",check[0],check[1])=="no":
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__wqueenlist.append(self.pastSpot)
					return "no"
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__wqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__wqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__wqueenlist.append(self.pastSpot)
							return "no"

				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__wqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True								
								self.__wqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__wqueenlist.append(self.pastSpot)
							return "no"
				elif thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wqueenlist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__wqueenlist.append(self.pastSpot)
									return "no"
					else:
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__wqueenlist.append(self.pastSpot)
						return "no"
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					
					self.__wqueenlist.append(self.pastSpot)
					return "no"

			elif r=="blackpawn":
				if (self.pastSpot[1]==check[1]-1 and (self.pastSpot[0]==check[0])):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]+1)=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==check[1]-1 and (self.pastSpot[0]==check[0]+1)):
					if self.checklist("white",self.pastSpot[0]-1,self.pastSpot[1]+1)!="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==check[1]-1 and (self.pastSpot[0]==check[0]-1)):
					if self.checklist("white",self.pastSpot[0]+1,self.pastSpot[1]+1)!="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bpawnlist.append(self.pastSpot)
						return "no"
					pass
				elif (self.pastSpot[1]==1 and self.pastSpot[1]==check[1]-2 and self.pastSpot[0]==check[0]):
					if self.checklist("both",self.pastSpot[0],self.pastSpot[1]+2)=="no" or self.checklist("both",self.pastSpot[0],self.pastSpot[1]+1)=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bpawnlist.append(self.pastSpot)
						return "no"
					pass
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__bpawnlist.append(self.pastSpot)
					return "no"
			elif r=="blackcastle":
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__bcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("black",check[0],check[1])=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						
						self.__bcastlelist.append(self.pastSpot)
						return "no"
				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bcastlelist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bcastlelist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__bcastlelist.append(self.pastSpot)
							return "no"
					if self.checklist("black",check[0],check[1])=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						
						self.__bcastlelist.append(self.pastSpot)
						return "no"
							
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					
					self.__bcastlelist.append(self.pastSpot)
					return "no"
			elif r=="blackhorse":
				if (self.pastSpot[0]+1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]+2==check[1]) or (self.pastSpot[0]+1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]-1==check[0] and self.pastSpot[1]-2==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]+1==check[1]) or (self.pastSpot[0]+2==check[0] and self.pastSpot[1]-1==check[1]) or (self.pastSpot[0]-2==check[0] and self.pastSpot[1]-1==check[1]):
					if self.checklist("black",check[0],check[1])=="no":
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bhorselist.append(self.pastSpot)
						return "no"
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__bhorselist.append(self.pastSpot)
					return "no"
			elif r=="blackbishop":
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.checklist("black",check[0],check[1])=="no":
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__wbishoplist.append(self.pastSpot)
					return "no"
				if thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bbishoplist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bbishoplist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bbishoplist.append(self.pastSpot)
									return "no"
					else:
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bbishoplist.append(self.pastSpot)
						return "no"
						
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__bbishoplist.append(self.pastSpot)
					return "no"
			elif r=="blackking":
				if self.checklist("black",check[0],check[1])=="no":
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__bkinglist.append(self.pastSpot)
					return "no"
				if self.pastSpot[0]+1==check[0] or self.pastSpot[1]+1==check[1] or self.pastSpot[0]-1==check[0] or self.pastSpot[1]-1==check[1]:
					pass
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__bkinglist.append(self.pastSpot)
					return "no"
			elif r=="blackqueen":
				if self.checklist("black",check[0],check[1])=="no":
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					self.__bqueenlist.append(self.pastSpot)
					return "no"
				thisnumber1=self.pastSpot[0]-check[0]
				thisnumber2=self.pastSpot[1]-check[1]
				if self.pastSpot[1]==check[1]:
					if self.pastSpot[0]>check[0]:
						for l in range(self.pastSpot[0],check[0],-1):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[0],check[0]):
							if self.checklist("both",l,check[1])=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[0]==check[0]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__bqueenlist.append(self.pastSpot)
							return "no"

				elif self.pastSpot[0]==check[0]:
					if self.pastSpot[1]>check[1]:
						for l in range(self.pastSpot[1],check[1],-1):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True
								
								self.__bqueenlist.append(self.pastSpot)
								return "no"
					else:
						for l in range(self.pastSpot[1],check[1]):
							if self.checklist("both",check[0],l)=="no":
								self.boolean=True
								if self.turn:
									self.turn=False
								else:
									self.turn=True								
								self.__bqueenlist.append(self.pastSpot)
								return "no"
						if self.pastSpot[1]==check[1]:
							self.boolean=True
							if self.turn:
								self.turn=False
							else:
								self.turn=True
							
							self.__bqueenlist.append(self.pastSpot)
							return "no"
				elif thisnumber1==thisnumber2 or thisnumber1*-1==thisnumber2:
					if thisnumber1<0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]+checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bqueenlist.append(self.pastSpot)
									return "no"
					elif thisnumber1>0:
						if thisnumber2<0:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]+checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bqueenlist.append(self.pastSpot)
									return "no"
						else:
							for checkspot in range(abs(thisnumber1)):
								if self.checklist("both",self.pastSpot[0]-checkspot,self.pastSpot[1]-checkspot)=="no":
									self.boolean=True
									if self.turn:
										self.turn=False
									else:
										self.turn=True
									self.__bqueenlist.append(self.pastSpot)
									return "no"
					else:
						self.boolean=True
						if self.turn:
							self.turn=False
						else:
							self.turn=True
						self.__bqueenlist.append(self.pastSpot)
						return "no"
				else:
					self.boolean=True
					if self.turn:
						self.turn=False
					else:
						self.turn=True
					
					self.__bqueenlist.append(self.pastSpot)
					return "no"

			for x in self.__wpawnlist:
				if check==x:
					self.__wpawnlist.remove(x)
			for x in self.__whorselist:
				if check==x:
					self.__whorselist.remove(x)
			for x in self.__wcastlelist:
				if check==x:
					self.__wcastlelist.remove(x)
			for x in self.__wkinglist:
				if check==x:
					self.__wkinglist.remove(x)
			for x in self.__wbishoplist:
				if check==x:
					self.__wbishoplist.remove(x)
			for x in self.__wqueenlist:
				if check==x:
					self.__wqueenlist.remove(x)
			for x in self.__bpawnlist:
				if check==x:
					self.__bpawnlist.remove(x)
			for x in self.__bhorselist:
				if check==x:
					self.__bhorselist.remove(x)
			for x in self.__bcastlelist:
				if check==x:
					self.__bcastlelist.remove(x)
			for x in self.__bkinglist:
				if check==x:
					self.__bkinglist.remove(x)
			for x in self.__bbishoplist:
				if check==x:
					self.__bbishoplist.remove(x)
			for x in self.__bqueenlist:
				if check==x:
					self.__bqueenlist.remove(x)
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
	def checklist(self,color,a,b):
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
