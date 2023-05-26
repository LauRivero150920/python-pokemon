import requests 
import json

print("**** Pokemon list ****")
pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pikachu']

for i in range(4):
    print(i + 1,pokemon[i])

print("**********************")
selected_pokemon = input("Select your pokemon: ")

while(int(selected_pokemon) > 4 or int(selected_pokemon) < 1):
    selected_pokemon = input("Please select a valid pokemon: ")

selected_pokemon = pokemon[int(selected_pokemon) - 1]
print("You selected", selected_pokemon)

response_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + selected_pokemon)
data = response_pokemon.text
pokemon_API_info = json.loads(data)

#print(pokemon_API_info['abilities'])
#print(pokemon_API_info)