from PIL import Image, ImageEnhance
import pytesseract

# Load the image
image = Image.open('Route 16 - Sample Image.png')

# Convert the image to grayscale
image = image.convert('L')

# Increase the contrast
image = ImageEnhance.Contrast(image).enhance(2.0) # adjust the factor as needed

# Extract the text using pytesseract
text = pytesseract.image_to_string(image)

print(text)


class imageEnhancer:
    def enhanceFunction(imageToEnhance):
        img = Image.open(imageToEnhance)
        img = image.convert('L')
        img = ImageEnhance.Contrast(img).enhance(2.0)
        return img
