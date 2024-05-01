import os
import time

from Bitwise_Not.BitwiseNotOperations import BitwiseNotOperations

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