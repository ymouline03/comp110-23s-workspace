#Wordle kind of
__author__ = "730611189"

print('Welcome to chardle. Player one will enter a 5 letter word and player 2 will try to guess the word letter by letter in 6 turns')

while True:
  word = input('Player 1, enter a word for player 2 to guess')
  if len(word) != 5: print('word must be 5 letters')
  else: break

bank = []
wordrev = '_____'

while True:
  guess = input('player 2, enter a letter')
  if guess == '': print('invalid guess') 
  elif len(guess) > 1: print('you can only guess one letter at a time')
  elif guess in bank: print('letter already guessed')    
  elif guess in word:
    print(guess, 'appears in the secret word', word.count(guess), 'time(s)')
    bank.append(guess)
    wordrevlist = list(wordrev)
    for i in range(0, 5):
      if word[i] == guess: wordrevlist[i] = guess
    wordrev = ''.join(wordrevlist)
    if wordrev == word: 
      print('You guessed it! The word was', wordrev, '. Thanks for playing.')
      break
    else: print('New word: ', wordrev) 
  else: 
    print('Letter not in word, try again.')
    
