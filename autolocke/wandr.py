import pandas as pd
import csv
import ast
import json

class wandr():
    def __init__(self):
        self.Gen3TableData = 'autolocke/Data/1to5.csv'
        self.pokeList = []
        self.typingDict = {}
        self.weaknessList = []
        self.pokemonTypingDict = {}

    def multiplier(self, attack, defense):
        data = pd.read_csv(self.Gen3TableData, index_col=0)
        intersection_value = data.loc[attack, defense]
        print(intersection_value)

    def weaknessFinder(self, defense):
        data = pd.read_csv(self.Gen3TableData, index_col=0)
        weaknesses = data[defense]
        wDict = data[defense].to_dict()
        weakOnly = {key for key, value in wDict.items() if value == '2'}
        return weakOnly
    
    def resistanceFinder(self, defense):
        data = pd.read_csv(self.Gen3TableData, index_col=0)
        resistance = data.loc[defense]
        resOnly = {key for key, value in resistance.items() if value == '1/2'}
        return resOnly



    def getTyping(self):
        typingList = []
        
        for pokemon in self.pokeList:
            if pokemon in self.typingDict:
                typings = self.typingDict[pokemon]
                typingList.append(typings)
        

    def loadTypingDict(self):
        with open('autolocke/Data/pokeTypeMasterSheet.csv', 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip the header row
            
            for row in csv_reader:
                pokemon = row[0].strip()
                typings = [typ.strip() for typ in row[1:]]
                self.typingDict[pokemon] = typings

    def csvInputToOutput(self):
        with open('autolocke/Data/wandr.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            
            for row in csv_reader:
                if row:  # Skip empty lines
                    self.pokeList.append(row[0].strip())
            print(self.pokeList)
    
    def pokemonTyping(self):
        with open('autolocke/Data/pokeTypeMasterSheet.json') as file:
            data = json.load(file)
        pokemon_types = {}
        for name in self.pokeList:
            for pokemon in data:
                if pokemon['Name'] == name:
                    pokemon_types[name] = pokemon['Type1']
                    if pokemon['Type2']:
                        pokemon_types[name].extend(pokemon['Type2'])
                    break
            else:
                pokemon_types[name] = 'Not Found'
        print(pokemon_types)
        self.pokemonTypingDict = pokemon_types

    def isolateType(self):
        for pokemon, types in self.pokemonTypingDict.items():
            if len(types) > 1:
                type_string = ' and '.join(types)
                print(type_string)
                if len(type_string) >8:
                    type1, type2 = type_string.split(" and ")
                    weakness1 = self.weaknessFinder(type1)
                    weakness2 = self.weaknessFinder(type2)
                    print(f'The Pokemon {pokemon} is {type1, type2} and is weak to {weakness1, weakness2}')
            else:
                print(types[0])
    
    def save_dictionary_as_csv(self):
        keys = self.pokemonTypingDict.keys()
        values = self.pokemonTypingDict.values()

        with open('autolocke/Data/wandrTyping.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(keys)
            writer.writerow(values)

test = wandr()

test.csvInputToOutput()
test.getTyping()
test.pokemonTyping()
test.isolateType()
