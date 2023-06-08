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
    'Route':[242, 47, 745, 121],
    'Pokemon':[300, 110, 450, 121],
    'Caught':[270, 800, 380, 207]
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

    def takeScreenshot(self, section_name):
        #grabs the coords for the screenshot TODO: instead of multiple small screenshots, it should be just one big screenshot where the functions take snippets FROM, thereby halving the amount of screenshots.
        self.section = cordsDictionary[section_name]
        x, y, width, height = self.section[0], self.section[1], self.section[2], self.section[3]
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        script_directory = os.path.dirname(os.path.abspath(__file__))
        images_directory = os.path.join(script_directory, "Images")
        file_path = os.path.join(images_directory, f'{section_name}Image.png')
        screenshot.save(file_path)



    def appendRoutePokeDict(self, CurrentRoute, CaughtPokemon):
        self.dict[CurrentRoute] = CaughtPokemon
        print(self.dict[CurrentRoute])


    def screenshotAnalyze(self, requestedImage, currentDirectory, analyzedGen=None):
        ia = fuzzChecker
        if analyzedGen == "Emerald":
            text = imageEnhancer.
        else:
            text = imageEnhancer.enhanceFunction(requestedImage)
        if requestedImage == 'autolocke\\Images\\routeImage.png':
            stripText = text.strip()
            routeFuzz = ia.checkList(currentDirectory,stripText, minScore=90)
            print(self.currentRoute + "CURRENT ROUTE SELF")
            
            if routeFuzz in self.routeDictionary:
                print("in dict")
                routeFuzzFinal = routeFuzz
                self.currentRoute = routeFuzzFinal
        elif requestedImage == 'autolocke\\Images\\CaughtImage.png':
            if "Gotcha" in text:
                print("if caught")
                if "!" in text:
                    gotchaOrNot, pokemonName = text.split("!\n")
                elif "|\n" in text:
                    gotchaOrNot, pokemonName = text.split("|\n")
                fuzz_pokemonName = ia.checkList('autolocke/Data/NatDexPokemonG3.txt', pokemonName)
                print(gotchaOrNot, pokemonName)
                print(fuzz_pokemonName)
                if gotchaOrNot == 'Gotcha ':
                    print(f"Caught {fuzz_pokemonName} in {self.currentRoute}")
                    self.routeDictionary[self.currentRoute] = fuzz_pokemonName
                    print(self.routeDictionary[self.currentRoute])
                    json_string = json.dumps(self.routeDictionary)
                    with open("autolocke\Data\data.json", "w") as f:
                        f.write(json_string)

                else:
                    return
            else:
                return

            

