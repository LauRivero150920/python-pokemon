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

pokemon_type = pokemon_API_info['types'][0]['type']['name']

#* Information Needed
# Pokemon Image
image_link = pokemon_API_info['sprites']['versions']['generation-vii']['ultra-sun-ultra-moon']['front_default']

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


#! Hp
#! Attack
#! Defense
#! Base Experience
#! Pokemon type
#! Pokemon Abilities: Name, effects