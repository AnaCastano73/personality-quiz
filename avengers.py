"""
Avengers personality game
adding to test if push to git
"""

from random import choice

def main():
  # VARIABLES 
  ans = ["","","","",""]

  name = input("Please enter your name: ")
  print()
  printWelcome(name)

  # QUESTION ONE
  print("What motivates you most?\nA. Morals\nB. Protecting Others")
  print("C. Being a leader\nD. Peacekeeping")
  ans[0] = input("Choice: ")
  print()

  # QUESTION TWO
  print("You have the chance to wield one Infinity stone. Which do you choose?")
  print("A. The Power Stone\nB. The Reality Stone\nC. The Mind Stone")
  print("D: The Time Stone")
  ans[1] = input("Choice: ")

  # QUESTION THREE
  print("\nWhat is your biggest strength?")
  print("A. Strategy\nB. Bravery\nC. Ambition\nD. Intelligence")
  ans[2] = input("Choice: ")

  # QUESTION FOUR
  print("\nWhat is your biggest weakness?")
  print("A. Insecure\nB. Stubborn\nC. Narrow-Minded\nD. Overreact")
  ans[3] = input("Choice: ")

  # QUESTION FIVE
  print("\nWho do you check on first after the Snap?")
  print("A. Parent(s)\nB. Partner\nC. Best Friend\nD. Other")
  ans[4] = input("Choice: ")

  avenger = findCharacter(ans)
  print("\n%s, you are %s!\n"%(name, avenger))

# FUNCTIONS #
"""
Purpose: print out welcome statement
Params: name -- name of user
Returns: n/a
"""
def printWelcome(name):
  print("Hi %s and welcome to the Avenger Personality Quiz Game!\n"%(name))

def findCharacter(ans):
  ave = ["Iron Man", "Thor", "Captain Marvel", "Black Widow", "Cap"]
  avenger = choice(ave)

  return avenger

main()
