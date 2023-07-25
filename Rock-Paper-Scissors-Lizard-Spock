"""
CATE DICKSTEIN
2-23-22
"""

import replit
import time
import random

def spock():
  print("""
        _    _
     _ / \\  / \\ _
    / \\| |  | |/ \\ 
    |  | |  | || |
 _  |  | \\  / || |
/ \ |  |  \\/  || |
\\  \\|  |      || |
 \\               |  
  \\             /
   \\___________/

    Spock
""")

def lizard():
  print("""

    ___________
---(   ________)
     /     / )     
     \\____/ /          
---\\_______/ 

    Lizard
        """)

def rock():
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
@wynand1004
    Rock
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
    Paper
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
    Scissors
""") 

def dialogue():
  print("""
  Scissors cuts Paper
  Paper covers Rock
  Rock crushes Lizard
  Lizard poisons Spock
  Spock smashes Scissors
  Scissors decapitates Lizard
  Lizard eats Paper
  Paper disproves Spock
  Spock vaporizes Rock
  (and as it always has) Rock crushes Scissors""")

cpu1 = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
decision = "yes"
ran = random.randint(0, 4)
cpu2 = cpu1[ran]
tie = 0
win = 0
lose = 0

print("Rock Paper Scissors Lizard Spock")
rules = input("Do you want to read the rules? (Yes/No) ").lower()
if rules == "yes":
  dialogue()
while decision == "yes":
  character = input("\nWhich one do you want to be? ").title()
  
  if character != "Rock" and character != "Paper" and character != "Scissors" and character != "Spock" and character != "Lizard":
    print("Stop It Dad ;-;")
    continue

  time.sleep(2)
  replit.clear
  
  if character == "Rock":
    rock()
    if cpu2 == "Rock":
      rock()
      print("You tied :/")
      tie += 1
    if cpu2 == "Paper":
      paper()
      print("You lost :(")
      lose += 1
    if cpu2 == "Scissors":
      scissors()
      print("YOU WON! :)")
      win += 1
    if cpu2 == "Lizard": 
      lizard()
      print("YOU WON! :)")
      win += 1
    if cpu2 == "Spock":
      spock()
      print("You lost :(")
      lose += 1
    
  if character == "Paper":
    paper()
    if cpu2 == "Rock":
      rock()
      print("YOU WON! :)")
      win += 1
    if cpu2 == "Paper":
      paper()
      print("You tied :/")
      tie += 1
    if cpu2 == "Scissors":
      scissors()
      print("You lost :(")
      lose += 1
    if cpu2 == "Lizard":
      lizard()
      print("You lost :(")
      lose += 1
    if cpu2 == "Spock":
      spock()
      print("YOU WON! :)")
      win += 1
      
    
  if character == "Scissors":
    scissors()
    if cpu2 == "Rock":
      rock()
      print("You lost :(")
      lose += 1
    if cpu2 == "Paper":
      paper()
      print("YOU WON! :)")
      win += 1
    if cpu2 == "Scissors":
      scissors()
      print("You tied :/")
      tie += 1
    if cpu2 == "Lizard":
      lizard()
      print("YOU WON! :)")
      win += 1
    if cpu2 == "Spock":
      spock()
      print("You lost :(")
      lose += 1
      
  if character == "Spock":
    spock()
    if cpu2 == "Rock":
      rock()
      print("YOU WON! :)")
      win += 1
    if cpu2 == "Paper":
      paper()
      print("You lost :(")
      lose += 1
    if cpu2 == "Scissors":
      scissors()
      print("YOU WON :)")
      win += 1
    if cpu2 == "Lizard":
      lizard()
      print("You lose :(")
      lose += 1
    if cpu2 == "Spock":
      spock()
      print("You tied :/")
      tie += 1

  if character == "Lizard":
    lizard()
    if cpu2 == "Rock":
      rock()
      print("You lose :(")
      lose += 1
    if cpu2 == "Paper":
      paper()
      print("YOU WON :)")
      win += 1
    if cpu2 == "Scissors":
      scissors()
      print("You lose :(")
      lose += 1
    if cpu2 == "Lizard":
      lizard()
      print("You tied :/")
      tie += 1
    if cpu2 == "Spock":
      spock()
      print("YOU WON :)")
      win += 1

  time.sleep(5)
  replit.clear()

  decision = input("Do you want to play again? (Yes/No) ").lower()

print(f"""
You have tied {tie} time/s
You have won {win} time/s
You have lost {lose} time/s""")
print("Thanks for playing :)")

