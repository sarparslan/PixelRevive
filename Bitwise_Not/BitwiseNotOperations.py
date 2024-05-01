class BitwiseNotOperations:    
    # Function to read a BMP file from the specified file path.
    @staticmethod
    def read_bmp(file_path):
        with open(file_path, 'rb') as f:
            bmp = f.read()  # Read the entire BMP file into memory.
        return bmp  # Return the contents of the BMP file.

    # Function to write data to a BMP file at the specified file path.
    @staticmethod
    def write_bmp(file_path, data):
        with open(file_path, 'wb') as f:
            f.write(data)  # Write the data to a BMP file.

    # Function to apply a bitwise NOT operation on the BMP image data.
    @staticmethod
    def bitwise_not(bmp):
        header = bmp[:54]  # BMP file header, 54 bytes.
        bpp = int.from_bytes(bmp[28:30], 'little')  # Extracting the bits per pixel from the header.
        width = int.from_bytes(bmp[18:22], 'little')  # Extracting image width from the header.
        height = int.from_bytes(bmp[22:26], 'little')  # Extracting image height from the header.

        # Calculate row padding to determine the exact row size in bytes.
        row_size = (bpp * width + 31) // 32 * 4
        img_data_size = row_size * abs(height)
        img_data_start = 54
        img_data = bmp[img_data_start:img_data_start+img_data_size]

        if bpp == 8:  # Handling for 8-bit images
            color_table_size = 256 * 4  # Each color entry is 4 bytes.
            img_data_start = 54 + color_table_size  # Start of image data after the color table.
            color_table = bmp[54:img_data_start]
            inverted_color_table = bytearray(len(color_table))
            for i in range(0, len(color_table), 4):
                # Inverting each color in the color table.
                inverted_color_table[i] = 255 - color_table[i]          # Invert Red
                inverted_color_table[i + 1] = 255 - color_table[i + 1]  # Invert Green
                inverted_color_table[i + 2] = 255 - color_table[i + 2]  # Invert Blue
            img_data = bmp[img_data_start:]
            return header + inverted_color_table + img_data
        
        elif bpp == 24 or bpp == 32:
            pixel_size = bpp // 8  # Calculating the number of bytes per pixel.
            inverted_img_data = bytearray(len(img_data))
            for row_start in range(0, len(img_data), row_size):
                row_end = row_start + (width * pixel_size)
                for i in range(row_start, row_end, pixel_size):
                    # Inverting the color of each pixel.
                    inverted_img_data[i] = 255 - img_data[i]              # Invert Blue
                    inverted_img_data[i + 1] = 255 - img_data[i + 1]      # Invert Green
                    if bpp == 24:
                        inverted_img_data[i + 2] = 255 - img_data[i + 2]  # Invert Red
                    if bpp == 32:
                        inverted_img_data[i + 2] = 255 - img_data[i + 2]  # Invert Red
                        inverted_img_data[i + 3] = img_data[i + 3]  # Preserving Alpha
            return header + inverted_img_data
        else:
            raise ValueError("Unsupported BMP format")
        
