
def heartmend_elixir(name, player_hp):

    print(f"You have slain the ghost! Prepare for your next battle, {name}!\n")
    print("The ghost has dropped a Heartmend Elixir!")

    while True:
        heal = input("Would you like to use the Heartmend Elixir to gain 20 HP? (y/n)\n")
        if heal == "y":
            player_hp += 20
            print(f"\nYou have gained 20 HP! Current HP: {player_hp}/100 HP\n")
            break    
        elif heal == "n":
            print(f"\nYou have chosen not to use the Heartmend Elixir. Current HP: {player_hp}/100 HP\n")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
