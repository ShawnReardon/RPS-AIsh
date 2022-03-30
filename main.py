from enums import Moves, Results
from random import choice, randint
from ai import AI
from time import sleep
 
# creating enumerations using class

com = AI('ai_1')
com2 = AI('ai_2')
moves = {"rock":1, "paper":2, "scissors":3}
p1_wins = 0
p2_wins = 0
resultsDic = {("rock", "scissors")}
#winCon = ((Moves(0),Moves(0), Results(3)))
exit = ''
def play(isPlayer):
  playerVsCom = isPlayer
  global exit
  debug = False
  exit = ''
  if playerVsCom:
    while exit not in range(0,4):
      print('Suggested Move: ', com2.nextMove)
      exit = int(input("Type \n 1 for rock \n 2 for paper \n 3 for scissors \n > "))
    assert exit in range(0,4), "Not in range 1-3"
    p = exit
    c = Moves(com.checkTendencies()).name
    com2.checkTendencies()
    com.storeMove(Moves(p).name)
    com2.storeMove(c)
    
   
    if debug: 
      print(com.oppMoves)
    return(Moves(p).name,c)
  else:
    c = Moves(com.checkTendencies()).name
    c2 = Moves(com2.checkTendencies()).name
    com.storeMove(c2)
    com2.storeMove(c)
    if debug: 
      print(com.oppMoves)
    return(c2,c)
  

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
  result = play(True)
  print()
  print('P1: ', result[0])
  print('P2: ', result[1])
  #print()
  print()
  verdict = determineResults(result)
  print(verdict)
  print()
  if verdict == 'P1_WIN':
    p1_wins += 1
    com.lost()
    com2.won()
  elif verdict == 'P2_WIN':
    p2_wins += 1
    com.won()
    com2.lost()
  else:
    com.draw()
    com2.draw()
  print(p1_wins, p2_wins)
  sleep(.5)
  print('------------------------------')
  
  
  