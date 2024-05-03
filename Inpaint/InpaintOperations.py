from PIL import Image  
class InpaintOperations:
    @staticmethod
    def create_mask_from_image(image_path, output_path):
        # Open the input image
        image = Image.open(image_path).convert("RGB")
        width, height = image.size
        
        # Create a new image for the mask
        mask = Image.new("RGB", (width, height))
        
        # Process each pixel to create the mask
        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                if (r, g, b) == (0, 0, 0):
                    # Non-black pixels become white in the mask
                    mask.putpixel((x, y), (255, 255, 255))
                else:
                    # Black pixels remain black
                    mask.putpixel((x, y), (0, 0, 0))
            # Save the generated mask
        mask.save(output_path)
