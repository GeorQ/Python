from board import Board

from square import Square
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rock import Rock
from queen import Queen
from king import King
from testPiece import TestPiece
from shashka import Shashka
from ultraPony import UltraPony

listForInt = ["1", "2", "3", "4", "5", "6", "7", "8"]
listForChars = ["a", "b", "c", "d", "e", "f", "g", "h"]

turn = True # When true white goes, when false black goes 

def initialisePiecesChess(board):
		for i in range(8):		
			board.setPiece(1, i, Pawn(1, i, True))
			board.setPiece(6, i, Pawn(6, i, False))

		board.setPiece(0, 1, Knight(0, 1, True))
		board.setPiece(0, 6, Knight(0, 6, True))
		board.setPiece(7, 1, Knight(7, 1, False))
		board.setPiece(7, 6, Knight(7, 6, False))

		board.setPiece(0, 2, Bishop(0, 2, True))
		board.setPiece(0, 5, Bishop(0, 5, True))
		board.setPiece(7, 2, Bishop(7, 2, False))
		board.setPiece(7, 5, Bishop(7, 5, False))

		board.setPiece(0, 0, Rock(0, 0, True))
		board.setPiece(0, 7, Rock(0, 7, True))
		board.setPiece(7, 0, Rock(7, 0, False))
		board.setPiece(7, 7, Rock(7, 7, False))

		board.setPiece(0, 4, King(0, 4, True))
		board.setPiece(7, 4, King(7, 4, False))

		board.setPiece(0, 3, Queen(0, 3, True))
		board.setPiece(7, 3, Queen(7, 3, False))

		board.setPiece(2, 3, TestPiece(2, 3, True))
		board.setPiece(5, 3, TestPiece(5, 3, False))

		board.setPiece(2, 1, UltraPony(2, 1, True))
		board.setPiece(5, 6, UltraPony(5, 6, False))

		board.setPiece(2, 0, Shashka(2, 0, True))
		board.setPiece(2, 7, Shashka(2, 7, True))
		board.setPiece(5, 0, Shashka(2, 0, False))
		board.setPiece(5, 7, Shashka(5, 7, False))

def initialisePiecesCheckers(board):
		for i in range(0, 8, 2):		
			board.setPiece(0, i + 1, Shashka(0, i + 1, True))
			board.setPiece(1, i, Shashka(1, i, True))
			board.setPiece(2, i + 1, Shashka(2, i + 1, True))

		for i in range(0, 8, 2):		
			board.setPiece(5, i, Shashka(5, i, False))
			board.setPiece(6, i + 1, Shashka(6, i + 1, False))
			board.setPiece(7, i, Shashka(7, i, False))

def cleanMove(move):
	moveX = int(move[1]) - 1
	moveY = 0
	for i in listForChars:
		if move[0] == i:
			break
		else:
			moveY += 1
	return moveX, moveY

def getInput(option, piece = None):
	if option == 0:
		move = input("Choose the piece: ").lower()
	else:
		move = input("Please make your move: ").lower()

	if move == "откат":
		return "continue"

	if move == "откатд":
		return "fullBack"

	while not isLegitMove(move, option, piece):
		move = input("Please make correct move: ").lower()
		if move == "откат":
			print("I was here")
			return "continue"
	return cleanMove(move)


def isLegitMove(move, option, piece = None):
	if len(move) != 2:
		return False
	if move[0] not in listForChars:
		return False
	if move[1] not in listForInt:
		return False
	cnMove = cleanMove(move)
	moveX = cnMove[0]
	moveY = cnMove[1]
	if option == 0:
		if not ( board.hasPiece(moveX, moveY) and (board.getPiece(moveX, moveY).getColour() == turn) ):
			print("There is no piece here or it's not ur turn to move")
			return False
	if option == 1:
		if piece == None:
			print("Impossible situation")
			return False
		if not piece.isLigitMove(moveX, moveY):
			return False
	return True

gameOption = int(input("Во что Вы хотите поиграть?\n1 - Шахматы\n2 - Шашки\nВаш выбор: "))

board = Board()

if gameOption == 1:
	initialisePiecesChess(board)
	while True:
		board.printBoard()
		cleanS = getInput(0)
		if cleanS == "continue":
			continue
		if cleanS == "fullBack":
			board.returnLastBoard()
			continue
		cleanF = getInput(1, board.getPiece(cleanS[0], cleanS[1]))
		if cleanF == "continue":
			continue
		board.movePiece(cleanS[0], cleanS[1], cleanF[0], cleanF[1])
		board.saveBoard()
		turn = not turn

if gameOption == 2:
	initialisePiecesCheckers(board)
	while True:
		board.printBoard()
		cleanS = getInput(0)
		if cleanS == "continue":
			continue
		cleanF = getInput(1, board.getPiece(cleanS[0], cleanS[1]))
		if cleanF == "continue":
			continue
		board.movePiece(cleanS[0], cleanS[1], cleanF[0], cleanF[1])
		turn = not turn