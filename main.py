import random

while True:
	print('Your choice:')
	choice = str(input())
	choice = choice.lower()

	print("Your choice is", choice)

	choices = ['rock', 'paper', 'scissors']

	computer_choice = random.choice(choices)

	print("Computer's choice is", computer_choice)
    #if tie
	if choice in choices:
		if choice == computer_choice:
			print('it is a tie')
       #option1
		if choice == 'rock':
			if computer_choice == 'paper':
				print('Computer wins')
			elif computer_choice == 'scissors':
				print('You win')
       #option2
		if choice == 'paper':
			if computer_choice == 'scissors':
				print('Computer wins')
			elif computer_choice == 'rock':
				print('You win')

        #option3
		if choice == 'scissors':
			if computer_choice == 'rock':
				print('Computer wins')
			elif computer_choice == 'paper':
				print('You win')
	else:
		print('Invalid choice, please enter correct value')

	print()
