from piece import Piece
from board import Board

class TestPiece(Piece):
	br = Board.getBoard()
	def __init__(self, x, y, colour):
		if (colour):
			symbol = "T"
		else:
			symbol = "t"
		super().__init__(x, y, symbol, colour)

	def __str__(self):
		return str(self.symbol)

	def isLigitMove(self, eX, eY):
		if (self.x == eX and self.y == eY):
			return False

		if Board.br[eX][eY].hasPiece() and Board.br[eX][eY].getPiece().getColour() == self.colour:
			return False

		return True