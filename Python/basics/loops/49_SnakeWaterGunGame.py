# SNAKE, WATER, GUN GAME

     
import random
play=True
while play:
    u=input("Enter your choice: ").upper()
    if u in ["SNAKE","WATER","GUN"]:
        c=random.choice(["SNAKE","WATER","GUN"])
        print("The COMPUTER CHOSE: ",c)

        if c=="SNAKE" and u=="WATER":
            print("You lost. The Computer won.")
    
        elif c=="SNAKE" and u=="GUN":
            print("You won. Congratulations!")
    
        elif c=="WATER" and u=="SNAKE":
            print("You won. Congratulations!")
    
        elif c=="WATER" and u=="GUN":
            print("You lost. The Computer won.")
    
        elif c=="GUN" and u=="WATER":
            print("You won. Congratulations!")
    
        elif c=="GUN" and u=="SNAKE":
            print("You lost. The Computer won.")
    
        else:
                print("Draw")
    
        ch=input("Do you want to play again? [yes/no] : ")
    
        if (ch.upper()=="NO"):
            play=False
            print("Thanks for playing.")
    else:
        print("Invalid Input.")