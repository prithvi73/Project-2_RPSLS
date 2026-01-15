import random

print("Enter your choice.")
print("1.Rock 2.Paper 3.Scissors 4.Lizard 5.Spock")

choices = ["rock" , "paper" , "scissors" , "lizard" , "spock"]

game_rules = {
    "rock": {"scissors" : "crushes" , "lizard" : "crushes"} ,
    "paper" : {"rock" : "cover" , "spock" : "disproves"},
    "scissors" : {"paper" : "cuts" , "lizard" : "decapitates"},
    "lizard" : {"paper" : "eats" , "spock" : "poisons"},
    "spock": {"rock" : "vaporises" , "scissors" : "smashes"} 

}

try:
    user_num = int(input("enter number (1-5) :  "))
    user_num-=1
    user_choice = choices[user_num]
except(ValueError , IndexError):
    print("Invalid Choice! Please pick 1-5")
    exit()

comp_choice = random.choice(choices)

print(f"\nYou picked {user_choice.upper()} , Computer picked {comp_choice.upper()}")
print("-"*40)

if (user_choice == comp_choice):
    print("Its a DRAW")

elif comp_choice in game_rules[user_choice]:
    verb = game_rules[user_choice][comp_choice]
    print(f"You WIN as {user_choice.upper()} {verb.upper()} {comp_choice.upper()}!")

else:
    verb = game_rules[comp_choice][user_choice]
    print(f"You LOSE as {comp_choice.upper()} {verb.upper()} {user_choice.upper()}!")