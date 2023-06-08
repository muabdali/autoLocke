from PIL import Image, ImageEnhance
import pytesseract
import cv2
import numpy as np

class imageEnhancer:
    def enhanceFunction(imageToEnhance):
        image = Image.open(imageToEnhance)
        image = image.convert('L')
        image = ImageEnhance.Contrast(image).enhance(2.0)
        image.save('EnhanceImage.png')
        text = pytesseract.image_to_string(image)
        return text
    def emeraldFunction(imageToEnhance):
        image = cv2.imread(imageToEnhance)
        # Convert HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #  brown/orange color in HSV
        lower_brown = np.array([10, 100, 100])
        upper_brown = np.array([25, 255, 255])
        brown_mask = cv2.inRange(hsv_image, lower_brown, upper_brown)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        brown_mask = cv2.morphologyEx(brown_mask, cv2.MORPH_OPEN, kernel)
        brown_mask = cv2.morphologyEx(brown_mask, cv2.MORPH_CLOSE, kernel)

        # Apply bitwise-and operation to remove the brown/orange regions from the original image
        result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(brown_mask))

        # Save the resulting image
        cv2.imwrite('autolocke/Images/RouteImage.png', result)
        
        text = pytesseract.image_to_string(result, lang='ruby')
        print(text)
        return text