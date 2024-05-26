
player_attacks = {
    1: (25, "Thunderstrike: A devastating blow that calls down a bolt of lightning from the sky, dealing 25 damage."),
    2: (0, "Tempest Shield: A defensive aura that surrounds the wielder with a vortex of wind and lightning, reducing incoming damage by 25%."),
    3: (0, "Stormcall: Summon a localized storm, increasing the wielder's damage for one turn.")
}

def stormbringer_attacks(): 
        return ("1.) Thunderstrike: A devastating blow that calls down a bolt of lightning from the sky, dealing 25 damage.\n" + 
        "2.) Tempest Shield: A defensive aura that surrounds the wielder with a vortex of wind and lightning, reducing incoming damage by 25%. for one turn.\n" + 
        "3.) Stormcall: Summons a localized storm, increasing the wielder's damage for one turn.\n")
        

def first_battle_attack_choice(name, player_hp):
    while True:
        try:        
            print(f"{name}: {player_hp}/100 HP\nAttack:")
            print(stormbringer_attacks())
            choice = int(input("Choose your attack (1, 2, or 3): "))  
                                        
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# adjusted for 125hp after first battle
def next_battle_attack_choice(name, player_hp):
     while True:
        try:            
            print(f"{name}: {player_hp}/125 HP\nAttack:")
            print(stormbringer_attacks())
            choice = int(input("Choose your attack (1, 2, or 3): "))                               
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")