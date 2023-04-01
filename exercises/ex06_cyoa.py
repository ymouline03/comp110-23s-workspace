'''EPIC BOSS BATTLE SIMULATOR'''

#importing modules
from time import sleep
import random

#global vars
__author__ = '730611189'
player: str = ''
points: int = 0
health: int = 0
UNAMUSED: str = "\U0001F612"
YAY: str = "\U0001F601"

#charcter attacks
opphealth = 150
mysticshot = 40
arcaneshift = 50
shotbarrage = 60
doublestrike = 40
alphastrike = 50
Yihealth = 120
highlander = 60
shroudofdarkness = 60
unspeakablehorror = 70
Nochealth = 90
paranoia = 40
loadeddice = 30
wildcard = 40
Fatehealth = 110
destiny = 80

def greet() -> None:
  '''game instructions'''
  print('Welcome to EPIC BOSS BATTLE SIMULATOR')
  sleep(2)
  print('The opponent you must face today goes by \"The Professor\"...')
  sleep(2.5)
  print('You will first start by choosing from 3 battle classes,')
  sleep(2.5)
  print('and then using the attacks that your class offers,')
  sleep(2.5)
  print('you will battle \"The Professor\" in an epic fight to the death!!!')
  sleep(2)
  print('Every time you beat the professor, you win 5 adventure points!')
  sleep(1.5)
  print('But everytime you lose to the professor, you lose 3 adventure points')
  sleep(2)
  print('You will battle the professor in 3 rounds')
  sleep(2)
  print('You win the game by getting to 20 points within the 3 rounds!')
  sleep(2)
  print('A round completes when either you or the professor loses all of their health')
  sleep(3)
  print('Additionally, you gain one adventure point when you pick your character at the start of each round, as well as after you pick each attack')
  sleep(2)
  global player
  player = input('Enter your name:')

def play() -> None:
  global player
  global points
  play_on: str = input(f'{player}, would you like to enter the game?(y/n)')
  if 'y' in play_on:
    points += 1
    print('Great! You get 1 adventure point for being adventurous')
  else:
    quit('Thanks for playing!')

def professor_stats_display() -> None:
  '''displays opponent stats'''
  print('Here are The Professors attacks/attack damage and health for reference\n(Note that attack damage is approximate and can be greater than or less than displayed amount on each turn due to varying effectiveness)')
  print(f'----The Professor----\nHealth = {opphealth} \nMystic shot = {mysticshot} \nArcane shift = {arcaneshift} \nShot barrage = {shotbarrage}')
  print()
  sleep(10)

def character_stats_display() -> None:
  '''displays character stats'''
  print(f'       (1)\n----MasterYi----\nDouble strike = {doublestrike} \nAlpha strike = {alphastrike} \nHighlander = {highlander} \nHealth = {Yihealth}')
  print()
  sleep(2)
  print(f'       (2)\n----Nocturne----\nShroud of darkness = {shroudofdarkness} \nUnspeakable horror = {unspeakablehorror} \nParanoia = {paranoia} \nHealth = {Nochealth}')
  print()
  sleep(2)
  print(f'       (3)\n----Twisted Fate----\nLoaded dice = {loadeddice} \nWildcard = {wildcard} \nDestiny = {destiny} \nHealth = {Fatehealth}')
  print()
  sleep(2)

def character_choice() -> int:
  '''prompts player to choose a character'''
  character_stats_display()
  while True:
    choice: int = int(input(f'{player}, Choose a class to battle with(type the number):\n(Note that attack damage is approximate and can be greater then or less than displayed amount on each turn due to varying effectiveness)\n 1. MasterYi\n 2. Nocturne\n 3. Twisted Fate\nMaking a choice will yield 1 adventure point'))
    if 0 < choice < 4:
      pass
    else:
      print('invalid input, enter the number')
    next: str = input('are you sure you want to continue?(y/n)')
    if 'y' in next: 
      global points
      points += 1
      global health
      if choice == 1:
        health += 120
      if choice == 2:
        health += 90
      if choice == 3:
        health += 110
      return choice

def attack_choice(character) -> int:
  '''prompts player to choose an attack'''
  if character == 1:
    print(f'----MasterYi----\n1. Double strike = {doublestrike} \n2. Alpha strike = {alphastrike} \n3. Highlander = {highlander}')
  if character == 2:
    print(f'----Nocturne----\n1. Shroud of darkness = {shroudofdarkness} \n2. Unspeakable horror = {unspeakablehorror} \n3. Paranoia = {paranoia}')
  if character == 3:
    print(f'----Twisted Fate----\n1. Loaded dice = {loadeddice} \n2. Wildcard = {wildcard} \n3. Destiny = {destiny}')
  while True:
    att = int(input(f'{player}, which attack do you choose?(type the number)\nYou gain 1 adventure point for picking each attack'))
    if 0 < att < 4:
      global points
      points += 1
      return att
    else:
      print('invalid input, type the number')
      
def MasterYi(attack_num) -> int:
  '''Master Yi damage calculator'''
  eff: int = random.randint(1,6)
  damage: int = 0
  if attack_num == 1:
    if 0 < eff < 3:
      damage += random.randint(38, 50)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(15, 30)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 10) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  if attack_num == 2: 
    if 0 < eff < 3:
      damage += random.randint(45, 60)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(25, 40)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 15) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  if attack_num == 3: 
    if 0 < eff < 3:
      damage += random.randint(65, 80)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(30, 45)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 20) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  return damage
  
