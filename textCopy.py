import pyautogui
import pytesseract
from PIL import ImageEnhance, Image
import time
from fuzzyCheck import fuzzChecker
from pytessGrayscaletest import *
import json


# Define the region of the screen to capture
x, y, width, height = 242, 47, 745, 121

# Take a screenshot of the region and save it as an image file
#screenshot = pyautogui.screenshot(region=(x, y, width, height))
#screenshot.save('screenshot.png')

# Load the image file and extract text from it

cordsDictionary = {
    'Route':[242, 47, 745, 121],
    'Pokemon':[300, 110, 450, 121],
    'Caught':[270, 800, 380, 207]
}

routePokemonDict = {
    "PALLET TOWN": "",
    "ROUTE 1": "TEST",
    "VIRIDIAN CITY": "TEST",
    "ROUTE 22": "Machamp",
    "ROUTE 2": "TEST",
    "VIRIDIAN FOREST": "",
    "ROUTE 3": "",
    "ROUTE 4": "",
    "MT. MOON": "",
    "CERULEAN CITY": "",
    "ROUTE 24": "",
    "ROUTE 25": "",
    "ROUTE 5": "",
    "ROUTE 6": "",
    "VERMILION CITY": "",
    "ROUTE 11": "",
    "DIGLETTS CAVE": "",
    "ROUTE 9": "Moltres",
    "ROUTE 10": "Cleffa",
    "ROCK TUNNEL": "",
    "POKÉMON TOWER": "",
    "ROUTE 12": "",
    "ROUTE 8": "",
    "ROUTE 7": "",
    "CELADON CITY": "",
    "SAFFRON CITY": "",
    "ROUTE 16": "",
    "ROUTE 17": "",
    "ROUTE 18": "",
    "FUSCIA CITY": "",
    "SAFARI ZONE": "",
    "ROUTE 15": "",
    "ROUTE 14": "",
    "ROUTE 13": "",
    "POWER PLANT": "",
    "ROUTE 19": "",
    "ROUTE 20": "",
    "SEAFOAM ISLANDS": "",
    "CINNABAR ISLAND": "",
    "POKEMON MANSION": "",
    "ONE ISLAND": "",
    "TWO ISLAND": "",
    "THREE ISLAND": "",
    "ROUTE 21": "",
    "ROUTE 23": "",
    "VICTORY ROAD": "",
    "FOUR ISLAND": "",
    "FIVE ISLAND": "",
    "SIX ISLAND": "",
    "SEVEN ISLAND": "",
    "CERULEAN CAVE": "",
    "EXTRA1": "",
    "EXTRA2": ""
}

class ImageDiscover:
    def __init__(self, cordsDictionary, routeDict):
        self.dict = cordsDictionary
        self.oldtext = ''
        self.currentPokemon = ''
        self.currentRoute = ''
        self.routeDictionary = routeDict

    def takeScreenshot(self, section_name):
        self.section = cordsDictionary[section_name]
        x, y, width, height = self.section[0], self.section[1], self.section[2], self.section[3]
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f'{section_name}Image.png')


    def appendRoutePokeDict(self, CurrentRoute, CaughtPokemon):
        self.dict[CurrentRoute] = CaughtPokemon
        print(self.dict[CurrentRoute])


    def screenshotAnalyze(self, requestedImage):
        ia = fuzzChecker
        text = imageEnhancer.enhanceFunction(requestedImage)
        if requestedImage == 'routeImage.png':
            stripText = text.strip()
            routeFuzz = ia.checkList('fireredroutes.txt',stripText, minScore=76)
            print(routeFuzz)
            print(self.currentRoute + "CURRENT ROUTE SELF")
            
            if routeFuzz in self.routeDictionary:
                print("in dict")
                routeFuzzFinal = routeFuzz
                self.currentRoute = routeFuzzFinal
        elif requestedImage == 'CaughtImage.png':
            if "Gotcha" in text:
                print("if caught")
                if "!" in text:
                    gotchaOrNot, pokemonName = text.split("!\n")
                elif "|\n" in text:
                    gotchaOrNot, pokemonName = text.split("|\n")
                fuzz_pokemonName = ia.checkList('NatDexPokemonG3.txt', pokemonName)
                print(gotchaOrNot, pokemonName)
                print(fuzz_pokemonName)
                if gotchaOrNot == 'Gotcha ':
                    print(f"Caught {fuzz_pokemonName} in {self.currentRoute}")
                    self.routeDictionary[self.currentRoute] = fuzz_pokemonName
                    print(self.routeDictionary[self.currentRoute])
                    json_string = json.dumps(self.routeDictionary)
                    with open("data.json", "w") as f:
                        f.write(json_string)

                else:
                    return
            else:
                return

            
# NEED TO CHANGE WHICH JSON FILE GETS CAUGHT UPDATES LINE 117
