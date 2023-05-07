import pyautogui
import pytesseract
from PIL import Image
import time
from fuzzyCheck import fuzzChecker

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
    'PALLET TOWN': None,
    'ROUTE 1': None,
    'VIRIDIAN CITY': None,
    'ROUTE 22': None,
    'ROUTE 2': None,
    'VIRIDIAN FOREST': None,
    'ROUTE 3': None,
    'ROUTE 4': None,
    'MT. MOON': None,
    'CERULEAN CITY': None,
    'ROUTE 24': None,
    'ROUTE 25': None,
    'ROUTE 5': None,
    'ROUTE 6': None,
    'VERMILLION CITY': None,
    'ROUTE 11': None,
    'DIGLETTS CAVE': None,
    'ROUTE 9': None,
    'ROUTE 10': None,
    'ROCK TUNNEL': None,
    'POKÉMON TOWER': None,
    'ROUTE 12': None,
    'ROUTE 8': None,
    'ROUTE 7': None,
    'CELADON CITY': None,
    'SAFFRON CITY': None

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
        imageGiven = Image.open(requestedImage)
        text = pytesseract.image_to_string(imageGiven)
        if requestedImage == 'routeImage.png':
            print("route")
            print(text)
            stripText = text.strip()
            if stripText in self.routeDictionary:
                print("in dict")
                self.currentRoute = stripText
        elif requestedImage == 'PokemonImage.png':
            print('pokemon')
            if text in 'NatDexPokemonG3.txt':
                print('existing pokemon')
        elif requestedImage == 'CaughtImage.png':
            print(text)
            if "Gotcha" in text:
                print("if caught")
                gotchaOrNot, pokemonName = text.split("!\n")
                fuzz_pokemonName = ia.checkList('NatDexPokemonG3.txt', pokemonName)
                print(gotchaOrNot, pokemonName)
                print(fuzz_pokemonName)
                if gotchaOrNot == 'Gotcha ':
                    print(f"Caught {fuzz_pokemonName} in {self.currentRoute}")
                else:
                    return
            else:
                return

                  
