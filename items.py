
def heartmend_elixir(name, player_hp):

    print(f"You have slain the ghost! Prepare for your next battle, {name}!\n")
    print("The ghost has dropped a Heartmend Elixir!")

    while True:
        heal = input("Would you like to use the Heartmend Elixir to gain 20 HP? (y/n)\n")
        if heal == "y":
            player_hp += 20
            print(f"\nYou have gained 20 HP!")
            # Current HP: {player_hp}/100 HP\n"
            break    
        elif heal == "n":
            print(f"\nYou have chosen not to use the Heartmend Elixir. Current HP: {player_hp}/100 HP\n")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    return player_hp

def  restoration_potion(name, player_hp):
    print(f"You have slain the enigma! Prepare for your next battle, {name}!\n")
    print("The enigma has dropped a Restoration Potion!")

    while True:
        heal = input("Would you like to use the Restoration Potion to gain 40 HP? (y/n)\n")
        if heal == "y":
            player_hp += 40
            print(f"\nYou have gained 40 HP! Current HP: {player_hp}/125 HP\n")
            break    
        elif heal == "n":
            print(f"\nYou have chosen not to use the Restoration Potion. Current HP: {player_hp}/125 HP\n")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    return player_hp