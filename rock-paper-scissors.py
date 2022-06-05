import random

print("*** Welcome to Rock, Paper and Scissors Game. ***\n")
def char_full(letter):
    if letter == 'R':
        return 'Rock'
    elif letter == 'P':
        return 'Paper'
    elif letter == 'S':
        return 'Scissors'


choices_ = ['R', 'P', 'S']

is_game_on = True

player_input = input("Select a letter ('R', 'P', 'S'): ")

while is_game_on:

    if player_input not in choices_:
        print("Error. Wrong Choice. Please Try Again\n")
        player_input = input("Select a letter ('R', 'P', 'S'): ")
    else:
        cpu_choice = random.choice(choices_)

        print(f"Player({char_full(player_input)}): CPU({char_full(cpu_choice)})\n")

        # Rock
        if player_input == 'R' and cpu_choice == 'S':
            print("You Win")
            is_game_on = False

        if player_input == 'S' and cpu_choice == 'R':
            print("Computer Wins")
            is_game_on = False

        # Paper
        if player_input == 'P' and cpu_choice == 'R':
            print("You Win")
            is_game_on = False

        if player_input == 'R' and cpu_choice == 'P':
            print("Computer Wins")
            is_game_on = False

        # Scizzors
        if player_input == 'S' and cpu_choice == 'P':
            print("You Win")
            is_game_on = False

        if player_input == 'P' and cpu_choice == 'S':
            print("Computer Wins")
            is_game_on = False

        if player_input == cpu_choice:
            print("Draw. Game will restart\n\n")




