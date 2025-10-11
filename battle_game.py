# Import needed libraries
import random

# Greet user
print ("Hello there! You will fight an opponent until one of you die. You will both start with 100 health!")
print ("Good luck!")
print()


# General settings
max_damage = 50
least_damage = 5

# Player settings
user_health = 100
user_damage = 0
user_shield = 60


# Opponent settings
op_damage = random.randint (least_damage, max_damage)
op_shield_health = 60
op_health = 100

# Decide if player starts
player_starts = random.choice([True, False])
if player_starts:
    print("You start first!")
else:
    print("Your opponent starts first!")

round = 1
# Game loop
while True:
    print("#" * 20)
    print(f"# Round {round}")
    print("#" * 20)
    print()
    round += 1

    # Round settings
    dodge_percent = random.randint (0, 20)
    damage = random.randint (least_damage, max_damage)

    # Player decision making
    player_decision = int(input("Do you want to (1) attack or (2) defend? "))
    if player_decision == 1: # attack
        player_weapon = int(input("Do you want to use (1) the hammer, (2) the bow and arrow, or (3) the sword? "))
    elif player_decision == 2: # defend
        if user_shield <= 0:
            player_defense = 2 # can only dodge since shield is broken
            print ("Your shield is broken, you can only try to dodge!")        
        else:
            player_defense = int(input("Do you want to (1) block with your shield, or (2) try to dodge the attack? "))

    # Opponent decision making
    opponent_decision = random.choice([1, 2]) # 1: attack, 2: defend
    print(f"Your opponent's decision: {opponent_decision}")
    if opponent_decision == 1: # attack
        opponent_weapon = random.choice([1, 2, 3]) # 1: hammer, 2: bow and arrow, 3: sword
        print(f"Your opponent's weapon: {opponent_weapon}")
    elif opponent_decision == 2: # defend
        if op_shield_health <= 0: # shield is broken
            opponent_defense = 2 # The opponent can only dodge, as their shield is broken
        else:
            opponent_defense = random.choice([1, 2]) # 1: block with shield, 2: try to dodge attack
        print(f"Your opponent's defense: {opponent_defense}")
        
    print()
    

    # If player goes first
    if player_starts:
        if player_decision == 1: # if player chooses to attack
            if opponent_decision == 2: # if the opponent chooses to defend
                if opponent_defense == 1: # if the opponent blocks the attack with their shield
                    print ("Your opponent has blocked your attack with their shield!")
                    op_shield_health -= damage
                    print (f"Your opponent's shield's durability has gone down to {op_shield_health}")
                elif opponent_defense == 2: # if the opponent tries to dodge attack
                    print("Your opponent has tried to dodge the attack!")
                    if dodge_percent >= 10:
                        print ("Your opponent has dodged your attack!")
                    elif dodge_percent < 10:
                        print("You did damage!")
                        op_health -= damage
                        print (f"Your opponent's health has gone down to {op_health}")    
            elif opponent_decision == 1: # if the opponent chooses to attack
                print ("You both attacked each other! You both received damage!")
                op_health -= damage
                user_health -= damage
                print (f"Your health is now at {user_health}")
                print (f"Your opponent's health is now at {op_health}")
                if op_health <= 0:
                    print ("You have defeated your opponent!")
                    print ("Congrats!")
                    break
                elif user_health <= 0:
                    print ("You have been defeated!")
                    print ("Sorry!")
                    break
        elif player_decision == 2: # player chooses to defend
            if opponent_decision == 1: # opponent chooses to attack
                if player_defense == 1: # player uses shield
                    print ("You blocked your opponent's attack!")
                    user_shield -= damage
                    print (f"You shield's durability has now gone down to {user_shield}")

                    # Check with dad, maybe I should put if the shield durability has gone down to 0?

                elif player_defense == 2: # player tries to dodge opponent attack
                    if dodge_percent >= 10: # if random number is equal to or greater than 10 
                        print ("You were able to dodge the attack!")       
                    elif dodge_percent < 10: # if random number is less than 10
                        print ("You weren't able to dodge the attack!")
                        user_health -= damage
                        print (f"Your health is now at {user_health}")
                    # Check with dad, maybe if the player couldn't dodge the attack and took damage but now health is now at 0 or less.
                    # Maybe add the posibility of health at 0 or less?
            elif opponent_decision == 2: # opponent also defends
                print ("You both defended!")
                print ("No one has taken damage!")
        
    # If opponent goes first
    if player_starts == False:
        if opponent_decision == 1: # the opponent chooses to attack
            if player_decision == 1: # player also chooses to attack
                print ("You both attacked each other!")
                user_health -= damage
                op_health -= damage
                print (f"Your health is now at {user_health}")
                print (f"Your opponent's health is now at {op_health}")
                if user_health <= 0: # health goes down to 0 and player loses
                    print ("Sorry! You've been defeated by your opponent!")
                    break
                elif op_health <= 0: # opponent health goes down to 0 and player wins
                    print ("Hooray! You've defeated your opponent!")
                    print ("Congratulations!")
                    break
            if player_decision == 2: # player chooses to defend
                if player_defense == 1: # chooses to block with shield
                    print ("You blocked your opponent's attack!")
                    user_shield -= damage
                    print (f"Your shield durability has gone down to {user_shield}")
                    
                    # Check with dad, maybe I should put if the shield durability has gone down to 0?
                
                elif player_defense == 2: # player tries to dodge the attack
                    if dodge_percent >= 10: # random number is equal to or greater than 10 
                        print ("You were successful in dodging the attack!")
                    elif dodge_percent < 10:
                        print ("You took damage! You couldn't dodge the attack!")
                        user_health -= damage
                        print (f"Your health is now at {user_health}")
                        

                        # Check with dad, maybe if the player couldn't dodge the attack and took damage but now health is now at 0 or less.
                        # Maybe add the posibility of health at 0 or less?
        
        elif opponent_decision == 2: # opponent defends
            if player_decision == 2: # player defends
                print ("You both defended!")
                print ("No one took damage!")
            elif player_decision == 1: # player chooses to attack
                if opponent_defense == 1: # opponent blocks with shield
                    print ("Your opponent blocked your attack with their shield!")
                    op_shield_health -= damage
                    print (f"Your opponent's shield's durability has gone down to {op_shield_health}")
                elif opponent_defense == 2: # opponent tries to dodge attack
                    if dodge_percent >= 10: # random number is greater than or equal to 10
                        print ("Your opponent has dodged your attack!")
                    elif dodge_percent < 10: # random number is less than 10
                        print ("You did damage, your opponent tried to dodge the attack, but was unsuccessful!")
                        op_health -= damage
                        print (f"Your opponent's health is now at {op_health}")

    # Next round definitions
    # (Does the player's shield have enough health?)
    if user_shield <= 0:
        print ("Your shield has broken and cannot be used again!")


    # (Does the player have enough health?)
    if user_health <= 0:
        print ("Sorry! You've died, your health reached 0!")
        break

    # (Does the player's shield have enough health?)
    if op_shield_health <= 0:
        print ("Your opponent's shield is broken!")

    # (Does the player have enough health?)
    if op_health <= 0:
        print ("You've won! You've defeated your opponent!")
        break


## Game play coverage table
# PA, OA
# PA, OD
# PD, OA
# PD, OD
# OA, PA
# OA, PD
# OD, PA
# OD, PD

# NOT WORKING I NEED SUPPORT FROM THE ONE AND ONLY .... FATHER!!!