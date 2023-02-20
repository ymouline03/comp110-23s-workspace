"""Structured Wordle."""

__author__ = '730611189'

def contains_char(str_search, str_one_char) -> str:
  '''searching for a matching index'''
  assert len(str_one_char) == 1
  index = 0
  while index <= len(str_search) - 1:
    if str_one_char == str_search[index]:
      return True
    index += 1
  return False

#stuff
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess, secret) -> str:
  '''inserting correct colored boxes'''
  boxes = ''
  assert len(secret) == len(guess)
  index = 0
  while index < len(guess):
    bool = contains_char(secret, guess[index])
    if bool == True:
      if guess[index] == secret[index]: boxes += GREEN_BOX
      else: boxes += YELLOW_BOX
    elif bool == False: boxes += WHITE_BOX
    index +=1
  return boxes


def input_guess(expected_length) -> int:
  '''checks for correct guess length'''
  correct_len_guess: str = input('What is your 6 letter guess?')
  while len(correct_len_guess) != expected_length:
    print('That was not', expected_length, 'letters! Try again:')
    correct_len_guess: str = input()
  return correct_len_guess
  

def main() -> None:
  secret_word = 'python'
  length = len(secret_word)
  turns = 0
  boxes = ''
  while turns <= 6:
    if boxes == GREEN_BOX * len(secret_word):
      print('You won in', turns ,'/6 turns!')
      exit()
    turns += 1
    print('=== Turn ', turns, '/6 ===')
    guess = input_guess(length)
    boxes = emojified(guess, secret_word)
    print(boxes)
  print('X/6 - Sorry, try again tomorrow!')
  
main()


