import os

def print_dashboard(player_container : list, opponent_container : list) -> None:
    
    # Greet user
    print()
    print ("Hello there! You will fight an opponent until one of you die. You will both start with 100 health!")
    print ("Good luck!")
    print()
    
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
    
    

def main():
    # Import needed libraries
    import random
    
    # General settings
    max_damage = 50
    least_damage = 5
    
    player_container = [
        100, # initial user health
        0,   # initial user damage
        60,  # initial user shield health
        0,   # default user decision
        0,   # default user weapon
        0    # default user defense
    ]
    
    
    opponent_container = [
        100, # initial opponent health
        0,   # initial opponent damage
        60,  # initial opponent shield health
        0,   # default opponent decision
        0,   # default opponent weapon
        0    # default opponent defense
    ]
    
    # Decide if player starts
    player_starts = random.choice([True, False])
    if player_starts:
        print("You start first!")
    else:
        print("Your opponent starts first!")
    
    round = 1
    # Game loop
    while True:
        clear_console()
        print_dashboard(player_container, opponent_container)
        print(f"#                           Round {round:<2}                          #")
        print("# " * 32)
        print()
        round += 1
    
        # Round settings
        dodge_percent = random.randint (0, 20)
        player_container[1] = random.randint (least_damage, max_damage) # player_container[1] is user_damage
        opponent_container [1] = random.randint (least_damage, max_damage)
    
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
        
    
        # If player goes first
        if player_starts:
            # player_container[3] is player_decision
            if player_container [3] == 1: # if player chooses to attack
                if opponent_container [3] == 2: # if the opponent chooses to defend
                     # opponent_container[5] is opponent_defense
                    if opponent_container [5] == 1: # if the opponent blocks the attack with their shield
                        print ("Your opponent has blocked your attack with their shield!")
                       # opponent_container[2] is opponent_shield_health
                        opponent_container [2] -= player_container [1] # player_container[1] is user_damage
                        print (f"Your opponent's shield's durability has gone down to {opponent_container [2]}")
                    elif opponent_container [5] == 2: # if the opponent tries to dodge attack
                        print("Your opponent has tried to dodge the attack!")
                        if dodge_percent >= 10:
                            print ("Your opponent has dodged your attack!")
                        elif dodge_percent < 10:
                            print("You did damage!")
                          # opponent_container[0] is opponent_health
                            opponent_container [0] -= player_container [1]
                            # player_container[1] is user_damage
                            print (f"Your opponent's health has gone down to {opponent_container [0]}")    
                   # opponent_container[3] is opponent_decision
                elif opponent_container [3] == 1: # if the opponent chooses to attack
                    print ("You both attacked each other! You both received damage!")
                  # opponent_container[0] is opponent_health
                    opponent_container [0] -= player_container [1] # player_container[1] is player_damage
                    # player_container[1] is user_damage
                    player_container [0] -= opponent_container [1]
                    # player_container[0] is user_health
                    print (f"Your health is now at {player_container [0]}")
                    print (f"Your opponent's health is now at {opponent_container [0]}")
                    if opponent_container [0] <= 0:
                        print ("You have defeated your opponent!")
                        print ("Congrats!")
                        break
                    elif player_container [0] <= 0:
                        print ("You have been defeated!")
                        print ("Sorry!")
                        break
                    # player_container[0] is user_health
            elif player_container [3] == 2: # player chooses to defend
            # player_container[3] is player_decision
                if opponent_container [3] == 1: # opponent chooses to attack
                    if player_container [5] == 1: # player uses shield
                        # player_container[5] is user_defense
                        print ("You blocked your opponent's attack!")
                        player_container [2] -= opponent_container [1]
                        print (f"You shield's durability has now gone down to {player_container[2]}")
                        # player_container[2] is player_shield_health
    
                    elif player_container [5] == 2: # player tries to dodge opponent attack
                        # player_container[5] is user_defense
                        if dodge_percent >= 10: # if random number is equal to or greater than 10 
                            print ("You were able to dodge the attack!")       
                        elif dodge_percent < 10: # if random number is less than 10
                            print ("You weren't able to dodge the attack!")
                            player_container [0] -= opponent_container [1]
                            print (f"Your health is now at {player_container [0]}")
                            # player_container[0] is player_health
                            
                elif opponent_container [3] == 2: # opponent also defends
                    print ("You both defended!")
                    print ("No one has taken damage!")
            
        # If opponent goes first
        if player_starts == False:
            if opponent_container [3] == 1: # the opponent chooses to attack
                if player_container [3] == 1: # player also chooses to attack
                    print ("You both attacked each other!")
                    # player_container[3] is player_decision
                    player_container [0] -= opponent_container [1]
                    # player_container[0] is player_health
                    opponent_container [0] -= player_container [1]
                    # player_container[1] is user_damage
                    print (f"Your health is now at {player_container [0]}")
                    print (f"Your opponent's health is now at {opponent_container [0]}")
                    if player_container [0] <= 0: # health goes down to 0 and player loses
                        print ("Sorry! You've been defeated by your opponent!")
                        break
                    # player_container[0] is user_health
                    elif opponent_container [0] <= 0: # opponent health goes down to 0 and player wins
                        print ("Hooray! You've defeated your opponent!")
                        print ("Congratulations!")
                        break
                if player_container [3] == 2: # player chooses to defend
                    # player_container[3] is player_decision
                    if player_container [5] == 1: # chooses to block with shield
                        print ("You blocked your opponent's attack!")
                        # player_container[5] is user_defense
                        player_container [2] -= opponent_container [1]
                        print (f"Your shield durability has gone down to {player_container [2]}")
                        # player_container[2] is player_shield_health
                    
                    elif player_container [5] == 2: # player tries to dodge the attack
                        # player_container[5] is user_defense
                        if dodge_percent >= 10: # random number is equal to or greater than 10 
                            print ("You were successful in dodging the attack!")
                        elif dodge_percent < 10:
                            print ("You took damage! You couldn't dodge the attack! Sorry!")
                            player_container [0] -= opponent_container [1]
                            # player_container[0] is player_health
                            print (f"Your health is now at {player_container [0]}")
            
            elif opponent_container [3] == 2: # opponent defends
                if player_container [3] == 2: # player defends
                    # player_container[3] is player_decision
                    print ("You both defended!")
                    print ("No one took damage!")
                elif player_container [3] == 1: # player chooses to attack
                    # player_container[3] is player_decision
                    if opponent_container [5] == 1: # opponent blocks with shield
                        print ("Your opponent blocked your attack with their shield!")
                        opponent_container [2] -= player_container [1]
                        # player_container[1] is user_damage
                        print (f"Your opponent's shield's durability has gone down to {opponent_container [2]}")
                    elif opponent_container [5] == 2: # opponent tries to dodge attack
                        if dodge_percent >= 10: # random number is greater than or equal to 10
                            print ("Your opponent has dodged your attack!")
                        elif dodge_percent < 10: # random number is less than 10
                            print ("You did damage, your opponent tried to dodge the attack, but was unsuccessful!")
                            opponent_container [0] -= player_container [1]
                            # player_container[1] is user_damage
                            print (f"Your opponent's health is now at {opponent_container [0]}")
                            
    
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
