# Checks user input to determine it's a number
def get_input():
  while True:
    print('')
    guess = input('What is your guess?: ')
    try:
      guess = int(guess)
      return guess # Exit the loop if the conversion was successful
    except ValueError:
      print('Mate, please enter a valid number. No shenanigans.')
      print('')