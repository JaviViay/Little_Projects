import random

pokemon = ["Charmander", "Squirtle", "Bulbasaur"]

print("Select a Pokemon:")
print("Charmander")
print("Squirtle")
print("Bulbasaur")
user_pokemon = str(input("-> "))

while user_pokemon not in pokemon:
    print("...Error! Choose a valid Pokemon")
    user_pokemon = str(input("-> "))

left_pokemon = pokemon.copy()
left_pokemon.remove(user_pokemon)
pc_pokemon = random.choice(left_pokemon)

print("You chose", user_pokemon, "and your opponent will be", pc_pokemon)

damage_plus = False
if (user_pokemon == "Charmander" and pc_pokemon == "Bulbasaur") or (pc_pokemon == "Charmander" and user_pokemon == "Bulbasaur"):
    damage_plus = True
elif (user_pokemon == "Squirtle" and pc_pokemon == "Charmander") or (pc_pokemon == "Squirtle" and user_pokemon == "Charmander"):
    damage_plus = True
elif (user_pokemon == "Bulbasaur" and pc_pokemon == "Squirtle") or (pc_pokemon == "Bulbasaur" and user_pokemon == "Squirtle"):
    damage_plus = True

charmander_attacks = ["scratch", "leer", "ember", "flamethrower"]
squirtle_attacks = ["tackle", "tail whip", "water gun", "hydro pump"]
bulbasaur_attacks = ["tackle", "growl", "vine whip", "solar beam"]

if user_pokemon == "Charmander":
    user_attacks = charmander_attacks
elif user_pokemon == "Squirtle":
    user_attacks = squirtle_attacks
elif user_pokemon == "Bulbasaur":
    user_attacks = bulbasaur_attacks

if pc_pokemon == "Charmander":
    pc_attacks = charmander_attacks
elif pc_pokemon == "Squirtle":
    pc_attacks = squirtle_attacks
elif pc_pokemon == "Bulbasaur":
    pc_attacks = bulbasaur_attacks

user_health = 100
pc_health = 100

def user_play():
    global user_health
    global pc_health
    global damage_plus
    while user_health > 0 and pc_health > 0:
        print("Choose an attack:")
        print(user_attacks[0], "  ", user_attacks[1], "  ", user_attacks[2], "  ", user_attacks[3])
        attack = str(input("-> "))
        if attack in user_attacks[2:4] and damage_plus:
            pc_health -= int(random.uniform(30, 45))
            damage_plus = False
        else:
            pc_health -= int(random.uniform(20, 30))
        print("...You used", attack+", the opponent's health now is", pc_health)
        if pc_health <= 0:
            break
        pc_play()

def pc_play():
    global user_health
    global pc_health
    global damage_plus
    attack = random.choice(pc_attacks)
    if attack in pc_attacks[2:4] and damage_plus:
        user_health -= int(random.uniform(30, 45))
        damage_plus = False
    else:
        user_health -= int(random.uniform(20, 30))
    print("...Opponent used", attack+", your health now is", user_health)

play = [user_play, pc_play]
first_play = random.choice(play)

while user_health > 0 and pc_health > 0:
    first_play()
    if user_health <= 0:
        print("...FINAL! You lost")
        break
    elif pc_health <= 0:
        print("...FINAL! YOU WON THE BATTLE")
        break
    if first_play == user_play:
        first_play = pc_play
    elif first_play == pc_play:
        first_play = user_play
