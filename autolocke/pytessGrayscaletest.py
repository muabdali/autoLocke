from PIL import Image, ImageEnhance
import pytesseract
import cv2
import numpy as np

class imageEnhancer:
    def enhanceFunction(imageToEnhance):
        image = Image.open(imageToEnhance)
        text = pytesseract.image_to_string(image)
        return text
    def emeraldFunction(imageToEnhance):
        image = cv2.imread(imageToEnhance)
        # Convert HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define color ranges for brown/orange and green in HSV
        lower_brown = np.array([10, 100, 100])
        upper_brown = np.array([25, 255, 255])
        lower_green = np.array([40, 100, 100])
        upper_green = np.array([75, 255, 255])

        # Create masks for brown/orange and green pixels
        brown_mask = cv2.inRange(hsv_image, lower_brown, upper_brown)
        green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

        # Combine the masks using bitwise-or operation
        combined_mask = cv2.bitwise_or(brown_mask, green_mask)

        # Perform morphology operations on the combined mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)

        # Apply bitwise-and operation to remove the brown/orange and green regions from the original image
        result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(combined_mask))

        # Save the resulting image
        cv2.imwrite('autolocke/Images/RouteImage.png', result)

        text = pytesseract.image_to_string(result)
        print(text)
        return text