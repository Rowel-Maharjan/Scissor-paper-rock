import random
import sys

wins = 0
lose = 0
ties = 0

def win(playerMove,computerMove):
  if(playerMove == "r" and computerMove == "s") or (playerMove == "p" and computerMove == "r") or (playerMove == "s" and computerMove == "p"):
    return True
  
while(True):
  print("Wins:",wins,"  Lose:",lose,"  Ties:",ties)

  computerMove = random.choice("rps")
  playerMove = input("Enter your move: (r)ock, (p)aper, (s)cissior or (q)uit\n")
  if playerMove == "q":
    break
  
  if playerMove == computerMove:
    print(computerMove)
    print("It is a tie")
    ties = ties+1

  else:
    if win(playerMove,computerMove):
      print(computerMove)
      print("You won")
      wins = wins + 1
    else:
      print(computerMove)
      print("You lose")
      lose = lose + 1

print("Final score is as follow:")
print("Wins:",wins)
print("Lose:",lose)
print("Ties:",ties)
  
  
