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
html_file = open("html/" + selected_pokemon + ".html", "a")
html_file.write("Now the file has more content!")

with open('html/base.html','r') as base_file, open("html/" + selected_pokemon + ".html", "a") as poke_html:
    for line in base_file:
        poke_html.write(line)

# red: rgb(212, 114, 114)
# yellow: rgb(232, 206, 128)
# green: rgb(113, 201, 150)
# water: rgb(128, 203, 232)