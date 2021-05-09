from piece import Piece
from board import Board

class Shashka(Piece):
	br = Board.getBoard()
	def __init__(self, x, y, colour):
		if (colour):
			symbol = "O"
		else:
			symbol = "o"
		super().__init__(x, y, symbol, colour)

	def __str__(self):
		return str(self.symbol)

	def isLigitMove(self, eX, eY):

		if (self.x == eX and self.y == eY):
			return False

		if Board.br[eX][eY].hasPiece() and Board.br[eX][eY].getPiece().getColour() == self.colour:
			return False

		if self.colour:
			if ( (eX - self.x == 1) and (abs(self.y - eY) == 1) and (not Board.br[eX][eY].hasPiece()) ):
				return True

		elif not self.colour:
			if ( (self.x - eX == 1) and (abs(self.y - eY) == 1) and (not Board.br[eX][eY].hasPiece()) ):
				return True

		if ( (self.x - eX == 2) and (self.y - eY == 2) and (Board.br[self.x - 1][self.y - 1].hasPiece()) and (Board.br[self.x - 1][self.y - 1].getPiece().getColour() != self.colour) and (not Board.br[eX][eY].hasPiece()) ):
			Board.br[self.x - 1][self.y - 1].removePiece()
			return True

		if ( (self.x - eX == 2) and (eY - self.y == 2) and (Board.br[self.x - 1][self.y + 1].hasPiece()) and (Board.br[self.x - 1][self.y + 1].getPiece().getColour() != self.colour) and (not Board.br[eX][eY].hasPiece()) ):
			Board.br[self.x - 1][self.y + 1].removePiece()
			return True

		if ( (eX - self.x == 2) and (self.y - eY == 2) and (Board.br[self.x + 1][self.y - 1].hasPiece()) and (Board.br[self.x + 1][self.y - 1].getPiece().getColour() != self.colour) and (not Board.br[eX][eY].hasPiece()) ):
			Board.br[self.x + 1][self.y - 1].removePiece()
			return True

		if ( (eX - self.x == 2) and (eY - self.y == 2) and (Board.br[self.x + 1][self.y + 1].hasPiece()) and (Board.br[self.x + 1][self.y + 1].getPiece().getColour() != self.colour) and (not Board.br[eX][eY].hasPiece()) ):
			Board.br[self.x + 1][self.y + 1].removePiece()
			return True

		return False