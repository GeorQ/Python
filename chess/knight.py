from piece import Piece
from board import Board
class Knight(Piece):
	br = Board.getBoard()
	def __init__(self, x, y, colour):
		if (colour):
			symbol = "N"
		else:
			symbol = "n"
		super().__init__(x, y, symbol, colour)
	
	def __str__(self):
		return str(self.symbol)

	def isLigitMove(self, eX, eY):
		if ((abs(self.x - eX) == 2) and (abs(self.y - eY) == 1)):
			if ( (Board.br[eX][eY].hasPiece()) and (Board.br[eX][eY].getPiece().getColour() == self.colour) ):
				return False
			return True

		if ((abs(self.x - eX) == 1) and (abs(self.y - eY) == 2)):
			if ( (Board.br[eX][eY].hasPiece()) and (Board.br[eX][eY].getPiece().getColour() == self.colour) ):
				return False
			return True

		return False