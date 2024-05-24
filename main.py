import time
from utils import choose_town, get_stormhollow_intro, get_eldoria_intro, stormbringer_description
from items import heartmend_elixir, restoration_potion
from player import first_battle_attack_choice, next_battle_attack_choice, stormbringer_attacks, player_attacks
from enemy import get_ghost_attack, get_enigma_attack, get_warden_attack


def main():
    # This function prompts the user to choose a town and prints the introduction message for the chosen town.
    # It also prompts the user to enter their name and prints a welcome message with the chosen name.
    global name
    town_choice = choose_town()   

    if town_choice == 1:
        print(get_stormhollow_intro())
        time.sleep(2)
        print("Elara:")
        name = get_player_name()               
        print("\nHello " + str(name) + "! Welcome to the town of " + "Stormhollow" + "!\n")
        time.sleep(1)

    elif town_choice == 2:
        print(get_eldoria_intro())
        time.sleep(2)
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

print(stormbringer_description())

print("\nLyra: " + 
        "Allow me to teach you how to properly utilize this weapon for battle.\n " + 
        "\nStormbringer's Wrath has 3 attacks.\n")
time.sleep(3)

print(stormbringer_attacks())
time.sleep(3)

print("Let us venture into The Obsidian Vault, where you will face the greatest foe of all. This is a chance to test your skills in combat, " + name + "! \n")
time.sleep(3)

print("**As you step into the first chamber, a ghostly figure appears from the shadows!**\n")
time.sleep(3)

print("Ghost:\nYour light flickers, mortal, as darkness claims its prize. Come, embrace the chill of eternity, for in my grasp, your soul shall find its rest.\n")
time.sleep(3)


# first enemy battle:

player_hp = 100
ghost_hp = 100

damage = 25    
ghost_damage = 0
actual_ghost_damage = ghost_damage

# player_attack_choice = first_battle_attack_choice(name, player_hp)
ghost_attack_choice = get_ghost_attack()

#Flag to indicate if tempest shield (attack 2) is used (reduces incoming damage by 25% for next turn)
tempest_shield_active = False 
#Flag to indicate if stormcall (attack 3) is used (increases damage by 50% for next turn)
stormcall_active = False 

enemy_hp = ghost_hp

while ghost_hp > 0 and player_hp > 0:
    # get_player_attack_choice not working properly, fix function
    attack_choice = first_battle_attack_choice(name, player_hp)
    damage, description = player_attacks[attack_choice]

    if attack_choice == 1:
        actual_damage = damage
        if stormcall_active:
            actual_damage *= 1.5
            stormcall_active = False
        print(f"\nYou unleash a powerful strike, calling down a bolt of lightning from the sky that strikes the ghost with a thunderous crash.\nThe ghost has taken {actual_damage} damage!\n")
        ghost_hp -= actual_damage
        time.sleep(2)

    elif attack_choice == 2:
        tempest_shield_active = True
        print("\nYou have summoned a defensive aura of wind and lightning, reducing incoming damage by 25%!\n")
        time.sleep(2)

    elif attack_choice == 3:
        stormcall_active = True
        print("\nYou have summoned a vicious storm, increasing damage significantly for the next turn!\n")
        time.sleep(2)

    if ghost_hp > 0:
        attack_name, ghost_damage, attack_message = get_ghost_attack()        
        if tempest_shield_active:
            ghost_damage *= 0.75
            tempest_shield_active = False
        player_hp -= ghost_damage

        print(attack_message.format(ghost_hp, ghost_damage))       
        time.sleep(2)
    

if ghost_hp <= 0:
    player_hp = heartmend_elixir(name, player_hp)
    time.sleep(2)

print("Lyra:\n Great work " + name + "! As you continue on this journey, the enemies you face will become more challenging. You are going to need some protective armor.\n ")
print("**Acquired Phoenix Guard Plate!**\n")
time.sleep(2)

# second enemy battle:

print("The air around you crackles with energy as you step into the next chamber. The ground beneath your feet is covered in ancient, glowing runes, and the walls glimmer with embedded crystals.\n")
time.sleep(3)

print("Lyra:\nBe on your guard, " + name + ". Something powerful resides here. I can feel its presence...\n")
time.sleep(3)

print("**A crystalline figure materializes before you, its body shimmering with an ethereal light. The Crystal Enigma has emerged!**\n")
time.sleep(3)

print("Enigma:\nYou dare to trespass in these sacred halls? Prepare to feel the crushing force of my wrath!\n")
time.sleep(3)


# dont give full hp after first battle if less than 100
# player_hp = 125
enigma_hp = 120

damage = 25    
enigma_damage = 0
actual_enigma_damage = enigma_damage

# player_attack_choice = next_battle_attack_choice(name, player_hp)
enigma_attack_choice = get_enigma_attack()

enemy_hp = enigma_hp

