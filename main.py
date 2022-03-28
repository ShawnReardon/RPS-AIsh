from enums import Moves, Results
from random import choice
from ai import AI
 
# creating enumerations using class

com = AI()
moves = {"rock":1, "paper":2, "scissors":3}
p1_wins = 0
p2_wins = 0
resultsDic = {("rock", "scissors")}
#winCon = ((Moves(0),Moves(0), Results(3)))
exit = ''
def play():
  global exit
  debug = False
  exit = ''
  while exit not in range(0,4):
    exit = int(input("Type \n 1 for rock \n 2 for paper \n 3 for scissors \n > "))
  assert exit in range(0,4), "Not in range 1-3"
  p = exit
  c = Moves(com.checkTendencies()).name
  com.storeMove(Moves(p).name)
  if debug: 
    print(com.oppMoves)
  return(Moves(p).name,c)

def determineResults(results):
  if result[0] == 'rock' and result[1] == 'paper':
    return Results(2).name
  elif result[0] == 'rock' and result[1] == 'scissors':
    return Results(1).name
  elif result[0] == 'paper' and result[1] == 'rock':
    return Results(1).name
  elif result[0] == 'paper' and result[1] == 'scissors':
    return Results(2).name
  elif result[0] == 'scissors' and result[1] == 'paper':
    return Results(1).name
  elif result[0] == 'scissors' and result[1] == 'rock':
    return Results(2).name
  else:
    return Results(3).name
while exit != 0:
  result = play()
  print()
  print('P1: ', result[0])
  print('P2: ', result[1])
  #print()
  print()
  verdict = determineResults(result)
  print()
  if verdict == 'P1_WIN':
    p1_wins += 1
    com.lost()
  elif verdict == 'P2_WIN':
    p2_wins += 1
    com.won()
  print(p1_wins, p2_wins)
  
  
  