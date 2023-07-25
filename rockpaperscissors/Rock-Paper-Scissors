"""
CATE DICKSTEIN
2-23-22
"""

import replit
import time
import random

def rock():
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
@wynand1004
""")

def paper():
  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
@wynand1004
""")

def scissors():
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
@wynand1004
""") 

cpu1 = ["Rock", "Paper", "Scissors"]
decision = "yes"
ran = random.randint(0, 2)
cpu2 = cpu1[ran]
tie = 0
win = 0
lose = 0

print("Rock Paper Scissors")

while decision == "yes":
  character = input("Which one do you want to be? ").title()
  time.sleep(2)
  replit.clear
  
  if character == "Rock":
    rock()
    if cpu2 == "Rock":
      rock()
      print("You tied :/")
      tie = tie + 1
    if cpu2 == "Paper":
      paper()
      print("You lost :(")
      lose = lose + 1
    if cpu2 == "Scissors":
      scissors()
      print("YOU WON! :)")
      win = win + 1
    
  if character == "Paper":
    paper()
    if cpu2 == "Rock":
      rock()
      print("YOU WON! :)")
      win = win + 1
    if cpu2 == "Paper":
      paper()
      print("You tied :/")
      tie = tie + 1
    if cpu2 == "Scissors":
      scissors()
      print("You lost :(")
      lose = lose + 1
    
  if character == "Scissors":
    scissors()
    if cpu2 == "Rock":
      rock()
      print("You lost :(")
      lose = lose + 1
    if cpu2 == "Paper":
      paper()
      print("YOU WON! :)")
      win = win + 1
    if cpu2 == "Scissors":
      scissors()
      print("You tied :/")
      tie = tie + 1

  time.sleep(5)
  replit.clear()

  decision = input("Do you want to play again? ").lower()

print(f"""
You have tied {tie} time/s
You have won {win} time/s
You have lost {lose} time/s""")
print("Thanks for playing :)")

