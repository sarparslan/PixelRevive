import os
import time
from Bitwise_Not.BitwiseNotOperations import BitwiseNotOperations
from Inpaint.InpaintOperations import InpaintOperations


operation = input("Enter operation : \nbitwise_not 1 \t inpaint 2 : ")
while(operation != '0' or operation != '1'):
    if(operation == str(1)):
        image_path = input("Enter the image path of your target image for BitwiseNot Operation: ")

        print("\nBitwise_Not Operation is loading for the image_path : " + image_path)
        time.sleep(1)
        filename_with_extension = os.path.basename(image_path)
        # Splitting the filename to separate file name and extension
        fileName, fileExtension = os.path.splitext(filename_with_extension)

        # Construct the output path using the original extension
        output_path = f'Bitwise_Not/Bitwise_Not_Outputs/{fileName}_result{fileExtension}'

        image = BitwiseNotOperations.read_image(image_path)
        modified_image = BitwiseNotOperations.manual_bitwise_not(image)

        # Save the modified image
        BitwiseNotOperations.write_image(output_path, modified_image)
        print("Output image has been saved in the path: " + output_path)
        break
    
        
    elif(operation == str(2)):        
        image_path = input("Enter the image path of your target image for Inpaint Operation: ")

        print("Inpaint Operation is loading for the image_path : " + image_path)
        time.sleep(1)
        filename_with_extension = os.path.basename(image_path)
        # Splitting the filename to remove the extension
        fileName, fileExtension = os.path.splitext(filename_with_extension)
        mask_path = f'Inpaint/Inpaint_Masks/{fileName}_mask.jpeg'
        time.sleep(1)

        # Generate the mask
        InpaintOperations.create_mask_from_image(image_path, mask_path)    
        print("Mask has been created in " + mask_path)
        time.sleep(1)
        print("\nApplying First Marching Method...")
        result_path = f'Inpaint/Inpaint_Outputs/{fileName}_restorated{fileExtension}'
        InpaintOperations.first_marching_method(image_path, mask_path, result_path)    
        print("Restored Image has been created in " + result_path)
        break

    else:
        print("Entered a different character")
        operation = input("Enter operation : \nbitwise_not 1 \t inpaint 2 : ")
