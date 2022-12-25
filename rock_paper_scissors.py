import random

while(True):
    user_choice = input("Enter a choice (rock, paper, or scissors) or if you are done playing, then type 'done with playing': ")
    comp_choice = random.choice(["rock", "paper", "scissors"])


    if(user_choice == "rock" and comp_choice == "scissors"):
        print("user wins")
    elif(user_choice == "rock" and comp_choice == "paper") :
        print("computer wins")

    elif(user_choice == "rock" and comp_choice == "rock") :
        print("it is a tie, try again")

    elif(user_choice == "paper" and comp_choice == "scissors") :
        print("computer wins")

    elif(user_choice == "paper" and comp_choice == "paper") :
        print("it is a tie, try again")

    elif(user_choice == "paper" and comp_choice == "rock") :
        print("user wins")

    elif(user_choice == "scissors" and comp_choice == "scissors") :
        print("it is a tie, try again")

    elif(user_choice == "scissors" and comp_choice == "paper") :
        print("user wins")

    elif(user_choice == "scissors" and comp_choice == "rock") :
        print("computer wins")
    elif(user_choice == "done with playing"):
        break
    
    print(f"The user's choice is: {user_choice}")
    print(f"The computer's choice is: {comp_choice}")
