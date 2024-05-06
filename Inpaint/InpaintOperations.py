import cv2

import cv2
import numpy as np
from heapq import heappop, heappush
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

    @staticmethod
    def load_image_as_grayscale(file_path):
            image = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
            if image is None:
                raise FileNotFoundError(f"Could not open or find the image: {file_path}")
            return image.tolist()

    @staticmethod
    def save_image(image, file_path):
        image_np = np.array(image, dtype=np.uint8)
        cv2.imwrite(file_path, image_np)
        
    @staticmethod
    def first_marching_method(damaged_image_path, mask_image_path, output_image_path):
        damaged_image = InpaintOperations.load_image_as_grayscale(damaged_image_path)
        mask = InpaintOperations.load_image_as_grayscale(mask_image_path)

        height, width = len(damaged_image), len(damaged_image[0])
        assert len(mask) == height and len(mask[0]) == width, "Error"

        pq = []
        priority_map = np.full((height, width), np.inf)
        distance_map = np.full((height, width), np.inf)

        def update_neighbors(y, x):
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and mask[ny][nx] == 255:
                    distance = abs(ny - y) + abs(nx - x)
                    if distance < distance_map[ny][nx]:
                        distance_map[ny][nx] = distance
                        priority_map[ny][nx] = distance
                        heappush(pq, (distance, ny, nx))

        for y in range(height):
            for x in range(width):
                if mask[y][x] == 0:
                    update_neighbors(y, x)

        while pq:
            _, y, x = heappop(pq)
            if mask[y][x] == 255:
                neighbor_values = []
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width and mask[ny][nx] == 0:
                        neighbor_values.append(damaged_image[ny][nx])

                if neighbor_values:
                    damaged_image[y][x] = sum(neighbor_values) / len(neighbor_values)
                mask[y][x] = 0
                update_neighbors(y, x)

        InpaintOperations.save_image(damaged_image, output_image_path)