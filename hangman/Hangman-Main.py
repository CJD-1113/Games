from functions import hangman
import time
import random
import replit

#Declares variables
tries = 0
wrong = 0
global previous
previous = []
global positions 
positions = []
separator = ", "

#Opens word list and selects random word
line = random.randint(0, 2863)
file = open('Wordlist.txt')
content = file.readlines()
word = content[line].lower().strip()
length = len(word)

#As long as you have not guessed 6 times,
while wrong <= 6:
  #Clears the console each time
  time.sleep(1)
  replit.clear()
  #First time through set's the underscores
  if tries == 0:
    graphic = []
    for y in word:
      graphic.append("_")
  #Runs hangman function
  hangman(wrong)
  #Prints the graphic
  for z in graphic:
    print(z, end=" ")
  for w in word:
    positions.append(w)
  if "_" not in graphic:
    print("\nYou won!")
    break
  if wrong == 6:
    break
  #Takes input
  print(f"\nYou have guessed: {separator.join(previous)}") 
  guess = input("\nWhat letter/word are you guessing? ").lower()
    
  if guess in word:
    if guess != word:
      if guess != word:
        for l in range(length):
          if guess == positions[l]:
            graphic[l] = guess
  if guess not in word:
    wrong = wrong + 1
  if guess == word:
    print("You won!")
    break
  tries = tries + 1
  previous.append(guess)

if guess != word and wrong == 6 and "_" in graphic:
  print("\nYou lost :(")
  print(f"The word was: {word}")



