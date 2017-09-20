import random

amt = 30
guesses = 7
count = 0

vocab = ['rockstars','sisters','brothers','parents','slippery','tongue','branches','planets']
word = random.choice(vocab)
length = len(word)

correct_guess = length * ['_']
ltr_guess = ''

def print_money():
	print('you have $' + str(amt))

def print_output():
	print(''.join([str(x) + " " for x in correct_guess]))

print('\nLet\'s play hangman.\nGuess the mystery word with less than ' + str(guesses) + ' errors.\n')
print('The word is ' + str(length) + ' letters long.')
print_output()
print('')

play = 'y'

while (amt>=5) and (guesses>0) and (play=='y'):
	print('-----------------------------')
	print_money()
	print('You have ' + str(guesses) + ' guesses left.')
	print_output()
	print('Letter(s) you\'ve guessed: ' + ltr_guess)
	print()
	letter = str(input('Please guess a letter from A to Z or "quit" to exit game: '))
	if letter == "quit":
		break
	elif letter in ltr_guess:
		print()
		print('You have already guessed this letter.\nPlease try again.')
		print()
	elif letter not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
		print('That is not a letter. Please enter a letter.')
		print()
	elif letter in word:
		ltr_guess = ltr_guess + " " + letter
		amt = amt + 5
		for i,x in enumerate(word):
			if x is letter:
				correct_guess[i] = letter
				count = count + 1
		print()
		if count == length:
		    print('Yes! The secret word is "' + word + '"! You have won!')
		    break
		else:
			print('You guessed correctly.')
			print_output()
			print()
			print_money()
			print('You have ' + str(guesses) + ' guesses left.')
			print('Letter you\'ve guessed: ' + ltr_guess)
			print()
	else:
		ltr_guess = ltr_guess + " " + letter
		amt = amt - 5
		guesses = guesses - 1
		print()
		print('You guessed wrong.')
		print_output()
		print()
		print_money()
		print('You have ' + str(guesses) + ' guesses left.')
		print('Letter you\'ve guessed: ' + ltr_guess)
		print()
		if (guesses < 0) or (amt < 5):
			print()
			print('Sorry, you have lost.\nYou have ' + str(guesses) + ' guesses left.\nYou have $' + str(amt))