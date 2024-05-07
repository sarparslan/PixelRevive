import os
import time
from Bitwise_Not.BitwiseNotOperations import BitwiseNotOperations
from Inpaint.InpaintOperations import InpaintOperations



operation = input("Enter operation : \nbitwise_not 1 \t inpaint 2 : ")
while(operation != '0' or operation != '1'):
    if(operation == str(1)):
        image_path = input("Enter the image path of your target image for BitwiseNot Operation (It must be in bmp format): ")

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
        break
    
    # blackbuck -> 24
    # bmp_24 -> 24
    # greenland_grid_velo -> 24
    # snail -> 24
    # bmp_08 -> 8 
    # dots -> 8 
    # lena -> 8   

        
    elif(operation == str(2)):        
        image_path = input("Enter the image path of your target image for Inpaint Operation ")

        print("Inpaint Operation is loading for the image_path : "+image_path)
        time.sleep(1)
        filename_with_extension = os.path.basename(image_path)
        # Spliting the filename to remove the extension
        fileName, _ = os.path.splitext(filename_with_extension)
        mask_path = 'Inpaint/Inpaint_Masks/'+fileName+"_mask.jpeg"
        time.sleep(1)


        # Generate the mask
        InpaintOperations.create_mask_from_image(image_path, mask_path)    
        print("Mask has been created in "+mask_path)
        time.sleep(1)
        print("\nAppliyng First Marching Method...")
        result_path = 'Inpaint/Inpaint_Outputs/'+fileName+"_restorated.png"
        InpaintOperations.first_marching_method(image_path, mask_path,result_path)    
        print("Restored Image has been created in "+result_path)
        break

    else:
        print("Entered a different character")
        operation = input("Enter operation : \nbitwise_not 1 \t inpaint 2 : ")
