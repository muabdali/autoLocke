from PIL import Image, ImageEnhance
import pytesseract
import cv2
import numpy as np

class imageEnhancer:
    def enhanceFunction(imageToEnhance):
        try:
            image = Image.open(imageToEnhance)
            image = image.convert('L')
            image = ImageEnhance.Contrast(image).enhance(2.0)
            image.save('EnhanceImage.png')
            text = pytesseract.image_to_string(image)
            return text
        except:
            print(f"Error occurred during image processing: {str()}")
            return None
    def emeraldFunction(imageToEnhance):
        image = cv2.imread(imageToEnhance)
        
        # Convert image to HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define color range for white in HSV
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([255, 30, 255])

        # Create mask for white pixels
        white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

        # Perform morphology operations on the white mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)
        white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)

        # Apply bitwise-and operation to keep only the white regions from the original image
        result = cv2.bitwise_and(image, image, mask=white_mask)
        
        # Perform OCR on the resulting image
        text = pytesseract.image_to_string(result)
        return text
    
    def emeraldCaught(imageToEnhance):
        image = cv2.imread(imageToEnhance)
        output_path = "autolocke/Images/CaughtImageEmerald.png"
        # Convert image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Threshold the image to extract the white text
        _, thresholded_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY_INV)

        # Create a 4-channel image (RGBA) with transparent background
        transparent_image = np.zeros((image.shape[0], image.shape[1], 4), dtype=np.uint8)

        # Set alpha channel to 255 for white text pixels and 0 for non-white text pixels
        transparent_image[thresholded_image == 255, 3] = 255

        # Save the result image with transparent background
        cv2.imwrite(output_path, transparent_image)

        text = pytesseract.image_to_string(image=output_path)
        return text
    
