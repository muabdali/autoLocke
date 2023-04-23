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
    'Pallet Town':None,
    'Route 1':None,
    'Viridian City':None,
    'Route 22':None,
    'Route 2':None,
    'Viridian Forest':None,
    'Route 3':None,
    'Route 4':None,
    'Mt. Moon':None,
    'Cerulean City':None,
    'Route 24':None,
    'Route 25':None,
    'Route 5':None,
    'Route 6':None,
    'Vermillion City':None,
    'Route 11':None,
    'Digletts Cave':None,
    'Route 9':None,
    'Route 10':None,
    'Rock Tunnel':None,
    'Pokémon Tower':None,
    'Route 12':None,
    'Route 8':None,
    'Route 7':None,
    'Celadon City':None,
    'Saffron City':None,

}


class ImageDiscover:
    def __init__(self, cordsDictionary):
        self.dict = cordsDictionary
        self.oldtext = ''
        self.currentPokemon = ''
        self.currentRoute = ''


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
            if text in routePokemonDict:
                print("in dict")
                self.currentRoute = text
        elif requestedImage == 'PokemonImage.png':
            print('pokemon')
            if text in 'NatDexPokemonG3.txt':
                print('existing pokemon')
        elif requestedImage == 'CaughtImage.png':
            print(text)
            if "Gotcha" in text:
                print("if caught")
                gotchaOrNot, pokemonName = text.split("|")
                fuzz_pokemonName = ia.checkList('NatDexPokemonG3.txt', pokemonName)
                print(gotchaOrNot, pokemonName)
                print(fuzz_pokemonName)
                if gotchaOrNot == 'Gotcha ':
                    print(f"Caught {fuzz_pokemonName} in ")
                else:
                    print("not caught")
            else:
                print("not currently on battle screen")

            
            

    def encounterDetect(self, section_name):
        self.takeScreenshot(section_name)



    def takeAnalyzeLoop(self, requestedImage, section_name, requestedImage2, section_name2):
        while True:
            self.takeScreenshot(section_name)
            self.screenshotAnalyze(requestedImage)
            self.takeScreenshot(section_name2)
            self.screenshotAnalyze(requestedImage2)
            time.sleep(0.1)

ia = ImageDiscover(cordsDictionary)
while True:
    ia.takeScreenshot(section_name='Route')
    ia.screenshotAnalyze('routeImage.png')
    time.sleep(0.5)


    


"""
ia = ImageDiscover(cordsDictionary)
ia.takeScreenshot('Caught')
ia.screenshotAnalyze('CaughtImage.png')
"""