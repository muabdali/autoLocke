from fuzzywuzzy import process

class fuzzChecker:
    @staticmethod  # Make the method static so it can be called without an instance of the class
    def checkList(pokeList, nameToCheck):
        with open(pokeList, 'r') as f:
            string_list = [line.strip() for line in f]
        best_match = process.extractOne(nameToCheck, string_list)
        return best_match  # Return the value of best_match

    



        