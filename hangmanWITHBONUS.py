# Hangman
import random
import string
import time

def difficulty():
	
	print('---------------------------------------------')
	print('Choose Difficulty for ALL players:')
	print('1: Beginner\t\t(Blank slate, room for error)')
	print('2: Normal\t\t(The base is started) [Default Difficulty]')
	print('3: Hard\t\t\t(The base is almost complete)')
	print('4: Insanity\t\t(Your head is almost in the noose)')
	
	try:
		diff_level = int(input("Pick a difficulty level (1-4) "))
		while int(diff_level) not in range(1,5,1):
			diff_level = input('Seriously... 1 2 3 4 only ')
	except:
		diff_level = 2
		print('Default difficulty auto-selected: (2: Normal)')
	print('---------------------------------------------')
	print('Difficulty level', str(diff_level), 'selected.')
	print('---------------------------------------------')
	pause_game()
	return diff_level

def draw_gallows(incorrect):
	lose = False
	if(incorrect==0):
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("\n")
	elif(incorrect==1):
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("  =======")
	elif(incorrect==2):
		print("\n")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("    /|\\")
		print("  =======")
	elif(incorrect==3):
		print(" _____")
		print(" |   |")
		print("     |")
		print("     |")
		print("     |")
		print("    /|\\")
		print("  =======")
	elif(incorrect==4):
		print(" _____")
		print(" |   |")
		print(" 0   |")
		print("     |")
		print("     |")
		print("    /|\\")
		print("  =======")
	elif(incorrect==5):
		print(" _____")
		print(" |   |")
		print(" 0   |")
		print("/|   |")
		print("     |")
		print("    /|\\")
		print("  =======")
	elif(incorrect==6):
		print(" _____")
		print(" |   |")
		print(" 0   |")
		print("/|\\  |")
		print("     |")
		print("    /|\\")
		print("  =======")
	elif(incorrect==7):
		print(" _____")
		print(" |   |")
		print(" 0   |")
		print("/|\\  |")
		print("/    |")
		print("    /|\\")
		print("  =======")
	else:
		print(" _____")
		print(" |   |")
		print(" 0   |")
		print("/|\\  |")
		print("/ \\  |")
		print("    /|\\")
		print("  =======")
		print("YOU LOSE!!!")
		lose = True
	return lose

def clearscreen():
	print(chr(27) + "[2J")
	print('Note: [2J will clear the screen in anything but SUBLIME...')
	#and because Sublime does not run clear console command:
	print('\n'*30)
	time.sleep(1)

def wordplay(the_word, guess, used):
	temp_word=[]
	
	for char in word_list[the_word]['word'].upper():
		if char == ' ':
			temp_word.append (' ')
		elif char in used:
			temp_word.append (char.upper())
		else:	
			temp_word.append ('?')

	return temp_word
	
def playgame(the_word, used, end, diff_level, word_list):
	incorrect = 0 + int(diff_level-1)
	used = []
	end = False
	lose = False
	win = False
	guess = ''
	while incorrect <= 7 and not end and not lose and not win:
		print("Your HINT:", word_list[the_word]['hint'].upper())
		print('Letters Used: ',used)
		print('The Answer:',''.join(wordplay(the_word, guess, used)))
		guess = input('Give me a letter: ')
		while guess.upper() in used or guess.upper() not in string.ascii_uppercase or guess=='':
			guess = input("Oops! Either you've used that one already or it's not a character... Try again: ")

		if guess.upper() in word_list[the_word]['word'].upper():
			print('There is/are', word_list[the_word]['word'].lower().count(guess.lower()), guess.upper()+"'s in the answer!")
			used += guess.upper()
			lose = draw_gallows(incorrect)
		else:
			print('There are no', guess.upper()+"'s in the answer...")
			incorrect += 1
			lose = draw_gallows(incorrect)
			used += guess.upper()

		temp_word = wordplay(the_word, guess, used)
		
		if ''.join(temp_word) == word_list[the_word]['word'].upper():
			print('Yes, the answer is', word_list[the_word]['word'])
			print('You win the round!')
			pause_game()
			win = True
			end = True

		elif end != True and not lose:
			print('Thus far: ', ''.join(temp_word))
			print('\n')
		elif lose == True:
			print('The answer was:', word_list[the_word]['word'])
			pause_game()
	return win, lose, end

def solostart():
	word_list = []
	incorrect = 0

	infile = open('E:\data.csv','r')
	for line in infile:
		row = line.split(',')
		row[0] = row[0].strip()
		row[1] = row[1].strip()
		word_list.append({'word':row[0],'hint':row[1]})

	the_word = random.randint(0,len(word_list)-1)
	guess = ''
	used = []
	end = False
	return word_list, incorrect, the_word, guess, used, end

def num_players():
	print('Welcome to Hangman!')
	print('Guess the answer before you hang yourself...')
	print('---------------------------------------------')
	print('Game Options:')
	print('1: Just you vs the computer. [Default setting]')
	print('2: Two players - Head to Head.')
	
	
	try:
		how_many = int(input("How many players? (1-2) "))
		while int(how_many) not in range(1,3,1):
			how_many = input('Seriously... 1 2 3 4 only ')
		if int(how_many) == 1:
			print('---------------------------------------------')
			print('Single Player Rules:')
			print('If you get the answer before you hang yourself, you GAIN a point!')
			print('If you hang yourself before reaching the answer, you LOSE a point!')
			print('You CANNOT get a negative score: the lowest possible score is ZERO (0) points.')
			print('How high of a score can you achieve?')
			print('---------------------------------------------')
		if int(how_many) > 1:
			print('---------------------------------------------')
			print('Multiplayer Rules:')
			print('If you get the answer before you hang yourself, you GAIN a point!')
			print('If you hang yourself before reaching the answer, you LOSE a point!')
			print('The winner is the first player to reach SEVEN (7) points!')
			print('You CANNOT get a negative score: the lowest possible score is ZERO (0) points.')
			print('For fairness: Scores are tallied after both players have taken their turn.')
			print('---------------------------------------------')
	except:
		how_many = 1
		print('Default number of players auto-selected: (1 vs CPU)')
	print('Preparing',how_many, 'player game...', )
	return int(how_many)