def Nocturne(attack_num) -> int:
  '''Nocturne damage calculator'''
  eff: int = random.randint(1,6)
  damage: int = 0
  if attack_num == 1:
    if 0 < eff < 3:
      damage += random.randint(55, 70)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(20, 40)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 15) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  if attack_num == 2: 
    if 0 < eff < 3:
      damage += random.randint(65, 80)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(25, 45)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 15) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  if attack_num == 3: 
    if 0 < eff < 3:
      damage += random.randint(35, 50)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(15, 25)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 10) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  return damage

def TwistedFate(attack_num) -> int:
  '''Twisted Fate damage calculator'''
  eff: int = random.randint(1,6)
  damage: int = 0
  if attack_num == 1:
    if 0 < eff < 3:
      damage += random.randint(25, 40)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(10, 20)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 5) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  if attack_num == 2: 
    if 0 < eff < 3:
      damage += random.randint(35, 50)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(15, 25)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 10) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  if attack_num == 3: 
    if 0 < eff < 3:
      damage += random.randint(75, 90)
      print(f'Your attack was very effective and dealt {damage} damage!')
    elif 2 < eff < 6:
      damage += random.randint(30, 55)
      print(f'Your attack was somewhat effective and dealt {damage} damage!')
    elif eff == 6:
      damage += random.randint(0, 20) 
      print(f'Your attack was ineffective and dealt {damage} damage!')
  return damage
  
def Professor() -> int:
  '''The Professor damage calculator'''
  oppeff: int = random.randint(1, 10)
  oppatt: int = random.randint(1, 3)
  damage: int = 0
  if oppatt == 1:
    if 0 < oppeff < 5:
      damage += random.randint(38, 45)
      print('The Professor has used Mystic Shot')
      print(f'The Professors attack was very effective and dealt {damage} damage!')
    elif 4 < oppeff < 9:
      damage += random.randint(15, 30)
      print('The Professor has used Mystic Shot')
      print(f'The Professors attack was somewhat effective and dealt {damage} damage!')
    elif 8 < oppeff < 11:
      damage += random.randint(0, 10) 
      print('The Professor has used Mystic Shot')
      print(f'The Professors attack was ineffective and dealt {damage} damage!')
  if oppatt == 2: 
    if 0 < oppeff < 5:
      damage += random.randint(45, 60)
      print('The Professor has used Arcane Shift')
      print(f'The Professors attack was very effective and dealt {damage} damage!')
    elif 4 < oppeff < 9:
      damage += random.randint(25, 40)
      print('The Professor has used Arcane Shift')
      print(f'The Professors attack was somewhat effective and dealt {damage} damage!')
    elif 8 < oppeff < 11:
      damage += random.randint(0, 15) 
      print('The Professor has used Arcane Shift')
      print(f'The Professors attack was ineffective and dealt {damage} damage!')
  if oppatt == 3: 
    if 0 < oppeff < 5:
      damage += random.randint(55, 70)
      print('The Professor has used Shot Barrage')
      print(f'The Professors attack was very effective and dealt {damage} damage!')
    elif 4 < oppeff < 9:
      damage += random.randint(30, 45)
      print('The Professor has used Shot Barrage')
      print(f'The Professors attack was somewhat effective and dealt {damage} damage!')
    elif 8 < oppeff < 11:
      damage += random.randint(0, 20) 
      print('The Professor has used Shot Barrage')
      print(f'The Professors attack was ineffective and dealt {damage} damage!')
  return damage

def main() -> None:
  '''Runs the game from start to finish'''
  greet()
  play()
  round: int = 1
  opphealth: int = 150
  global points
  global health
  global player
  print(f'{player}, you currently have {points} adventure points')
  professor_stats_display()
  while round < 4:
    opphealth = 150
    health = 0
    character = character_choice()
    while health > 0 and opphealth > 0:
      print(f'Round {round}:')
      sleep(2)
      attack = attack_choice(character)
      if character == 1:
        opphealth -= MasterYi(attack)
      if character == 2:
        opphealth -= Nocturne(attack)
      if character == 3:
        opphealth -= TwistedFate(attack)
      sleep(4)
      print(f'The Professor has {opphealth} heath remaining!')
      sleep(3)
      if opphealth <= 0:
        break
      print('It is now The Professors turn to attack!')
      sleep(2)
      health -= Professor()
      sleep(4)
      print(f'You have {health} health remaining!')
      sleep(2)
    if health <= 0:
      print(f'You have fallen to the wrath of The Professor in round {round}')
      sleep(2)
      points -= 3
      print('You have lost 3 adventure points')
      sleep(2)
    if opphealth <= 0:
      print(f'Congrats! You beat the professor in round {round}!')
      sleep(2)
      points += 5
      print('You have won 5 adventure points!')
    print(f'You noew have {points} points')
    sleep(3)
    if points >= 20:
      print('YOU WIN!!!')
      print(YAY)
      break  
    next_round: str = input('Would you like to continue to the next round?(y/n)')
    if 'y' in next_round:
      pass
    else:
      break
    round += 1
  if points < 20:
    print('Sorry, you are out of rounds, and you lose')
    print(UNAMUSED)
  print('Thanks for playing!')
  
if __name__ == "__main__":
  main()  