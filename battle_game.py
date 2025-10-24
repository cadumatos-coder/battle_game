# Import needed libraries
import random
import os

def print_dashboard(player_container : list, opponent_container : list, player_starts) -> None:
    # Greet user
    print()
    print ("Hello there! You will fight an opponent until one of you die. You will both start with 100 health!")
    print ("Good luck!")
    print()

    if player_starts:
        print("You start first!")
    else:
        print("Your opponent starts first!")
    
    # Print Dashboard
    print(f"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                               #    _ _                      #
#   O                           #   |o o|                     #
#  /|\\     health: {player_container[0]:>3}          #   (|.|)      health: {opponent_container[0]:>3}    #
#   |      shield: {player_container[2]:>3}          #  / | | \\     shield: {opponent_container[2]:>3}    #
#  / \\                          #    /`\\                      #
#                               #   (___)                     #
#                               #                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #""")

def clear_console():
        # For Windows
        if os.name == 'nt': 
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')

def getIntInput(input_msg : str, valid_values : list) -> int:
    valid = False
    while not valid:
        usr_input = input(f"{input_msg}(valid entries: {valid_values}) ")
        if not usr_input:
            print("Your input was empty. Try again...")
            continue
        if not usr_input.isnumeric():
            print("Your input needs to be a number. Try again...")
            continue
        usr_input_int = int(usr_input)
        if usr_input_int not in valid_values:
            print("Your input is not valid. Try again...")
            continue
        valid = True
    return usr_input_int
    
def player_decision_making(player_container):
    # Player decision making
    # player_container[3] is player_decision
    player_container[3] = getIntInput("Do you want to (1) attack or (2) defend? ",[1,2])
    if player_container[3] == 1: # attack
        # player_container[4] is player_weapon
        player_container[4] = getIntInput("Do you want to use (1) the hammer, (2) the bow and arrow, or (3) the sword? ",[1,2,3])
    elif player_container[3] == 2: # defend
        if player_container[2] <= 0: # player_container[2] is player_shield_health
            # player_container[5] is player_defense
            player_container[5] = 2 # can only dodge since shield is broken
            print ("Your shield is broken, you can only try to dodge!")        
        else:
            player_container[5] = getIntInput("Do you want to (1) block with your shield, or (2) try to dodge the attack? ",[1,2])
    
def opponent_decision_making(opponent_container):
    # Opponent decision making
    opponent_container [3] = random.choice([1, 2]) # 1: attack, 2: defend
    print(f"Your opponent's decision: {opponent_container [3]}") # opponent_container[3] is opponent_decision
    if opponent_container [3] == 1: # attack
        # opponent_container[4] is opponent_weapon
        opponent_container [4] = random.choice([1, 2, 3]) # 1: hammer, 2: bow and arrow, 3: sword
        print(f"Your opponent's weapon: {opponent_container [4]}")
        # opponent_container[3] is opponent_decision
    elif opponent_container [3] == 2: # defend
        # opponent_container[2] is opponent_shield_health
        if opponent_container[2] <= 0: # shield is broken
            # opponent_container[5] is opponent_defense
            opponent_container[5] = 2 # The opponent can only dodge, as their shield is broken
        else:
            opponent_container [5] = random.choice([1, 2]) # 1: block with shield, 2: try to dodge attack
        print(f"Your opponent's defense: {opponent_container [5]}") 
    print()

def player1_attacks_player2_defends(attacking_player, defending_player, dodge_percent):
    # opponent_container[5] is opponent_defense
    if defending_player[5] == 1: # if the opponent blocks the attack with their shield
        print (f"{defending_player[6]} blocked {attacking_player[6]}'s attack with their shield!")
        # opponent_container[2] is opponent_shield_health
        defending_player[2] -= attacking_player[1] # player_container[1] is user_damage
        print (f"{defending_player[6]}'s shield's durability has gone down to {defending_player[2]}")
    elif defending_player[5] == 2: # if the opponent tries to dodge attack
        print(f"{defending_player[6]} has tried to dodge {attacking_player[6]}'s attack!")
        if dodge_percent >= 10:
            print (f"{defending_player[6]} has dodged {attacking_player[6]}'s attack!")
        elif dodge_percent < 10:
            print(f"{attacking_player[6]} did damage!")
            # opponent_container[0] is opponent_health
            defending_player[0] -= attacking_player[1]
            # player_container[1] is user_damage
            print (f"{defending_player[6]}'s health has gone down to {defending_player[0]}")


def player1_attacks_player2_attacks(starting_player, player2_cont):
    should_break = False
    print ("You both attacked each other! You both received damage!")
    # player2_cont opponent_health
    player2_cont [0] -= starting_player [1] # player1_cont[1] is player_damage
    # player1_cont[0] is user_health
    starting_player [0] -= player2_cont [1] # player2_cont[1] is opponent damage
    print (f"{starting_player[6]}'s health is now at {starting_player [0]}")
    print (f"{player2_cont[6]}'s health is now at {player2_cont [0]}")
    if player2_cont [0] <= 0:
        print (f"{starting_player[6]} has defeated {player2_cont[6]}!")
        should_break = True
    elif starting_player [0] <= 0:
        print (f"{player2_cont[6]} has defeated {starting_player[6]}!")
        should_break = True
    # player1_cont[1] is user_health
    return should_break
     

def main():
    # General settings
    max_damage = 50
    least_damage = 5
    
    player_container = [
        100, # initial user health
        0,   # initial user damage
        60,  # initial user shield health
        0,   # default user decision
        0,   # default user weapon
        0,   # default user defense
        "Player"
    ]
    
    opponent_container = [
        100, # initial opponent health
        0,   # initial opponent damage
        60,  # initial opponent shield health
        0,   # default opponent decision
        0,   # default opponent weapon
        0,   # default opponent defense
        "CPU"
    ]
    
    # Decide if player starts
    player_starts = random.choice([True, False])
    
    round = 1
    # Game loop
    while True:
        clear_console()
        print_dashboard(player_container, opponent_container, player_starts)
        print(f"#                           Round {round:<2}                          #")
        print("# " * 32)
        print()
        round += 1
    
        # Round settings
        dodge_percent = random.randint (0, 20)
        player_container[1] = random.randint (least_damage, max_damage) # player_container[1] is user_damage
        opponent_container [1] = random.randint (least_damage, max_damage)
    
        # Decision Making
        player_decision_making(player_container)
        opponent_decision_making(opponent_container)

        # Play out
        # If player goes first
        if player_starts:
            # player_container[3] is player_decision
            if player_container [3] == 1: # if player chooses to attack
                if opponent_container [3] == 2: # if the opponent chooses to defend
                    player1_attacks_player2_defends(attacking_player=player_container, defending_player=opponent_container, dodge_percent=dodge_percent)
                   # opponent_container[3] is opponent_decision
                elif opponent_container [3] == 1: # if the opponent chooses to attack
                    should_break = player1_attacks_player2_attacks(player_container, opponent_container)
                    if should_break:
                        break
            elif player_container [3] == 2: # player chooses to defend
            # player_container[3] is player_decision
                if opponent_container [3] == 1: # opponent chooses to attack
                    player1_attacks_player2_defends(attacking_player=opponent_container, defending_player=player_container, dodge_percent=dodge_percent)
                            
                elif opponent_container [3] == 2: # opponent also defends
                    print ("You both defended!")
                    print ("No one has taken damage!")
            
        # If opponent goes first
        else:
            if opponent_container [3] == 1: # the opponent chooses to attack
                if player_container [3] == 2: # player chooses to defend
                    player1_attacks_player2_defends(attacking_player=opponent_container, defending_player=player_container, dodge_percent=dodge_percent)
                elif player_container [3] == 1: # player also chooses to attack
                    should_break = player1_attacks_player2_attacks(opponent_container, player_container)
                    if should_break:
                        break
            
            elif opponent_container [3] == 2: # opponent defends
                if player_container [3] == 1: # player chooses to attack
                    player1_attacks_player2_defends(attacking_player=player_container, defending_player=opponent_container, dodge_percent=dodge_percent)
                elif player_container [3] == 2: # player defends
                    # player_container[3] is player_decision
                    print ("You both defended!")
                    print ("No one took damage!")
                            
    
        # Next round definitions
        # (Does the player's shield have enough health?)
        if player_container [2] <= 0:
            # player_container[2] is player_shield_health
            print ("Your shield has broken and cannot be used again!")
    
        # (Does the player have enough health?)
        if player_container [0] <= 0:
            # player_container[0] is user_health
            print ("Sorry! You've died, your health reached 0!")
            break
    
        # (Does the player's shield have enough health?)
        if opponent_container [2] <= 0:
            print ("Your opponent's shield is broken!")
    
        # (Does the player have enough health?)
        if opponent_container [0] <= 0:
            print ("You've won! You've defeated your opponent!")
            break

        input("Press enter to continue...")

if __name__ == "__main__":
    main()
