import cv2
from heapq import heappop, heappush

class InpaintOperations:
    @staticmethod
    def create_mask_from_image(image_path, output_path):
        # Reading the image from the specified path
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Could not open or find the image: {image_path}")

        height, width = image.shape[:2]
         # Initializing a blank mask with white (255)

        mask = [[255 for _ in range(width)] for _ in range(height)]

        for y in range(height):
            for x in range(width):
                # Extracting the color channels of each pixel
                b, g, r = image[y, x]
                # Set mask pixel to 255 if black, otherwise 0
                if((b,g,r) == (0,0,0)):
                    mask[y][x] = 255
                    
                else:
                    mask[y][x] = 0

         # Writing the mask to the specified output file in PGM format
        with open(output_path, 'w') as f:
            f.write(f'P2\n{width} {height}\n255\n')
            for row in mask:
                f.write(' '.join(map(str, row)) + '\n')

    @staticmethod
    def load_image_as_color(file_path):
        # Loading the image in color mode
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(f"Could not open or find the image: {file_path}")
        return image

    @staticmethod
    def load_image_as_grayscale(file_path):
        # Loading the image in grayscale mode
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Could not open or find the image: {file_path}")
        return image

    @staticmethod
    def save_color_image(image, file_path):
         # Saving the processed image to the specified file path
        cv2.imwrite(file_path, image)

    @staticmethod
    def first_marching_method(damaged_image_path, mask_image_path, output_image_path):
        # Loading the damaged image and the mask
        damaged_image = InpaintOperations.load_image_as_color(damaged_image_path)
        mask = InpaintOperations.load_image_as_grayscale(mask_image_path)

        height, width = mask.shape
        #Checks whether the distorted image and the mask are the same size
        assert damaged_image.shape[:2] == (height, width), "Error"

        pq = []
        priority_map = [[float('inf')] * width for _ in range(height)]
        distance_map = [[float('inf')] * width for _ in range(height)]

        def update_neighbors(y, x):
             # Updating neighboring pixels
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and mask[ny][nx] == 255:
                    # Calculating the distance to neighboring pixel
                    distance = abs(ny - y) + abs(nx - x)
                    if distance < distance_map[ny][nx]:
                        # Updating the distance and priority maps
                        distance_map[ny][nx] = distance
                        priority_map[ny][nx] = distance
                        # Push the neighbor to the priority queue
                        heappush(pq, (distance, ny, nx))

        # Initializing the priority queue with border pixels
        for y in range(height):
            for x in range(width):
                if mask[y][x] == 0:
                    update_neighbors(y, x)
                    
        # Processing pixels in the order of their priority
        while pq:
            _, y, x = heappop(pq)
            if mask[y][x] == 255:
                # Restoring the pixel's color by averaging neighbors' colors
                for c in range(3):
                    neighbor_values = []
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < height and 0 <= nx < width and mask[ny][nx] == 0:
                            neighbor_values.append(damaged_image[ny, nx, c])

                    if neighbor_values:
                        damaged_image[y, x, c] = int(sum(neighbor_values) / len(neighbor_values))

                # Marking the pixel as repaired
                mask[y][x] = 0
                # Updating its neighbors
                update_neighbors(y, x)

        # Saving the repaired image to the output path
        InpaintOperations.save_color_image(damaged_image, output_image_path)