while enigma_hp > 0 and player_hp > 0:
    # get_player_attack_choice not working properly, fix function
    attack_choice = next_battle_attack_choice(name, player_hp)
    damage, description = player_attacks[attack_choice]

    if attack_choice == 1:
        actual_damage = damage
        if stormcall_active:
            actual_damage *= 1.5
            stormcall_active = False
        print(f"You unleash a powerful strike, calling down a bolt of lightning from the sky that strikes the enigma with a thunderous crash. The enigma has taken {actual_damage} damage!\n")
        enigma_hp -= actual_damage
        time.sleep(2)

    elif attack_choice == 2:
        tempest_shield_active = True
        print("You have summoned a defensive aura of wind and lightning, reducing incoming damage by 25%!\n")
        time.sleep(2)

    elif attack_choice == 3:
        stormcall_active = True
        print("You have summoned a vicious storm, increasing damage significantly for the next turn!\n")
        time.sleep(2)

    if enigma_hp > 0:
        attack_name, enigma_damage, attack_message = get_enigma_attack()        
        if tempest_shield_active:
            enigma_damage *= 0.75
            tempest_shield_active = False
        player_hp -= enigma_damage

        print(attack_message.format(enigma_hp, enigma_damage))       

    time.sleep(2)

if enigma_hp <= 0:
    player_hp = restoration_potion(name, player_hp)
    time.sleep(2)

print("Lyra:\nGreat work, " + name + "! You've proven your strength once again. However, the final boss battle is still ahead, and it will be your greatest challenge yet. Stay sharp and be prepared for anything.\n")
time.sleep(3)

print("As you catch your breath, the chamber begins to tremble. The walls shift and part, revealing a hidden passage that descends into the depths of The Obsidian Vault. A sense of foreboding washes over you as you step forward.\n")
time.sleep(3)

print("Lyra:\nThis is it, " + name + ". The core of The Obsidian Vault lies ahead, and with it, the final guardian. Nyxarion, the Eternal Warden, awaits you. Remember everything you've learned, and may your courage guide you through this last trial.\n")
time.sleep(3)

print("The air grows colder and the shadows deepen as you make your way through the narrow passage. The sound of distant echoes and the flicker of arcane energy become your only companions. At last, you emerge into a vast, dark chamber, illuminated by the eerie glow of molten magma and ancient runes carved into obsidian walls.\n")
time.sleep(3)

print("Eternal Warden:\nIntruder, you have come far, but this is where your journey ends. I am the Eternal Warden, and I shall protect the secrets of this vault with my very essence. Prepare yourself, for only one of us will leave this place alive.\n")
time.sleep(3)

print("The ground beneath you shakes as the Warden raises his blade, ready to unleash its fury. The ultimate challenge awaits. This is the final battle!\n")
time.sleep(3)


# player hp does not update after using restoration potion, fix this
warden_hp = 120

damage = 25    

warden_damage = 0
# warden attacks do 0 damage, fix this
actual_warden_damage = warden_damage

# player_attack_choice = next_battle_attack_choice(name, player_hp)
warden_attack_choice = get_warden_attack()

enemy_hp = enigma_hp

while warden_hp > 0 and player_hp > 0:
    # get_player_attack_choice not working properly, fix function
    attack_choice = next_battle_attack_choice(name, player_hp)
    damage, description = player_attacks[attack_choice]

    if attack_choice == 1:
        actual_damage = damage
        if stormcall_active:
            actual_damage *= 1.5
            stormcall_active = False
        print(f"You unleash a powerful strike, calling down a bolt of lightning from the sky that strikes the enigma with a thunderous crash. The enigma has taken {actual_damage} damage!\n")
        warden_hp -= actual_damage
        time.sleep(2)

    elif attack_choice == 2:
        tempest_shield_active = True
        print("You have summoned a defensive aura of wind and lightning, reducing incoming damage by 25%!\n")
        time.sleep(2)

    elif attack_choice == 3:
        stormcall_active = True
        print("You have summoned a vicious storm, increasing damage significantly for the next turn!\n")
        time.sleep(2)

    if warden_hp > 0:
        attack_name, enigma_damage, attack_message = get_warden_attack()        
        if tempest_shield_active:
            warden_damage *= 0.75
            tempest_shield_active = False
        player_hp -= warden_damage

        print(attack_message.format(warden_hp, warden_damage))       

    time.sleep(2)

if warden_hp <= 0:
    print("With a final, earth-shattering roar, The Eternal Warden crumbles to the ground, its obsidian form shattering into countless fragments. The once-intimidating guardian is no more, and the chamber falls silent.\n")
    time.sleep(3)

    print("Lyra:\nYou've done it, " + name + "! The Obsidian Vault is no longer a threat. You have proven yourself to be a true hero, overcoming every challenge thrown your way. The realm owes you a debt of gratitude.\n")
    time.sleep(3)

    print("As the dust settles, a hidden door behind where The Warden stood opens, revealing the heart of The Obsidian Vault. Inside, treasures of unimaginable value and ancient knowledge are laid bare, rewards for your perseverance and bravery.\n")
    time.sleep(3)

    print("Lyra:\nThis is your victory, " + name + ". The treasures and secrets of the vault are now yours to claim. But more importantly, you have ensured the safety and peace of all. Your name will be remembered for generations to come.\n")
    time.sleep(3)

    print("You take a deep breath, feeling a sense of accomplishment and relief. The journey has been long and arduous, but you have emerged victorious. As you step forward to claim your reward, the light of the vault shines brighter, signaling the dawn of a new era.\n")
    time.sleep(3)

    print("Congratulations, " + name + "! You have beaten the game and saved the realm from the darkness of The Obsidian Vault. Thank you for playing!\n")
    




