"""Structured Wordle."""

__author__ = '730611189'

def contains_char(str_search: str, str_one_char: str) -> bool:
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

def emojified(guess: str, secret: str) -> str:
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


def input_guess(expected_length: int) -> str:
  '''checks for correct guess length'''
  correct_len_guess: str = input(f'What is your {expected_length} letter guess?')
  while len(correct_len_guess) != expected_length:
    correct_len_guess: str = input(f'That was not {expected_length} letters! Try again:')
  return correct_len_guess
  

def main() -> None:
  '''The entrypoint of the program and main game loop.'''
  secret_word: str = 'codes'
  turns: int = 0
  guess: str = ''
  while turns <= 5 and secret_word != guess:
    turns += 1
    print(f'=== Turn {turns}/6 ===')
    guess = input_guess(len(secret_word))
    boxes = emojified(guess, secret_word)
    print(boxes)
  if turns <= 5: print(f'You won in {turns}/6 turns')
  else: print('X/6 - Sorry, try again tomorrow!')

if __name__ == "__main__":
  main()


