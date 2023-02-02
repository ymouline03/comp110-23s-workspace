"""One shot Wordle."""
__author__ = '730611189'

secret: str = 'python'

guess: str = input('What is your 6-letter guess?')
while len(guess) != 6:
    print('That was not 6 letters! Try again:')
    guess: str = input()


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

count: int = 0
boxes: str = ''

while count <= 5:
    if guess[count] == secret[count]: 
        boxes += GREEN_BOX
    elif guess[count] in secret: 
        boxes += YELLOW_BOX
    elif guess[count] not in secret: 
        boxes += WHITE_BOX
    count += 1

print(boxes)
if boxes == GREEN_BOX * 6: 
    print('Woo! You got it!')
else: 
    print('Not quite. Play again soon.')