def multistart(how_many, round):
	word_list = []
	guess = ''
	used = []
	end = False
	clearscreen()
	print('Round:',round)
	print('Time to stump your opponent:')
	for num in range(0, how_many,1):
		chooseword = ''
		choosehint = ''
		good = False
		print('Everyone but Player'+str(num+1), 'should look away now...')
		while not good or chooseword == '' or choosehint == '':
			chooseword = input('Player'+str(num+1)+' word: ')
			choosehint = input('Player'+str(num+1)+' hint: ')
			print('\n')
			print("You have chosen:")
			print("WORD:", chooseword.upper())
			print("HINT:", choosehint.upper())
			if str(chooseword) == '' or str(choosehint) == '' or (chooseword.isnumeric()):
				print("\tNot picking a word or hint is kind of cheating...")
				print("\tYou have been warned...")
				print("Try again...")
			else:
				check = input('Is this correct/acceptable? (y/n) ')
				if str(check[0].lower()) == 'y':
					good = True
				elif str(check[0].lower()) == 'n':
					print("It's ok to change your mind... but the other Player is waiting!")
					print("Try again...")
				elif str(chooseword) == '' or str(choosehint) == '':
					print("Not picking a word or hint is kind of cheating...")
					print("You have been warned...")
					print("Try again...")
				else:
					print("It's ok to change your mind... but the other Player is waiting!")
					print("Try again...")
			#except:
				#good = True
				#print("Continuing on...")
		word_list.append({'word':chooseword,'hint':choosehint})
		if num < how_many-1 and good:
			nextplayer = input('Hit [Enter] to continue, and then give Player'+str(num+2)+' the keyboard...')
			clearscreen()

	print(word_list)
	return word_list, guess, used, end

def pause_game():
	time.sleep(1)
	input('Hit [Enter] to continue...')
	time.sleep(1)

how_many = int(num_players())

round = 1
keepplaying = True
scores = []

if how_many == 1:
	scores.append (0)
	#while keepplaying == True:
	word_list, incorrect, the_word, guess, used, end = solostart()
	diff_level = difficulty()
	while keepplaying == True:
		win, lose, end = playgame(the_word, used, end, diff_level, word_list)
		if win:
			scores[0] += 1
		else:
			scores[0] -= 1
			if scores[0] < 0:
				scores[0] = 0
		#pause_game()
		clearscreen()
		print('-----------------------------')
		print('|Round:', round,'\t\t\t\t\t|')
		print('|Score:', scores[0],'\t\t\t\t\t|')
		print('-----------------------------')
		round +=1
		pause_game()
		good = False
		while not good:
			check = input('Shall we keep playing? (y/n) ')
			if str(check[0].lower()) == 'y':
				good = True
				keepplaying = True
				word_list, incorrect, the_word, guess, used, end = solostart()
			elif str(check[0].lower()) == 'n':
				print("Thank you for playing!")
				good = True
				keepplaying = False
			else:
				good = False

else:
	diff_level = difficulty()
	word_list, guess, used, end = multistart(how_many, round)

	for num in range (0, how_many):
		scores.append (0)
	the_word = 0
	while max(scores) < 7:
		
		for num in range (0,int(how_many)):
			used = []
			clearscreen()
			print("Player"+str(num+1)+": you're up...")
			win, lose, end = playgame(the_word, used, end, diff_level, word_list)
			if win == True:
				scores[num] += 1
			if lose == True:
				scores[num] -= 1
				if scores[num] < 0:
					scores[num] = 0
			the_word += 1
		
		if max(scores) != 7:
			clearscreen()
			print('-----------------------------')
			print('|Round', round,'score: \t\t\t|')
			for num in range (0,int(how_many)):
				print("| Player"+str(num+1)+":", scores[num], "points \t\t|")
			if scores[0] == scores[1]:
				print("| The scores are Tied! \t\t|")
			elif scores[0] > scores[1]:
				print("| Player1 is Winning (+"+str(int(scores[0]-scores[1]))+")\t|")
			else:
				print("| Player2 is Winning (+"+str(int(scores[1]-scores[0]))+")\t|")
			print('-----------------------------')
			pause_game()
			round += 1
			the_word = 0
			word_list, guess, used, end = multistart(how_many, round)

		if max(scores) == 7:
			clearscreen()
			print('-----------------------------')
			print('|Round', round,'score: \t\t\t|')
			for num in range (0,int(how_many)):
				print("| Player"+str(num+1)+":", scores[num], "points \t\t|")
			if scores[0] == scores[1]:
				print("| The scores are Tied! \t\t|")
			elif scores[0] > scores[1]:
				print("| Player1 Wins! (+"+str(int(scores[0]-scores[1]))+")\t|")
			else:
				print("| Player2 Wins! (+"+str(int(scores[1]-scores[0]))+")\t|")
			print('-----------------------------')
			pause_game()
			print("Thank you for playing!")






