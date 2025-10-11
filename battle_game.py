# Import required libraries
import random # Needed for opponent's shield usage, dodging attacks, and amoutn of damage

# Greetings
print ("Hello there! You will fight an opponent until one of you die. You will both start with 100 health!")
print ("Good luck!")
print()

# General settings
max_damage = 50
least_damage = 5

# User initial settings
user_health = 100
user_damage = 0
user_shield = 60

# Opponent initial settings
op_damage = random.randint (least_damage, max_damage)
op_shield_health = 60
op_health = 100

## To-dos (ARs)
# 1. Change all string-based inputs to int-based inputs (e.g. decision, attack, ...)
# 2. 


# Game loop
while True:
    # Every round starts here

    # Set opponent's shield usage
    op_shield_used = False
    if op_shield_health > 0 and random.choice([True, False]):
         op_shield_health = True
    
    # Set overall dodging and damage and shield
    dodge_percent = random.randint (0, 20)
    damage = random.randint (least_damage, max_damage)
    shield_left = user_shield - op_damage

    decision = int(input("Do you want to (1) attack or (2) defend:"))
    if decision == 1: # "attack"
        attack = int(input("Do you want to use the (1) hammer, (2) the bow and arrow, or (3) the sword: "))
        # If hammer and no shield and no attack from CPU
        if attack == 1 and op_shield_used == False and op_damage == False:
            print (f"You did {damage} damage on your opponent!")
            op_health -= damage
            print(f"Your opponent now has {op_health} health")
        # If hammer and yes shield and no attack from CPU
        elif attack == 1 and op_shield_used == True and op_damage == False:
                print ("Your opponent used his shield!")
                op_shield_health -= damage 
                print (f"Your opponent's shield durability has now gone to {op_shield_health}") 
        # If hammer and yes shield and yes attack from CPU
        elif attack == 1 and op_shield_used == False and op_damage == True:
                print ("Your opponent has attacked you at the same time as you attacked him!")
                op_health -= damage
                user_health -= op_damage
                print (f"Your health has gone down to {user_health} and your opponent's health has gone down to {op_health}")        
        # If bow and arrow and no shield
        elif attack == 2 and op_shield_used == False and op_damage == False:
            print (f"You did {damage} damage on your opponent!")
            op_health -= damage
            print(f"Your opponent now has {op_health} health")
        # If bow and arrow and yes shield
        elif attack == 2 and op_shield_used == True and op_damage == False:
                print ("Your opponent used his shield!")
                op_shield_health -= damage 
                print (f"Your opponent's shield durability has now gone to {op_shield_health}")
        # If bow and arrow and no shield and yes atttack from cpu
        elif attack == 2 and op_shield_used == True and op_damage == True:
                print ("Your opponent has attacked you at the same time as you attacked him!")
                op_health -= damage
                user_health -= op_damage
                print (f"Your health has gone down to {user_health} and your opponent's health has gone down to {op_health}")      
        # If sword and no shield and no attack from cpu
        elif attack == 3 and op_shield_used == False and op_damage == False:
            print (f"You did {damage} damage on your opponent!")
            op_health -= damage
            print(f"Your opponent now has {op_health} health")
        # If sword and yes shield and no attack from cpu
        elif attack == 3 and op_shield_used == True and op_damage == False:
                print ("Your opponent used his shield!")
                print (f"Your opponent's shield durability has now gone to {op_shield_health}")
                op_shield_health -= damage 
        # If sword and yes shield and yes attack from cpu
        elif attack == 3 and op_shield_used == True and op_damage == False:
                print ("Your opponent has attacked you at the same time as you attacked him!")
                op_health -= damage
                user_health -= op_damage
                print (f"Your health has gone down to {user_health} and your opponent's health has gone down to {op_health}")     
                op_shield_health -= damage 
        if op_shield_health - damage <= 0:
                 print ("Your opponent's shield has broken!")
                 if op_shield_used == True:
                      op_health -= damage
                      op_shield_used == False
        else:
             print ("Your opponent's shield still has durability")                     
    
    elif decision == 2:
        defend = input("Do you want to (1) use your shield or (2) try to dodge (not 100% percent successful)")
        op_damage = False
        if op_damage and random.choice([True, False]):
            op_damage = True
        if defend == 1 and op_damage == True:
            print (f"Your shield durability has gone from {user_shield} to {shield_left}")
            if shield_left <= 0:
                print ("Your shield broke!")
        elif defend == 1 and op_damage == False:
             print ("You didn't take damage.. the CPU has not attacked you")
        elif defend == 2 and op_damage == True:
            print ("A random number has been picked, it needs to be above 10 to win")
            print (f"The number was {dodge_percent}")
            if dodge_percent > 10:
                print ("You were successful in dodging the attack!")
            elif dodge_percent < 10:
                print (f"You weren't able to dodge the attack! You took {damage} damage!")
                user_damage -= op_damage
                print (f"You now have {user_damage} left of health!")
                print()
        elif defend == 2 and op_damage == False:
            print ("You have not taken damage... the CPU has not attacked you")
    
    
    if user_health <= 0:
        print ("You have died... your opponent has defeated you!")
        break
    if op_health <= 0:
             print ("Congrats! You have defeated your opponent! Your opponent's shield broke, and you hit the finishing blow.")
             break
    
        

    