from square import Square

class Board(object):
	queue = []
	br = [ [], [], [], [], [], [], [], [] ]
	def __init__(self):
		for i in range(8):	
			for j in range(8):
				Board.br[i].append(Square(i, j))
		# self.initialisePieces()

	def printBoard(self):
		print("   A B C D E F G H\n")
		for i in range(8):
			print(str(i + 1), end="  ")
			for j in range(8):
				print(Board.br[i][j], end=" ")
			print(" " + str(i + 1))
		print("\n   A B C D E F G H \n")

	def setPiece(self, x, y, piece):
		Board.br[x][y].setPiece(piece)

	@staticmethod
	def getBoard():
		return Board.br

	def getPiece(self, x, y):
		return Board.br[x][y].getPiece()

	def movePiece(self, xS, yS, xE, yE):
		pc = Board.br[xS][yS].getPiece()
		Board.br[xS][yS].getPiece().updateCoordinates(xE, yE)
		Board.br[xE][yE].setPiece(pc)
		Board.br[xS][yS].removePiece()
	
	def hasPiece(self, x, y):
		return Board.br[x][y].hasPiece()

	def saveBoard(self):
		ls = [[],[],[],[],[],[],[],[]]
		for i in range(8):	
			for j in range(8):
				ls[i].append(Square(i, j)) 
		for i in range(8):
			for j in range(8):
				if Board.br[i][j].hasPiece():
					ls[i][j].setPiece(Board.br[i][j].getPiece())
		Board.queue.append(ls)

	def returnLastBoard(self):
		Board.br = Board.queue.pop(0)