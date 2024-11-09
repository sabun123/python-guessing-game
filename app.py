# 9 November 2024 - Yusuf Ismail Shukor
# Guessing game that randomly select a number between 1 and 10


import random
from app.greet import greet_player
from app.get_input import get_input


greet_player()

print('I have selected a number between 1 and 10, try and guess what it is.')
selected_number = random.randint(1,10)

# Keep asking the user for guesses until they guess the correct number
guess = get_input()

print('You guessed: ', guess)
print('')

while int(guess) != selected_number:
  print('No dice, try again!')
  guess = get_input()
  print('You guessed: ', guess)

print('You got it! The number was: ', selected_number)

print('GAME OVER')

print('')