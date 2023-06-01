# Pokemon Information Page Generation
This script allows for the user to select from a list of pokemon and generate an **HTML** file containing detailed information about the pokemon.

### Adding New Pokemon
It supports the first of a 3 step evolution pokemon. Types include grass, water, fire and electric types.

You can add more pokemon to the list by appending their names to the array on line 42.

```python
pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pichu', 'elekid', 'chikorita', 'cyndaquil', 'totodile', 'piplup', 'oshawott']
```
### Adding New Type Formats
In order to add a new cholor shceme for the generated document, add a new **elif** condition for the code block begining in line 133

```python
elif(pokemon_type == 'new_type'):
    back_color = "rgb_color for the background"
    letter_color = "rgb_color for the text"
```