'''One shot Wordle'''
__author__ = 730611189

word: str = input('Enter a 6 character word: ')
if len(word) != 6: 
  print('Error: Word must contain 6 characters')
  exit()

guess: str = input('Guess a 6 character word: ')
if len(guess) != 6:
  print('Error: Word must be 6 letters')
  exit()

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

count = 0
boxes = [WHITE_BOX, WHITE_BOX, WHITE_BOX, WHITE_BOX, WHITE_BOX, WHITE_BOX]

while count <=5:
  if guess[count] == word[count]: boxes[count] = GREEN_BOX
  elif guess[count] in word: boxes[count] = YELLOW_BOX
  elif guess[count] not in word: pass
  count += 1

if boxes == [GREEN_BOX, GREEN_BOX, GREEN_BOX, GREEN_BOX, GREEN_BOX, GREEN_BOX]: 
  boxes = ''.join(boxes)
  print(boxes)
  print('Woo! You got it!')
else: 
  boxes = ''.join(boxes)
  print(boxes)
  print('Not quite. Play again soon.')
    