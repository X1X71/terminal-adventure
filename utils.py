import time
stormhollow = 1
eldoria = 2

def choose_town():
    while True:
        try:
            town = int(input('Where would you like to start your adventure?\n 1.) Stormhollow 2.) Eldoria\n '))
            if town in [1, 2]:                
                return town
            else:
                print("Invalid choice. Select 1.) Stormhollow or 2.) Eldoria to start your adventure!\n")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

def get_stormhollow_intro():
    return("As you step into the rugged town of Stormhollow, bracing against the salty sea breeze, a figure emerges from the shadows of a sturdy stone building." + 
          " Clad in practical, weather-worn attire, she walks with a confident, purposeful stride. Her striking green eyes, reflecting the determination and resilience of the town, meet yours." + 
          "\"Greetings, adventurer,\" she says in a calm, steady voice. \"I am Elara Windrider, your guide through these treacherous lands. Stormhollow is a place of legends and bravery, " + 
          "and I am here to help you navigate its storms and uncover its hidden treasures. Together, we will explore the rugged cliffs, the turbulent seas, and the ancient relics that lie in wait.\"" + 
          "Her presence exudes a blend of calm assurance and adventurous spirit, filling you with a sense of readiness for the journey ahead. With Elara by your side," + 
          " you feel prepared to face the challenges of Stormhollow and discover the stories waiting to be told.\n")

def get_eldoria_intro():
    return("As you step into the mystical realm of Eldoria, a figure emerges from the shadows cast by the towering Eldertree. " + 
          "Lyra Sunshadow, with her flowing robes adorned with celestial motifs and a staff aglow with ethereal light, approaches you with a serene smile. " + 
          "Her eyes, like shimmering pools reflecting the night sky, hold an ancient wisdom that seems to transcend time itself." + 
          "\"Welcome, traveler,\" Lyra greets you with a voice as soft as the whisper of the wind through the forest canopy.\n" + "\"I am Lyra Sunshadow, " +
          "guardian of the cosmic energies that weave through the fabric of Eldoria. This town, cradled within the embrace of the ancient forest, is a sanctuary where the realms of magic and nature converge.\"\n" + 
          "Gesturing towards the majestic Eldertree, its branches reaching towards the stars above, Lyra continues, \"Eldoria is a place of wonder and enchantment, " + 
          "where the celestial harmonies blend with the earthly melodies to create a symphony of magic.\nHere, amidst the glow of moonlight and the dance of the constellations, " + 
          "you will find yourself on a journey of self-discovery and enlightenment, guided by the cosmic forces that shape our destinies.\n")

def stormbringer_description():
    time.sleep(2)
    return("Stormbringer's Wrath is a legendary weapon, forged in the heart of a celestial tempest. This two-handed greatsword contains the raw power of a storm, its blade constantly crackling with arcs of electricity.\n" + 
        "Embedded within the crossguard is a sapphire gem that pulses with an inner light, resonating with the weapon's electric fury.")  
        

