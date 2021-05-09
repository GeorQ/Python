from piece import Piece
from board import Board
class Rock(Piece):
	br = Board.getBoard()
	def __init__(self, x, y, colour):
		if (colour):
			symbol = "R"
		else:
			symbol = "r"
		super().__init__(x, y, symbol, colour)
	
	def __str__(self):
		return str(self.symbol)

	def isLigitMove(self, eX, eY):
		if Board.br[eX][eY].hasPiece() and Board.br[eX][eY].getPiece().getColour() == self.colour:
			return False

		if ((abs(eX - self.x) < 8) and (self.y == eY)):
			if self.x < eX:
				for i in range(self.x + 1, eX):
					if Board.br[i][self.y].hasPiece():
						return False
				return True
			elif self.x > eX:
				for i in range(self.x - 1, eX):
					if Board.br[i][self.y].hasPiece():
						return False
				return True

		if ((self.x == eX) and (abs(eY - self.y) < 8)):
			if self.y < eY:
				for i in range(self.y + 1, eY):
					if Board.br[self.x][i].hasPiece():
						return False
				return True
			elif self.y > eY:
				for i in range(self.y - 1, eY):
					if Board.br[self.x][i].hasPiece():
						return False
				return True

		return False