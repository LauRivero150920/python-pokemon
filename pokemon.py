import requests 
import json

def retrieve_response(url, selected_pokemon):
    response_pokemon = requests.get(url + selected_pokemon)
    data = response_pokemon.text
    output = json.loads(data)
    return output

print("**** Pokemon list ****")
pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pichu']

for i in range(4):
    print(i + 1,pokemon[i])

print("**********************")
selected_pokemon = input("Select your pokemon: ")

while(int(selected_pokemon) > 4 or int(selected_pokemon) < 1):
    selected_pokemon = input("Please select a valid pokemon: ")

selected_pokemon = pokemon[int(selected_pokemon) - 1]
print("You selected", selected_pokemon)

pokemon_API_info = retrieve_response('https://pokeapi.co/api/v2/pokemon/', selected_pokemon)

# Pokemon Type
pokemon_type = pokemon_API_info['types'][0]['type']['name']

# Pokemon Image
image_link = pokemon_API_info['sprites']['other']['dream_world']['front_default']

# Double damage from
db_dmg = retrieve_response('https://pokeapi.co/api/v2/type/', pokemon_type)

db_dmg_from_array = []
db_dmg_from = db_dmg['damage_relations']['double_damage_from']

db_dmg_from_array = [0 for i in range(len(db_dmg_from))] 
for i in range(len(db_dmg_from)):
    db_dmg_from_array[i] = db_dmg_from[i]['name']

# Double damage to
db_dmg_to_array = []
db_dmg_to = db_dmg['damage_relations']['double_damage_to']

db_dmg_to_array = [0 for i in range(len(db_dmg_to))] 
for i in range(len(db_dmg_to)):
    db_dmg_to_array[i] = db_dmg_to[i]['name']

# Evolutions
pokemon_species_info = retrieve_response('https://pokeapi.co/api/v2/pokemon-species/', selected_pokemon)
evolution_chain_url = pokemon_species_info['evolution_chain']['url']
evolution_chain = retrieve_response(evolution_chain_url, "")
evolution_1 = evolution_chain['chain']['evolves_to'][0]['species']['name']
evolution_2 = evolution_chain['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']

# Hp, Attack, Defense
poke_stats = pokemon_API_info['stats']

poke_hp = poke_stats[0]['base_stat']
poke_attack = poke_stats[1]['base_stat']
poke_defense = poke_stats[2]['base_stat']

# Base Experience
poke_base_exp = pokemon_API_info['base_experience']

# Pokemon Abilities: Name, effects
abilities_names = []
abilities_array = []
abilities = pokemon_API_info['abilities']

abilities_names = [0 for i in range(len(abilities))]
abilities_array = [0 for i in range(len(abilities))]

for i in range(len(abilities)):
    ability = abilities[i]['ability']
    ability_name = ability['name']
    ability_url = ability['url']

    abilities_names[i] = ability_name

    abilities_array[i] = retrieve_response(ability_url, "")['effect_entries'][1]['effect']

#* HTML Generation
poke_html = open("html/" + selected_pokemon + ".html", "a")
base_file = open('html/base.html','r')

if(pokemon_type == 'fire'):
    back_color = "rgb(212, 114, 114)"
    letter_color = "rgb(245, 243, 243)"
elif(pokemon_type == 'water'):
    back_color = "rgb(128, 203, 232)"
    letter_color = "rgb(245, 243, 243)"
elif(pokemon_type == 'electric'):
    back_color = "rgb(232, 206, 128)"
    letter_color = "rgb(21, 21, 21)"
elif(pokemon_type == 'grass'):
    back_color = "rgb(113, 201, 150)"
    letter_color = "rgb(21, 21, 21)"

data = [0 for i in range(20)]

with open('css/style.css', 'r') as poke_css:
    data = poke_css.readlines()

data[1] = f"\tbackground-color: {back_color};\n"
data[2] = f"\tcolor: {letter_color};\n"

with open('css/style.css', 'w') as poke_css:
    poke_css.writelines(data)

for line in base_file:
    poke_html.write(line)