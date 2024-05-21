import random
import time
from utils import choose_town, get_stormhollow_intro, get_eldoria_intro, stormbringer_description
from items import heartmend_elixir
from player import get_player_attack_choice, stormbringer_attacks, player_attacks
from enemy import get_ghost_attack


def main():
    # This function prompts the user to choose a town and prints the introduction message for the chosen town.
    # It also prompts the user to enter their name and prints a welcome message with the chosen name.
    global name
    town_choice = choose_town()   

    if town_choice == 1:
        print(get_stormhollow_intro())
        time.sleep(1)
        print("Elara:")
        name = get_player_name()               
        print("\nHello " + str(name) + "! Welcome to the town of " + "Stormhollow" + "!\n")
        time.sleep(1)

    elif town_choice == 2:
        print(get_eldoria_intro())
        time.sleep(1)
        print("Lyra: ")
        name = get_player_name()
        print("\nHello " + str(name) + "! Welcome to the town of " + "Eldoria" + "!\n")
        time.sleep(1)

def get_player_name():
    name = input("What is your name adventurer? \n")
    return name

if __name__ == "__main__":
    main()

print("First, let's prepare you for battle. You're going to need a weapon to protect yourself on this adventure.\n")
time.sleep(2)
print("**Acquired Stormbringer's Wrath!**\n")
time.sleep(2)
print(stormbringer_description())
print(stormbringer_attacks())
time.sleep(3)

print("Let's test your skills in combat, " + name + "! \n")
time.sleep(2)
print("**A ghostly figure has appeared from the shadows!**\n")
time.sleep(2)
print("Ghost:\nYour light flickers, mortal, as darkness claims its prize. Come, embrace the chill of eternity, for in my grasp, your soul shall find its rest.\n")
time.sleep(2.5)

player_hp = 100
ghost_hp = 100

damage = 25    
ghost_damage = 0
actual_ghost_damage = ghost_damage

player_attack_choice = get_player_attack_choice(name, player_hp)
ghost_attack_choice = get_ghost_attack()


#Flag to indicate if tempest shield (attack 2) is used (reduces incoming damage by 25% for next turn)
tempest_shield_active = False 
#Flag to indicate if stormcall (attack 3) is used (increases damage by 50% for next turn)
stormcall_active = False 


enemy_hp = ghost_hp

while ghost_hp > 0 and player_hp > 0:
    attack_choice = get_player_attack_choice(name, player_hp)
    damage, description = player_attacks[attack_choice]

    if attack_choice == 1:
        actual_damage = damage
        if stormcall_active:
            actual_damage *= 1.5
            stormcall_active = False
        print(f"You unleash a powerful strike, calling down a bolt of lightning from the sky that strikes the ghost with a thunderous crash. The ghost has taken {actual_damage} damage!\n")
        ghost_hp -= actual_damage

    elif attack_choice == 2:
        tempest_shield_active = True
        print("You have summoned a defensive aura of wind and lightning, reducing incoming damage by 25%!\n")

    elif attack_choice == 3:
        stormcall_active = True
        print("You have summoned a vicious storm, increasing damage significantly for the next turn!\n")

    if ghost_hp > 0:
        attack_name, ghost_damage, attack_message = get_ghost_attack()        
        if tempest_shield_active:
            ghost_damage *= 0.75
            tempest_shield_active = False
        player_hp -= ghost_damage

        print(attack_message.format(ghost_hp, ghost_damage))
        
    time.sleep(1)

if ghost_hp <= 0:
    ghost_defeated = heartmend_elixir(name, player_hp)

print("Lyra:\n Great work " + name + "! As you continue on this journey, the enemies you face will become more challenging. You are going to need some protective armor.\n ")
print("**Acquired Phoenix Gaurd Plate!**")

# create new (stronger) opponent and increase player hp because of armor. maybe add a way to break armor and repair it?