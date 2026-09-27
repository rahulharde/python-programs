import random

choices=["rock","paper","scissor"]
user_score=0
computer_score=0

rounds=int(input("Enter Number of rounds:"))

for i in range(rounds):
    user_choice=input("Enter Your value:(rock,paper,scissor):")
    computer_choice=random.choice(choices)
    
    print("You entered:",user_choice)
    print("Computer entered:",computer_choice)

    if user_choice==computer_choice:
        print("Round draw")
        
    elif (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissor" and computer_choice=="paper") or (user_choice=="rock" and computer_choice=="scissor"):
        user_score=user_score+1
        print("This round you win")
        
    else:
        computer_score=computer_score+1
        print("This round computer win")

if computer_score>user_score:
    print("Computer win")
else:
    print("You win")

print("Your score:",user_score)
print("Computer score:",computer_score)
