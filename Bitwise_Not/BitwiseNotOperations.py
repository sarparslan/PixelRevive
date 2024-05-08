import cv2
import numpy as np

class BitwiseNotOperations:
    @staticmethod
    def read_image(file_path):
        # Reading the image in unchanged mode to preserve color channels and depth
        return cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

    @staticmethod
    def write_image(file_path, image):
        # Converting the Python list back to a NumPy array to use cv2.imwrite
        array_image = np.array(image, dtype=np.uint8)
        cv2.imwrite(file_path, array_image)

    @staticmethod
    def manual_bitwise_not(image):
        # Geting image dimensions
        height, width = image.shape[:2]
        if len(image.shape) == 2:
            channels = 1  # Grayscale image
        else:
            channels = image.shape[2]  # Color image

        # Creating a new image for the inverted data 
        inverted_image = []
        for y in range(height):
            row = []
            for x in range(width):
                if channels == 1:
                    # For grayscale images
                    inverted_value = 255 - image[y, x]
                    row.append(inverted_value)
                else:
                    # For color images
                    pixel = []
                    for c in range(channels):
                        inverted_value = 255 - image[y, x, c]
                        pixel.append(inverted_value)
                    row.append(pixel)
            inverted_image.append(row)

        return inverted_image
