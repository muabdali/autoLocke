import pyautogui
import pytesseract
from PIL import Image

# Define the region of the screen to capture
x, y, width, height = 242, 47, 745, 121

# Take a screenshot of the region and save it as an image file
#screenshot = pyautogui.screenshot(region=(x, y, width, height))
#screenshot.save('screenshot.png')

# Load the image file and extract text from it
image = Image.open('screenshot.png')
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)

cordsDictionary = {
    'Route':[242, 47, 745, 121]




}

class imageAnalyze:
    def __init__(self, cordsDictionary):
        self.dict = cordsDictionary
    def screenshotText(section):
        x = cordsDictionary[section[1]]
        y = cordsDictionary[section[2]]
        width = cordsDictionary[section[3]]
        height = cordsDictionary[section[4]]
