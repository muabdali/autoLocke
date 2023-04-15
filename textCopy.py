import pyautogui
import pytesseract
from PIL import Image
import time

# Define the region of the screen to capture
x, y, width, height = 242, 47, 745, 121

# Take a screenshot of the region and save it as an image file
#screenshot = pyautogui.screenshot(region=(x, y, width, height))
#screenshot.save('screenshot.png')

# Load the image file and extract text from it
cordsDictionary = {
    'Route':[242, 47, 745, 121],
    'Pokemon':[1,2,34,5]
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
    def takeScreenshot(self, section_name):
        self.section = cordsDictionary[section_name]
        x, y, width, height = self.section[0], self.section[1], self.section[2], self.section[3]
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f'{section_name}Image.png')

    def screenshotAnalyze(self, requestedImage):

        imageGiven = Image.open(requestedImage)
        text = pytesseract.image_to_string(imageGiven)

        if self.oldtext != text:
            print(text)
            self.oldtext = text



    def takeAnalyzeLoop(self, requestedImage, section_name):
        while True:
            self.takeScreenshot(section_name)
            self.screenshotAnalyze(requestedImage
                                   )
            time.sleep(1)





ia = ImageDiscover(cordsDictionary)
ia.takeAnalyzeLoop('routeImage.png', 'Route')

"""
ib = ImageAnalyze(cordsDictionary)
ib.screenshotText('routeImage.png')
"""
