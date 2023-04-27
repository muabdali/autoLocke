from PIL import Image, ImageEnhance
import pytesseract


class imageEnhancer:
    def enhanceFunction(imageToEnhance):
        image = Image.open(imageToEnhance)
        image = image.convert('L')
        image = ImageEnhance.Contrast(image).enhance(2.0)
        text = pytesseract.image_to_string(image)
        return text
        
