import pyautogui
import pytesseract
from PIL import Image

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
    

}


class ImageDiscover:
    def __init__(self, cordsDictionary):
        self.dict = cordsDictionary
    def takeScreenshot(self, section_name):
        print(section_name)
        self.section = cordsDictionary[section_name]
        x, y, width, height = self.section[0], self.section[1], self.section[2], self.section[3]
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f'{section_name}Image.png')
    def screenshotAnalyze(self, requestedImage):
        imageGiven = Image.open(requestedImage)
        text = pytesseract.image_to_string(imageGiven)
        print(text)







ia = ImageDiscover(cordsDictionary)
ia.screenshotAnalyze('routeImage.png')

"""
ib = ImageAnalyze(cordsDictionary)
ib.screenshotText('routeImage.png')
"""
