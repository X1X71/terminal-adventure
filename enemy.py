import time
import random

player_hp = 100
ghost_damage = 0
actual_ghost_damage = ghost_damage

def get_ghost_attack():
    # Retrieves a random ghost attack from the `ghost_attack` dictionary.
    # Returns a tuple containing the attack name (str), ghost damage (int), and attack message (str).   
    attack_name = random.choice(list(ghost_attack.keys()))
    ghost_damage, attack_message = ghost_attack[attack_name]
    time.sleep(1.5)
    return attack_name, ghost_damage, attack_message
time.sleep(2.5)

ghost_attack = {
    "phantom_grasp": (10, "Ghost: {}/100 HP\nThe ghost used Phantom Grasp!\nYou have taken {} damage!\n"),
    "ephemeral_phase": (5, "Ghost: {}/100 HP\nThe ghost used Ephemeral Phase!\nYou have taken {} damage!\n"),
    "wall_of_despair": (15, "Ghost: {}/100 HP\nThe ghost used Wall of Despair!\nCritical hit! You have taken {} damage!\n"),
    "soul_siphon": (10, "Ghost: {}/100 HP\nThe ghost used Soul Siphon!\nYou have taken {} damage!\n")
}


