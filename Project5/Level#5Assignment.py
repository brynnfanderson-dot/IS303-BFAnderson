import random

# Welcome the user to the game
print("Welcome to Rock, Paper, Scissors!")
#starting variables
rounds_play_for = 0
game_counter = 0
player_wins = 0
computer_wins = 0
approved_list = ["rock", "paper", "scissors"]

#build get_player_choice
def get_player_choice():
#ask the user for their choice #convert reponse to lower case
    player_choice = str(input("Enter rock, paper, or scissors: ")).lower()
#ensure users choice is valid
    while player_choice not in approved_list:
        print(f"Sorry {player_choice} is not a valid choice. Please try again")
        player_choice = str(input("Enter rock, paper, or scissors: ")).lower()
#return result
    return player_choice

#build get_comp_choice
def get_comp_choice():
    comp_choice = random.choice(approved_list)
    return comp_choice


#build determine_winner
def determine_winner(player_choice, comp_choice):
    #tie
    if player_choice == comp_choice:
        return "tie"
#paper beats rock()
    elif player_choice == "paper" and comp_choice == "rock":
        return "win"
#rock beats scissors
    elif player_choice == "rock" and comp_choice == "scissors":
        return "win"
#scissors beats paper
    elif player_choice == "scissors" and comp_choice == "paper":
        return "win"
    else:
        return "loss"
#return result - win, loss, tie



#ask how many times they would like to play
rounds_play_for = int(input("How many rounds would you like to play?: "))
#ensure the number is valid
while rounds_play_for <= 0 or rounds_play_for % 2 == 0:
    print("Please try again, the number must be a positive, odd number.")
    rounds_play_for = int(input("How many rounds would you like to play?: "))

while game_counter < rounds_play_for:
    player_choice = get_player_choice()
    comp_choice = get_comp_choice()

    print(f"The computer chose {comp_choice}.")

    result = determine_winner(player_choice, comp_choice)
#increment game counter
    if result == "win":
        print("You won!")
        player_wins += 1
        game_counter += 1

    elif result == "loss":
        print("You lost!")
        computer_wins += 1
        game_counter += 1

    else:
        print("Tie! Play again.")
#present final score
#decorative line
print("\n*" + "*" * 50)
print(f"Scores -- You: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You Win!")
elif computer_wins > player_wins:
    print("Computer Wins!")
#print "thanks for playing"
print("Thanks for playing!")