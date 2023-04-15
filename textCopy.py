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

class ImageAnalyze:
    def __init__(self, cordsDictionary):
        self.dict = cordsDictionary
    def takeScreenshot(self, section_name):
        section = cordsDictionary[section_name]
        x, y, width, height = section[0], section[1], section[2], section[3]

        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f'{section}Image.png')
    def screenshotText(self, requestedImage):
        topLeftImage = Image.open(requestedImage)
        text = pytesseract.image_to_string(topLeftImage)
        print(text)




"""
ib = ImageAnalyze(cordsDictionary)
ib.screenshotText('routeImage.png')
"""