import pyautogui
import pytesseract
from PIL import ImageEnhance, Image
import time
from autolocke.fuzzyCheck import fuzzChecker
from autolocke.pytessGrayscaletest import *
import json
import os

# Define the region of the screen to capture
x, y, width, height = 242, 47, 745, 121

# Take a screenshot of the region and save it as an image file
#screenshot = pyautogui.screenshot(region=(x, y, width, height))
#screenshot.save('screenshot.png')

# Load the image file and extract text from it

cordsDictionary = {
    'Emerald Route':[242, 49, 700, 161],
    'Emerald Caught':[270, 800, 380, 207],
    'Fire Red Route':[242, 47, 745, 121],
    'Fire Red Caught':[250, 820, 380, 207]
}

"""
TODO - change reference check for fuzzywuzzy for appropriate txt route, right now
it only checks fireredroutes no matter which gen is selected.

"""

#cordsDictionary removed from here, now only in file where ImageDiscover is called
class ImageDiscover:
    def __init__(self, cordsDictionary, routeDict):
        self.dict = cordsDictionary
        self.oldtext = ''
        self.currentPokemon = ''
        self.currentRoute = ''
        self.routeDictionary = routeDict
    

    def takeScreenshot(self, section_name, currentGenScreenshot):
        #grabs the coords for the screenshot TODO: instead of multiple small screenshots, it should be just one big screenshot where the functions take snippets FROM, thereby halving the amount of screenshots.
        self.file_path_route = ("autolocke/Images/RouteImage.png")
        self.file_path_caught = ("autolocke/Images/CaughtImage.png")
        self.section = cordsDictionary[f'{currentGenScreenshot} {section_name}']
        x, y, width, height = self.section[0], self.section[1], self.section[2], self.section[3]
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        script_directory = os.path.dirname(os.path.abspath(__file__))
        if section_name == 'Route':
            screenshot.save(self.file_path_route)
        else:
            screenshot.save(self.file_path_caught)


    def appendRoutePokeDict(self, CurrentRoute, CaughtPokemon):
        self.dict[CurrentRoute] = CaughtPokemon
        print(self.dict[CurrentRoute])


    def screenshotAnalyze(self, requestedImage, currentDirectory, analyzedGen=None):
        ia = fuzzChecker
        if analyzedGen == "Emerald":
            if requestedImage == 'autolocke/Images/RouteImage.png':
                text = imageEnhancer.emeraldFunction(requestedImage)
            elif requestedImage == 'autolocke/Images/CaughtImage.png':
                text = imageEnhancer.emeraldCaught(requestedImage)
            else:
                return
        else:
            text = imageEnhancer.enhanceFunction(requestedImage)
        if requestedImage == 'autolocke/Images/RouteImage.png':
            stripText = text.strip()
<<<<<<< HEAD
            routeFuzz = ia.checkList(currentDirectory, stripText, minScore=90)
=======
            routeFuzz = ia.checkList(currentDirectory,stripText, minScore=84)
>>>>>>> 39c54c80c394d7f9130cf835ecdbe78b9337d658
            print(self.currentRoute + "CURRENT ROUTE SELF")
            
            if routeFuzz in self.routeDictionary:
                print("in dict")
                routeFuzzFinal = routeFuzz
                self.currentRoute = routeFuzzFinal
        elif requestedImage == 'autolocke/Images/CaughtImage.png':
            if "Gotcha" in text:
                print("if caught")
<<<<<<< HEAD
                if "!" in text:
                    if analyzedGen == "Emerald":
                        gotchaOrNot, pokemonName = text.split("!")
                    else:
                        gotchaOrNot, pokemonName = text.split("!\n")

                elif "|\n" in text:
                    gotchaOrNot, pokemonName = text.split("|\n")
                else:
                    print("CAUGHT ERROR89 tC.p")
                fuzz_pokemonName = ia.checkList('autolocke/Data/NatDexPokemonG3.txt', pokemonName, minScore=80)
                print(gotchaOrNot, pokemonName)
                print(fuzz_pokemonName)
                
                if 'Gotcha' in gotchaOrNot:
=======
                if "\n" in text:
                    gotchaOrNot, pokemonName, filler = text.split("\n")
                else:
                    if "!" in text:
                        gotchaOrNot, pokemonName = text.split("!")
                    elif "|\n" in text:
                        gotchaOrNot, pokemonName = text.split("|\n")
                    else:
                        print("CAUGHT ERROR89 tC.p")
                fuzz_pokemonName = ia.checkList('autolocke/Data/NatDexPokemonG3.txt', pokemonName, minScore=80)
                print(gotchaOrNot, pokemonName)
                print(fuzz_pokemonName)
                """
                OLD VERSION WITH NO ERROR CATCH
                if gotchaOrNot == 'Gotcha ':
                    print(f"Caught {fuzz_pokemonName} in {self.currentRoute}")
                    self.routeDictionary[self.currentRoute] = fuzz_pokemonName
                    print(self.routeDictionary[self.currentRoute])
                    json_string = json.dumps(self.routeDictionary)
                    with open("autolocke\Data\data.json", "w") as f:
                        f.write(json_string)
                """
                if "Gotcha" in gotchaOrNot:
>>>>>>> 39c54c80c394d7f9130cf835ecdbe78b9337d658
                    print(f"Caught {fuzz_pokemonName} in {self.currentRoute}")
                    if fuzz_pokemonName:
                        self.routeDictionary[self.currentRoute] = fuzz_pokemonName
                    else:
                        # Handle the case when the value is empty
                        self.routeDictionary.pop(self.currentRoute, None)
                    print(self.routeDictionary[self.currentRoute])
                    json_string = json.dumps(self.routeDictionary)
                    with open("autolocke/Data/data.json", "w") as f:
                        f.write(json_string)
                else:
                    return
            else:
                return

            

