from pokedex import pokedex

version = "0.1"
user_agent = "hello"

pokedex = pokedex.Pokedex()

pokemon = pokedex.get_pokemon_by_name('pikachu')
pokemon_types = [t for t in pokemon[0]['types'] if t == 'Electric']
print(pokemon_types)
