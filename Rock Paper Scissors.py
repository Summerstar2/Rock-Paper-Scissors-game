import random
def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
Computer=["Rock","Paper","Scissors"]
print ("Welcome to the Rock Paper Scissors game!")
print ("In this program you can play against the computer as many times as you like with different choice everytime!")
Play=str(input("Do you wish to play? (Yes/No) "))
if Play=="No":
    quit()
else:
    while True:
        Choice=str(input("Enter your choice (Rock/Paper/Scissors) - "))    
        Computer_choice=random.choice(Computer)
        if Choice=="Rock":
            if Computer_choice=="Rock":
                print ("Both players chose Rock!\nIt's a draw!")
            if Computer_choice=="Paper":
                print ("The computer chose Paper and Paper covers Rock!\nYou lost.")
            if Computer_choice=="Scissors":
                print ("The computer chose Scissors and Rock breaks Scissors!\nYou won!")
        if Choice=="Paper":
            if Computer_choice=="Rock":
                print ("The computer chose Rock and Paper covers Rock!\nYou won!")
            if Computer_choice=="Paper":
                print ("Both players chose Paper!\nIt's a draw!")
            if Computer_choice=="Scissors":
                print ("The computer chose Scissors and Scissors cut Paper!\nYou lost.")
        if Choice=="Scissors":
            if Computer_choice=="Rock":
                print ("The computer chose Rock Rock breaks Scissors!\nYou lost.")
            if Computer_choice=="Paper":
                print ("The computer chose Paper and Scissors cut Paper!\nYou won!")
            if Computer_choice=="Scissors":
                print ("Both players chose Scissors!\n It's a draw!")
        if not Continue():
            break
