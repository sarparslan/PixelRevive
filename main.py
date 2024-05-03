import os
import time
from tkinter import Image
from PIL import Image  # PIL kütüphanesinden Image modülünü ekleyin

from Bitwise_Not.BitwiseNotOperations import BitwiseNotOperations
from Inpaint.InpaintOperations import InpaintOperations



operation = input("Enter operation : \nbitwise_not -> 1 \t inpaint -> 2 : \n")

if(operation == str(1)):
    image_path = input("Enter the image path of your target image (It must be in bmp format): ")

    print("\nBitwise_Not Operation is loading for the image_path : "+image_path)
    time.sleep(1)
    filename_with_extension = os.path.basename(image_path)

    # Spliting the filename to remove the extension
    fileName, _ = os.path.splitext(filename_with_extension)
    output_path = 'Bitwise_Not/Bitwise_Not_Outputs/'+fileName+"_result.bmp"
    
    # Reading the original BMP file.
    bmp_data = BitwiseNotOperations.read_bmp(image_path)

    # Applying bitwise NOT operation to the BMP data.
    modified_bmp = BitwiseNotOperations.bitwise_not(bmp_data)

    # Writing the modified BMP data back to a new file.
    print("\nOutput image has been saved in the path : "+output_path)
    BitwiseNotOperations.write_bmp(output_path, modified_bmp)    


 
# blackbuck -> 24
# bmp_24 -> 24
# greenland_grid_velo -> 24
# snail -> 24
# bmp_08 -> 8 
# dots -> 8 
# lena -> 8   

#   Bitwise_Not_Inputs/lena.bmp
#else:
print("Inpaint Operation is loading...")
output_path = '/Users/sarparslan/Downloads/'

# Kullanım Örneği:
image_path = '/Users/sarparslan/Downloads/cat_damaged.png'
output_path = 'Inpaint/Inpaint_Outputs/cat_damaged_mask.png'



# Generate the mask
InpaintOperations.create_mask_from_image(image_path, output_path)    