import random, os

words_file = open("eng.txt", "rt")
words = words_file.read().split()
words_file.close()


def clear(): os.system('cls') #on Windows System

def printString(count, answer, all_guesses):
	gesStr = "These all your guesses: "
	numOfUnders = len(gesStr) + 1 + len(all_guesses) * 5
	if numOfUnders < 30: numOfUnders = 40
	print("_" * numOfUnders)
	print(str(10 - count) + " guesses left.")
	print("The word so far: " + answer)
	print("These all your guesses: ", all_guesses)
	print("_" * numOfUnders)

def welcomeString():
	print("_" * 50)
	game_mode = input("\t\tHello to the Game!!!\n\t\n\t1. Easy\n\t2. Medium\n\t3. Hard\n\t4. You will lose don't worry\n\n" + "_" * 50 + "\n\nPlease choose the game mode: ")
	while (game_mode != "1" and game_mode != "2" and game_mode != "3" and game_mode != "4"):
		game_mode = input("Please enter one of the four options: ")
	return game_mode 

def extraDifficulty():
	pass


while True:
	game_mode = welcomeString()
	word = random.choice(words)
	len_word = len(word)
	if game_mode == "1":
		while len_word < 10:
			word = random.choice(words)
			len_word = len(word)
	elif game_mode == "2":
		while len_word >= 10 or len_word < 6:
			word = random.choice(words)
			len_word = len(word)
	elif game_mode == "3":
		while len_word >= 6:
			word = random.choice(words)
			len_word = len(word)
	elif game_mode == "4":
		extraDifficulty()

	count = 0
	win = False
	all_guesses = []
	answer = "-" * int(len_word)

	clear()
	printString(count, answer, all_guesses)

	while (count < 10 and win is False):
		guess = input("Enterg guess " + str(count) + "/10: ")

		if guess == "hint":
			print("\n\n"+word)
			input()
			clear()
			printString(count, answer, all_guesses)
			continue;

		while guess in all_guesses:
			clear()
			printString(count, answer, all_guesses)
			guess = input("\nEnter different guess, you have this one already: ")
		count += 1
		all_guesses.append(guess)
		tmp = ""
		i = 0
		while (i < len(word)):
		 	if (word[i] == guess):
		 		tmp += guess
		 	else:
		 		tmp += answer[i]
		 	i += 1
		if (answer != tmp):
			print("\nGreat guess")
			count = count - 1
			answer = tmp
		else:
			print("\nNot a great guess")

		if (answer == word):
			clear()
			print("YEY the word is ", word + "\n")
			print("Well done, you win!!!")
			win = True
			break

		clear()
		printString(count, answer, all_guesses)
	if (count == 10 and win is False):
		clear()
		print("Sorry, but you loose, correct word was: " + word)
	cho = input("Do you want play again? ").lower()
	if cho == "yes" or cho == "y":
		clear()
		continue
	else:
		break

input("Enter")
