from enums import Moves, Results
from random import choice
from ai import AI
 
# creating enumerations using class

com = AI()
moves = {"rock":1, "paper":2, "scissors":3}

resultsDic = {("rock", "scissors")}
#winCon = ((Moves(0),Moves(0), Results(3)))
exit = ''
def play():
  global exit
  p = int(input("Type \n 1 for rock \n 2 for paper \n 3 for scissors \n >"))
  exit = p
  c = Moves(com.checkTendencies()).name
  com.storeMove(Moves(p).name)
  print(com.oppMoves)
  return(Moves(p).name,c)

while exit != 0:
  result = play()
  print(result)
  if result[0] == 'rock' and result[1] == 'paper':
    print(Results(2).name)
  elif result[0] == 'rock' and result[1] == 'scissors':
    print(Results(1).name)
  elif result[0] == 'paper' and result[1] == 'rock':
    print(Results(1).name)
  elif result[0] == 'paper' and result[1] == 'scissors':
    print(Results(2).name)
  elif result[0] == 'scissors' and result[1] == 'paper':
    print(Results(1).name)
  elif result[0] == 'scissors' and result[1] == 'rock':
    print(Results(2).name)
  else:
    print(Results(3).name)
  
  