import sys 
import random

from enum import Enum;

class RPS(Enum):
    ROCK=1
    PAPER=2
    SISSOR=3


print('');
print("------------ Rock - Papaer - Sissor --------------");
print("1 - Rock ");
print("2 - Paper ");
print("3 - Sissor ");

playerChoice= input(" Your choice \n");
player=int(playerChoice);

if player < 1 or player > 3:
    sys.exit("! Invalid Choice \n Choice should be 1 or 2 or 3");

computerChoice=random.choice("123");
computer=int(computerChoice);

print("Your Choice : " + str(RPS(player)).replace("RPS.",""));
print("Bot Choice : " + str(RPS(computer)).replace("RPS.",""));

if player == 1 and computer == 3:
    print("Player Won")
elif player ==2 and computer == 1:
    print("Player Won")
elif player==3 and computer ==3:
    print("Player won")
elif player == computer:
    print("Game Tie")
else:
    print("Python Won")
