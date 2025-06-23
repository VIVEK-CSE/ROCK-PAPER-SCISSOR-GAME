
#ROCK PAPER SCISSOR GAME

import random

ans = [["DRAW","YOU WON","YOU LOSE"],["YOU LOSE","DRAW","YOU WON"],["YOU WON","YOU LOSE","DRAW"]]
opt = ["ROCK","PAPER","SCISSOR"]

def game():
    print("FOR ROCK -> PRESS 0\nFOR PAPER -> PRESS 1\nFOR SCISSOR -> PRESS 2")
    user = int(input("ENTER YOUR CHOICE: "))

    if(user<0 or user>2):
        print("!!!WRONG INPUT!!!")

    comp = random.randint(0,2)
    print("YOU CHOOSE :",opt[user])
    print("COMPUTER CHOOSE:",opt[comp])
    print(ans[comp][user])
    
    print("\nIF YOU WANT TO PLAY AGAIN PRESS -> 1 OTHERWISE PRESS -> 0 TO EXIT.")
    temp=int(input("PRESS 0 OR 1 : "))
    if(temp==1):
        game()
    else:
        print("THANK YOU FOR PLAYING THE GAME :)")


game()    
