import os
import time
from tkinter import Image

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
    BitwiseNotOperations.write_bmp(output_path, modified_bmp)   
    print("\nOutput image has been saved in the path : "+output_path)


 
# blackbuck -> 24
# bmp_24 -> 24
# greenland_grid_velo -> 24
# snail -> 24
# bmp_08 -> 8 
# dots -> 8 
# lena -> 8   

    
else:
    image_path = '/Users/sarparslan/Downloads/cat_damaged.png'
  #  output_path = '/Users/sarparslan/Downloads/cat_damaged_mask.jpg'
    print("Inpaint Operation is loading for the image_path : "+image_path)
    time.sleep(1)
    filename_with_extension = os.path.basename(image_path)
     # Spliting the filename to remove the extension
    fileName, _ = os.path.splitext(filename_with_extension)
    output_path = 'Inpaint/Inpaint_Masks/'+fileName+"_mask.jpeg"
    time.sleep(1)


    # Generate the mask
    InpaintOperations.create_mask_from_image(image_path, output_path)    
    print("Mask has been created in "+output_path)
    time.sleep(1)
    print("\nAppliyng First Marching Method...")
    