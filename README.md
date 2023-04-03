# square-images

This script will take all the images in the OLD_DIR directory and resize 
them to be square with a background of the TILE_IMAGE. If TILE_IMAGE is 
smaller than the resized image it will be tiled across the background. 
The new images will be saved in the NEW_DIR directory with the same 
filename and extension of the old image.

## Why?
I am getting married later this year and we are using [Zola](https://zola.com) for our wedding's website. It has been super helpful, but they make a really silly decision when you upload photos to put in a gallery. When you upload an image they first take the image and make it a square, which makes it easier to lay them out I guess, but then they add a *white background* to the image to fill in the empty space...why?! *Some* of their website palettes have white as the background color, but it is far from every palette. Initially I was going to fix all of the pictures by hand, adding tiles of the image used for the websites background, but that seemed like it would have been more work than writing this script because each of the original images was slightly different for its largest dimension. Hopefully this will help others down the line, we pay our photographers to take these amazing pictures and it is a shame to treat them the way Zola's upload system does.

## Installation:

1. Clone the repository: `git clone https://github.com/jwolff52/square-images`
2. Enter directory: `cd square-images`
3. Install virtual environment: `python -m venv .venv`
4. Source the virtual environment: `source .venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`

## Usage:
```
python App.py [-h] [-v] [-o OLD] [-n NEW] [-t TILE]

options:
  -h, --help            show this help message and exit
  -v, --verbose         Increase output verbosity (default: False)
  -o OLD, --old OLD     The directory containing the old images (default: images/old)
  -n NEW, --new NEW     The directory to save the new images (default: images/new)
  -t TILE, --tile TILE  The tile image to use as the background (default: images/tile.jpg)
```
