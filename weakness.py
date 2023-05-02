from pokedex import pokedex

pokedex = pokedex.Pokedex()

pokemon = pokedex.get_pokemon_by_name('pikachu')
pokemon_types = [t for t in pokemon[0]['types'] if t == 'Electric']
print(pokemon_types)


class weaknessGrab():
    def __init__(self):
        self.pokedex = pokedex.Pokedex()
        self.weaknessDict = {
            'Electric':None,
            'Poison':None,
            'Ground':None,
            'Fire':None,
            'Water':None,
            'Grass':None,
            'Rock':None,
            'Flying':None,
            'Ghost':None,
            'Poison':None,
            'Poison':None,
            'Poison':None,
            'Poison':None,


        }