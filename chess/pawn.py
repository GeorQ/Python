from piece import Piece
from board import Board
class Pawn(Piece):
	br = Board.getBoard()
	def __init__(self, x, y, colour):
		self.isLongMove = True
		if (colour):
			symbol = "P"
		else:
			symbol = "p"
		super().__init__(x, y, symbol, colour)

	def __str__(self):
		return str(self.symbol)

	def isLigitMove(self, eX, eY):


		if self.colour:

			if ( (eX - self.x == 1) and (abs(self.y - eY) == 1) and (Board.br[eX][eY].hasPiece()) and(Board.br[eX][eY].getPiece().getColour != self.colour) ):
					return True

			if self.isLongMove:
				if ((eX - self.x == 2 or eX - self.x == 1) and (not Board.br[self.x + 1][self.y].hasPiece()) and (eY == self.y) and (not Board.br[eX][eY].hasPiece())):
					self.isLongMove = False
					return True

			else:
				if ((eX - self.x == 1) and (eY == self.y) and (not Board.br[eX][eY].hasPiece())):
					self.isLongMove = False
					return True



		if not self.colour:
			if ( (self.x - eX == 1) and (abs(self.y - eY) == 1) and (Board.br[eX][eY].getPiece().getColour != self.colour) ):
					return True

			if self.isLongMove:
				if ((self.x - eX == 2 or self.x - eX == 1) and (not Board.br[self.x - 1][self.y].hasPiece()) and (eY == self.y) and (not Board.br[eX][eY].hasPiece()) ):
					self.isLongMove = False
					return True
			else:
				if ((self.x - eX == 1) and (eY == self.y) and (not Board.br[eX][eY].hasPiece())):
					self.isLongMove = False
					return True

		

		return False