# Pokemon Information Page Generation
This script allows for the user to select from a list of pokemon and generate an **HTML** file containing detailed information about the pokemon.

The files generated are stored in the **html** and **css** folders. The html file is named like the selected pokemon and the sylesheet is named like the pokemon type.

All information about the pokemon is retrieved from the **PokeAPI**
PokeApi Documentation: https://pokeapi.co/ 

## Running the Code
1. Install the corresponding python modules
```python
pip install bs4
pip install requests
```
2. In the path where the **pokemon.py** file is located, run the following command
```python
py .\pokemon.py 

```
3. Introduce the desired pokemon according to the list displayed
4. Find the generated file inside the **HTML** folder and open it to see the results!

### Adding New Pokemon
It supports the first of a 3 step evolution pokemon. Types include grass, water, fire and electric types.

You can add more pokemon to the list by appending their names to the array on line 42.

```python
pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pichu', 'elekid', 'chikorita', 'cyndaquil']
```
### Adding New Type Formats
In order to add a new cholor shceme for the generated document, add a new **elif** condition for the code block begining in line 133

```python
elif(pokemon_type == 'new_type'):
    back_color = "rgb_color for the background"
    letter_color = "rgb_color for the text"
```