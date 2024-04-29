

def read_bmp(file_path):
    # Opening the file in binary read mode and read the entire content into bmp
    with open(file_path, 'rb') as f:
        bmp = f.read()
    return bmp

def write_bmp(file_path, data):
    # Opening the file in binary write mode and write the modified data to a new file
    with open(file_path, 'wb') as f:
        f.write(data)

def invert_color_table(bmp):
    header = bmp[:54]  # BMP header which is usually 54 bytes
    color_table_size = 256 * 4  # Size of the color table (256 colors, each 4 bytes RGBA)
    img_data_start = 54 + color_table_size  # Calculating the start of image data

    color_table = bmp[54:img_data_start]  # Extracting the color table from the BMP
    img_data = bmp[img_data_start:]  # Extracting the image data

    # Creating a new bytearray for the inverted color table
    inverted_color_table = bytearray(len(color_table))
    for i in range(0, len(color_table), 4):
        # Inverting each color component in the color table
        inverted_color_table[i] = 255 - color_table[i]  # Invert Red
        inverted_color_table[i + 1] = 255 - color_table[i + 1]  # Invert Green
        inverted_color_table[i + 2] = 255 - color_table[i + 2]  # Invert Blue

    # Returning the modified BMP data with the inverted color table and original image data
    return header + inverted_color_table + img_data


image_path = 'lena.bmp'
output_path = 'lena2.bmp'

# Reading the original BMP file
bmp_data = read_bmp(image_path)

# Inverting the color table in the BMP data
inverted_bmp = invert_color_table(bmp_data)

# Writing the modified BMP data to a new file
write_bmp(output_path, inverted_bmp)
