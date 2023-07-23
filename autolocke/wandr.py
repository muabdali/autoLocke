import pandas as pd
import csv
import ast
import json

# data querying using pandas and 1to5.csv

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
        return wDict
    
    def resistanceFinder(self, defense):
        data = pd.read_csv(self.Gen3TableData, index_col=0)
        resistance = data.loc[defense]
        resOnly = {key for key, value in resistance.items() if value == '1/2'}
        return resOnly
    
    def weakcombine(self, dict1, dict2):
        result = {}

        for key in dict1:
            if key in dict2:
                value1 = float(dict1[key]) if dict1[key] != '1/2' else 0.5  # Handle resistance value '1/2'
                value2 = float(dict2[key]) if dict2[key] != '1/2' else 0.5
                result[key] = str(value1 * value2)  # Store the multiplication result as a string

        print(result)
        return result


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
                if row and row[0].strip():  # Skip empty lines and lines with empty first value
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
        combined_weaknesses = {}  # Dictionary to store combined weaknesses
        
        for pokemon, types in self.pokemonTypingDict.items():
            if len(types) > 1:
                type_string = ' and '.join(types)
                if len(type_string) > 8:
                    type1, type2 = type_string.split(" and ")
                    weakness1 = self.weaknessFinder(type1)
                    weakness2 = self.weaknessFinder(type2)
                    combined_weakness = self.weakcombine(dict1=weakness1, dict2=weakness2)
                    combined_weaknesses[pokemon] = combined_weakness
            else:
                weakness1 = self.weaknessFinder(types[0])
                combined_weaknesses[pokemon] = weakness1
        
        # Save combined_weaknesses dictionary in desired format
        self.save_dictionary_as_csv(combined_weaknesses)
        self.save_dictionary_as_json(combined_weaknesses)
        self.save_dictionary(combined_weaknesses)

    def save_dictionary_as_csv(self, dictionary):
        with open('autolocke/Data/wandrTyping.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Pokemon', 'Combined Weakness'])
            for pokemon, weaknesses in dictionary.items():
                writer.writerow([pokemon, weaknesses])

    def save_dictionary_as_json(self, dictionary):
        with open('autolocke/Data/wandrTyping.json', 'w') as jsonfile:
            json.dump(dictionary, jsonfile)

    def save_dictionary(self, dictionary):
        # No specific file extension, dictionary is returned
        # for further processing or storage
        return dictionary
