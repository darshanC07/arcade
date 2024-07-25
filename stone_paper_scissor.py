from random import randint
import time

c_choice = 0
user_choice = None

def comp_choice():
    c_choice = randint(1,3)
    return c_choice

def check(c_choice,user_choice):
    if c_choice==1 and user_choice==3:
        print("Computer Won.")
    elif c_choice==1 and user_choice==2:
        print("You Won.")
    elif c_choice==2 and user_choice==3:
        print("You Won.")
    elif c_choice==2 and user_choice==1:
        print("Computer Won.")
    elif c_choice==3 and user_choice==1:
        print("You Won.")
    elif c_choice==3 and user_choice==2:
        print("Computer Won.")

def printing(num):
    match num:
        case 1:
            return "Stone"
        case 2:
            return "Paper"
        case 3:
            return "Scissor"


print("Stone-Paper-Scissor Game")
print("---------------------------------------")
print(" Game Rule \n Stone VS Scissor = Stone Wins \n Stone VS Paper = Paper Wins \n Paper VS Scissor = Scissor Wins")
print("---------------------------------------")
user_name = input("Enter your username : ")
print(f"Welcome {user_name}")
start = int(input("Press 1 to start \tPress 0 to stop : "))

while start==1:
    user_choice = int(input("Press 1 for Stone \nPress 2 for Paper \nPress 3 for Scissor \nInput : "))
    if user_choice==0:
        break
    print("Computer is choosing...")
    time.sleep(2)
    c_choice = comp_choice()
    print(f"Computer chose {printing(c_choice)}")
    print("...........................")
    print(f"Your choice = {printing(user_choice)} and Computer Choice = {printing(c_choice)}")
    check(c_choice,user_choice)


