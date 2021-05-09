class Piece(object):
	def __init__(self, x, y, symbol, colour):
		self.x = x
		self.y = y
		self.symbol = symbol
		self.colour = colour
	

	def getSymbol(self):
		return self.symbol

	def setSymbol(self, symbol):
		self.symbol = symbol

	def getColour(self):
		return self.colour

	def updateCoordinates(self, x, y):
		self.x = x
		self.y = y		
		