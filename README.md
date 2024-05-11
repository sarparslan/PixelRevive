# PixelRevive

PixelRevive is a Python project that demonstrates advanced image processing techniques, including color inversion and inpainting, using Python's capabilities with minimal reliance on external libraries, specifically OpenCV for basic image handling. The project offers two main functionalities: bitwise not inversion and image inpainting.

## Features

- **Bitwise Not Operation**: Manually invert the colors of an image.
- **Inpaint Operation**: Repair damaged images using a custom implementation of the First Marching Method.

## Requirements

- Python 3.6 or higher
- OpenCV library

## Installation

To get started with PixelRevive, clone the repository:
```bash
git clone https://github.com/sarparslan/PixelRevive.git
```

## How to Use
Navigate to the project directory and execute the main script:
``` bash
cd PixelRevive
python main.py
```

## Bitwise Not Operation

### Description
The Bitwise Not operation inverts the colors of an image. This operation reads an image from the specified path, processes it to invert each pixel's color values, and saves the output in the Bitwise_Not/Bitwise_Not_Outputs directory.

### Example

**Grayscale Image**
<p align="center">
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/313c5c77-1366-483e-8983-824ce319e153" alt="Before Bitwise Not" width="45%" />
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/48efd431-21ea-419f-8b60-fa94011cd586" alt="After Bitwise Not" width="45%" />
</p>

**Color Image**
<p align="center">
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/b5dc3252-f6f7-4bd4-ae6b-40fb97465f7a" alt="Before Bitwise Not" width="45%" />
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/e23a37d9-bc85-4e81-873b-2fac951332b4" alt="After Bitwise Not" width="45%" />
</p>
<p align="center">
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/8097e430-c226-4e76-b003-17788ef851a1" alt="Before Bitwise Not" width="45%" />
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/dc5b7076-e897-4675-86ae-34f033ceb871" alt="After Bitwise Not" width="45%" />
</p>


## Inpaint Operation

### Description
The Inpaint operation repairs damaged parts of images. It starts by generating a mask from the input image to highlight areas needing repair. The application then applies the First Marching Method using this mask to restore the damaged parts, saving the restored image to the Inpaint/Inpaint_Outputs directory.


### Example

<!-- Row for Damaged Image and Mask -->
<p align="center">
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/cb9cb795-1393-4f04-bb5d-b5f6f339c245" alt="Damaged Image" width="45%" style="margin-right: 20%;" />
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/9c2b50ca-f689-4c58-9c89-5a2f21b22ef6" alt="Mask" width="45%" style="margin-left: 20%;" />
</p>

<!-- Row for Result -->
<p align="center">
  <img src="https://github.com/sarparslan/PixelRevive/assets/96438389/b618db14-4ab2-4a54-8800-cf935837b977" alt="Result" width="45%" />
</p>


## Directory Structure
- Bitwise_Not/
  - BitwiseNotOperations.py: Implements the bitwise NOT operation.
  - Bitwise_Not_Outputs/: Stores the inverted images.
    
- Inpaint/
  - InpaintOperations.py: Handles the creation of masks and the inpainting process.
  - Inpaint_Masks/: Stores the generated masks.
  - Inpaint_Outputs/: Stores the restored images.

