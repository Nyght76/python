# Hangman
import random
import string

def draw_gallows(incorrect):
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
		print("\n" + ("YOU LOSE!!!  " * 19))
	return

def wordplay(the_word, guess, used):
	temp_word=[]
	
	for item in word_list[the_word]['word'].lower():
		if item == ' ':
			temp_word.append (' ')
		elif item in used:
			temp_word.append (item)
		else:	
			temp_word.append ('?')

	return temp_word
	
def playgame(the_word, used, end):
	incorrect = 0
	while incorrect <= 7 and not end:
		print("Your HINT:", word_list[the_word]['hint'])
		print('Letters Used: ',used)
		guess = input('Give me a letter: ')
		print('You guessed a(n)', guess)
		if guess.lower() in word_list[the_word]['word'].lower():
			print('There is/are', word_list[the_word]['word'].lower().count(guess), guess+"'s in the word!")
			used += guess.lower()
			draw_gallows(incorrect)
		else:
			print('There are no', guess+"'s in the word...")
			incorrect += 1
			draw_gallows(incorrect)
			used += guess.lower()

		temp_word = wordplay(the_word, guess, used)
		
		if ''.join(temp_word) == word_list[the_word]['word'].lower():
			print('Yes, the answer is', word_list[the_word]['word'])
			print('You win '*16)

			end = True

		if end != True:
			print('Thus far: ', ''.join(temp_word))
			print('\n')
		if end == True:
			print('You win '*16)

## MAIN PROGRAM ##

word_list = []
incorrect = 0

infile = open('E:\data.csv','r')
for line in infile:
	row = line.split(',')
	row[0] = row[0].strip()
	row[1] = row[1].strip()
	word_list.append({'word':row[0],'hint':row[1]})

the_word = random.randint(0,len(word_list))
guess = ''
used = []
end = False

playgame(the_word, used, end)