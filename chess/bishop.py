from piece import Piece
from board import Board
class Bishop(Piece):
	br = Board.getBoard()
	def __init__(self, x, y, colour):
		if (colour):
			symbol = "B"
		else:
			symbol = "b"
		super().__init__(x, y, symbol, colour)
	
	def __str__(self):
		return str(self.symbol)

	def isLigitMove(self, eX, eY):
		if (self.x == eX and self.y == eY):
			return False
			
		if Board.br[eX][eY].hasPiece() and Board.br[eX][eY].getPiece().getColour() == self.colour:
			return False

		if ( (abs(self.x - eX) == abs(self.y - eY)) and (abs(self.x - eX) < 8) ):
			
			if (self.x > eX and self.y > eY):
				for i in range(1, abs(self.y - eY)):
					if Board.br[self.x - i][self.y - i].hasPiece():
						return False

			if (self.x < eX and self.y < eY):
				for i in range(1, abs(self.y - eY)):
					if Board.br[self.x + i][self.y + i].hasPiece():
						return False

			if (self.x < eX and self.y > eY):
				for i in range(1, abs(self.y - eY)):
					if Board.br[self.x + i][self.y - i].hasPiece():
						return False

			if (self.x > eX and self.y < eY):
				for i in range(1, abs(self.y - eY)):
					if Board.br[self.x - i][self.y + i].hasPiece():
						return False

			return True

		return False