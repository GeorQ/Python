class Square:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.haspiece = False
		self.__Piece = None

	def getX(self):
		return self.x	
	
	def getY(self):
		return self.y

	def hasPiece(self):
		if self.getPiece() != None:
			return True
		return False

	def removePiece(self):
		self.__Piece = None

	def setPiece(self, Piece):
		self.__Piece = Piece

	def getPiece(self):
		return self.__Piece

	def __str__(self):
		if self.__Piece != None:
			return str(self.__Piece)
		return "*"