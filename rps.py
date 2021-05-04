import random

print("Choose hammer, net, or katana")

player_wins = 0
computer_wins = 0

while (computer_wins < 3 or player_wins < 3):
    rpk_input = input("Enter your weapon: ")
    rpk = ["hammer", "net", "katana"]
    computer_action = random.choice(rpk)
    print("----- ROUND START -----")
    print(f"You chose {rpk_input}, computer chose {computer_action}")
    if rpk_input == computer_action:
        print(f"Both players selected {rpk_input}. It's a tie!")
    elif rpk_input == "hammer":
        if computer_action == "katana":
            print("hammer shatters katana! You win!")
            player_wins += 1
        else:
            print("net covers hammer! You lose.")
            computer_wins += 1
    elif rpk_input == "net":
        if computer_action == "hammer":
            print("net covers hammer! You win!")
            player_wins += 1
        else:
            print("katana slices net! You lose.")
            computer_wins += 1
    elif rpk_input == "katana":
        if computer_action == "net":
            print("katana slices net! You win!")
            player_wins += 1
        else:
            print("hammer shatters katana! You lose.")
            computer_wins += 1
    else:
        print("Invalid choice. Please enter hammer, net, or katana!")
    
    print(f"Your score: {player_wins} Computer score: {computer_wins}")
    if player_wins == 3:
        print("WINNER WINNER CHICKEN DINNER")
        break
    elif computer_wins == 3:
        print("Terrible, just terrible")
        break



# random number guesser
# import random

# tries = 3

# while tries > 0:
#     rand_num = random.randint(0, 10)
#     guess = int(input("Guess a number between 0 and 10!: "))
#     if guess == rand_num:
#         print("You win! now leave")
#         break
#     else:
#         print("You are wrong")
#         print(f"The number was {rand_num}")
#         tries -= 1

# if tries == 0:
#     print("You lost the game")
# else: print("Winner winner chicken dinner!")