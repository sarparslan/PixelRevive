import cv2

class InpaintOperations:
    @staticmethod
    def create_mask_from_image(image_path, output_path):
        # Open the input image using OpenCV
        image = cv2.imread(image_path)
        
        # Check if image was successfully loaded
        if image is None:
            raise FileNotFoundError(f"Could not open or find the image: {image_path}")
        
        # Get image dimensions
        height = image.shape[0]
        width  = image.shape[1]
        
        # Create a new blank mask image
        mask = [[255 for _ in range(width)] for _ in range(height)]
        
        # Process each pixel to create the mask
        for y in range(height):
            for x in range(width):
                # Get pixel intensity values
                b, g, r = image[y, x]
                
                 # Check if the pixel is black
                if (b, g, r) == (0, 0, 0):
                    # Set the pixel to white in the mask
                    mask[y][x] = 255
                else:
                    # Set the pixel to black in the mask
                    mask[y][x] = 0

    

        
        # Save the mask to a PGM file
        with open(output_path, 'w') as f:
            f.write(f'P2\n{width} {height}\n255\n')
            for row in mask:
                f.write(' '.join(map(str, row)) + '\n')
        