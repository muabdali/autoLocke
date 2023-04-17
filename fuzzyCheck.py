from fuzzywuzzy import process


class fuzzChecker:
    def __init__(self, pokeList, nameToCheck):
        self.list = pokeList
        self.name = nameToCheck
    def checkList(pokeList, nameToCheck):
        with open(pokeList, 'r') as f:
            string_list = [line.strip() for line in f]
        best_match = process.extractOne(nameToCheck, string_list)
        print(best_match)
        return best_match
        