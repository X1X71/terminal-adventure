import time
import random


# first battle (ghost)

player_hp = 100
ghost_damage = 0
actual_ghost_damage = ghost_damage


# incorrect damage done to player
def get_ghost_attack():
    # Retrieves a random ghost attack from the `ghost_attack` dictionary.
    # Returns a tuple containing the attack name (str), ghost damage (int), and attack message (str).   
    attack_name = random.choice(list(ghost_attack.keys()))
    ghost_damage, attack_message = ghost_attack[attack_name]
    time.sleep(1.5)
    return attack_name, ghost_damage, attack_message
time.sleep(2.5)

ghost_attack = {
    "phantom_grasp": (5, "Ghost: {}/100 HP\nThe ghost used Phantom Grasp!\nYou have taken {} damage!\n"),
    "ephemeral_phase": (2.5, "Ghost: {}/100 HP\nThe ghost used Ephemeral Phase!\nYou have taken {} damage!\n"),
    "wall_of_despair": (5, "Ghost: {}/100 HP\nThe ghost used Wall of Despair!\nCritical hit! You have taken {} damage!\n"),
    "soul_siphon": (2.5, "Ghost: {}/100 HP\nThe ghost used Soul Siphon!\nYou have taken {} damage!\n")
}

# second battle

# +25 hp from shield received after first battle
player_hp = 125
enigma_hp = 120
enigma_damage = 0
actual_enigma_damage = enigma_damage
attack_number = 1

def get_enigma_attack():
    # Retrieves a random enigma attack from the `enigma_attack` dictionary.
    # Returns a tuple containing the attack name (str), enigma damage (int), and attack message (str).   
    global attack_number
    if attack_number == 1:
        attack_name = random.choice(list(enigma_attack.keys())[:-1])
    else:
        attack_name = random.choice(list(enigma_attack.keys()))
    attack_number += 1

    enigma_damage, attack_message = enigma_attack[attack_name]
    time.sleep(1.5)
    return attack_name, enigma_damage, attack_message
time.sleep(2.5)


# make sure enigma cannot use reconstruction first turn
enigma_attack = {
    "shard_barrage": (10, "Enigma: {}/120 HP\nThe Enigma used Shard Barrage!\nYou have taken {} damage!\n"),
    "radiant_beam": (7.5, "Enigma: {}/120 HP\nThe Enigma used Radiant Beam!\nYou have taken {} damage!\n"),
    "reflective_barrier": (5, "Enigma: {}/120 HP\nThe Enigma used Reflective Barrier!\nYou have taken {} damage!\n"),
    "reconstruction": (0, "Enigma: {}/120 HP\nThe Enigma used Radiant Beam!\nThe Enigma has regenerated 15 HP!\n")
}

if enigma_attack == "reconstruction":
    enigma_hp += 15

# third and final boss battle

player_hp = 125
warden_hp = 150
warden_damage = 0
actual_warden_damage = warden_damage
    
def get_warden_attack():
    # Retrieves a random warden attack from the `warden_attack` dictionary.
    # Returns a tuple containing the attack name (str), warden damage (int), and attack message (str).   
    attack_name = random.choice(list(warden_attack.keys()))
    warden_damage, attack_message = warden_attack[attack_name]
    time.sleep(1.5)
    return attack_name, warden_damage, attack_message
time.sleep(2.5)

warden_attack = {
    "obsidian_onslaught": (10, "Warden: {}/120 HP\nThe Warden used Obsidian Onslaught!\nYou have taken {} damage!\n"),
    "arcane_vortex": (15, "Warden: {}/150 HP\nThe Warden used Arcane Vortex!\nYou have taken {} damage!\n"),
    "magma_burst": (20, "Warden: {}/150 HP\nThe Warden used Magma Burst!\nYou have taken {} damage!\n"),
    "seismic_slam": (15, "Warden: {}/150 HP\nThe Warden used Seismic Slam!\nYou have taken {} damage!\n")
}