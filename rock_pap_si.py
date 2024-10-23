import random

print("""Choose from :
R --> Rock
P --> Paper
S --> Scissor

Rock beats Scissor, Scissor beats Paper, Paper beats Rock""")

while True:
    user_choice = input("Enter Your Choice : ")
    user_choice = user_choice.capitalize()

    if(user_choice == "R"):
        print("You chose Rock")
    elif(user_choice == "P"):
        print("You chose paper")
    elif(user_choice == "S"):
        print("You chose Scissor")
    else:
        print("Restart and enter a valid choice")
        break

    x = random.randint(1,3)

    if(x == 1):
        comp_choice = "Rock"
        print(f"Computer chose {comp_choice} ")
    elif(x == 2):
        comp_choice = "Paper"
        print(f"Computer chose {comp_choice} ")
    else:
        comp_choice = "Scissor"
        print(f"Computer chose {comp_choice} ")

    print("Computing ...")

    if(user_choice == "R" and comp_choice == "Rock"):
        print("It was a draw")
    elif(user_choice == "R" and comp_choice == "Paper"):
        print("Computer wins !")
    elif(user_choice == "R" and comp_choice == "Scissor"):
        print("You Win")
    elif(user_choice == "P" and comp_choice == "Rock"):
        print("You win !")
    elif(user_choice == "P" and comp_choice == "Paper"):
        print("It was a draw")
    elif(user_choice == "P" and comp_choice == "Scissor"):
        print("Computer wins !")
    elif(user_choice == "S" and comp_choice == "Rock"):
        print("Computer wins !")
    elif(user_choice == "S" and comp_choice == "Paper"):
        print("You win !")
    elif(user_choice == "S" and comp_choice == "Scissor"):
        print("It was a draw")

    a = input("Do you want to continue ? Reply with a yes or no. \n")
    a = a.capitalize()
    if(a == "No"):
        break

print("Game Exited")







