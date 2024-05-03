# PixelRevive

PixelRevive is a Python project that implements OpenCV's `cv2.bitwise_not` function without using any external libraries. The application allows you to invert the colors of a BMP image and save the result.

## Features
- Invert the colors of an image without external libraries.
- Accepts a BMP file path from the user.
- Saves the processed image to the `Bitwise_Not/Bitwise_Not_Outputs` folder.

## Requirements

- Python 3.6 or higher

  
## How to Use
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/sarparslan/PixelRevive.git
2. Navigate to the project directory:
   ```bash
    cd PixelRevive
3. Run the application:
   ```bash
    python main.py

## Structure

Bitwise_Not/
BitwiseNotOperations.py: Contains functions for reading, processing (bitwise NOT), and writing BMP images.
Bitwise_Not_Outputs/: Stores the processed BMP images.