from piece import Piece
from board import Board
import sys
import os
class King(Piece):
	def __init__(self, x, y, colour):
		br = Board.getBoard()
		if (colour):
			symbol = "K"
		else:
			symbol = "k"
		super().__init__(x, y, symbol, colour)
	
	def __str__(self):
		return str(self.symbol)

	def __del__(self):
		if self.colour:
			print("Black won")
			os._exit(0)

		elif not self.colour:
			print("White won")
			os._exit(0)
	def isLigitMove(self, eX, eY):
		if Board.br[eX][eY].hasPiece() and Board.br[eX][eY].getPiece().getColour() == self.colour:
			return False
			
		if ( (abs(self.x - eX) == 1) or (abs(self.y - eY) == 1) or ((abs(self.x - eX) == 1) and (abs(self.y - eY) == 1)) ):
			return True

		return False