"""
This script will take all the images in the OLD_DIR directory and resize
them to be square with a background of the TILE_IMAGE. If TILE_IMAGE is
smaller than the resized image it will be tiled across the background.
The new images will be saved in the NEW_DIR directory with the same
filename and extension of the old image.
"""

import argparse
import os
from PIL import Image

DEFAULT_OLD_DIR = "images/old"
DEFAULT_NEW_DIR = "images/new"
DEFAULT_TILE_IMAGE = "images/tile.jpg"

# Parse the command line arguments
parser = argparse.ArgumentParser(description=__doc__, epilog="For more information see: https://github.com/jwolff52/square-images")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument("-o", "--old", help="The directory containing the old images", default=DEFAULT_OLD_DIR)
parser.add_argument("-n", "--new", help="The directory to save the new images", default=DEFAULT_NEW_DIR)
parser.add_argument("-t", "--tile", help="The tile image to use as the background", default=DEFAULT_TILE_IMAGE)
args = parser.parse_args()

OLD_DIR = args.old
NEW_DIR = args.new
TILE_IMAGE = args.tile

# Get a list of all the images in the old directory
image_names = os.listdir(OLD_DIR)
# Load the tile image
tile_image = Image.open(TILE_IMAGE)

print(f"Found {len(image_names)} images in {OLD_DIR} directory")

for f in image_names:
    print(f"Processing {f}...")
    try:
      image = Image.open(f"{OLD_DIR}/{f}")
    except IOError:
       print(f"Not an image file: {f}")
       continue
    old_image_mode = image.mode
    if args.verbose:
      print(f"Original image mode: {old_image_mode}")
    width, height = image.size
    if args.verbose:
      print(f"Original image size: {width}x{height}")
    max_dimension = max(width, height)
    if args.verbose:
      print(f"Now resizing to {max_dimension}x{max_dimension}")
    square_image = Image.new("RGBA", (max_dimension, max_dimension))
    square_image.paste(image, (int((max_dimension - width) / 2), int((max_dimension - height) / 2)))
    background = Image.new("RGBA", (max_dimension, max_dimension))
    if args.verbose:
      print(f"Tiling tile image on background {TILE_IMAGE}...")
    for x in range(0, max_dimension, tile_image.width):
        for y in range(0, max_dimension, tile_image.height):
            background.paste(tile_image, (x, y))
    if args.verbose:
       print("Combining images...")
    final_image = Image.alpha_composite(background, square_image)
    if (old_image_mode != "RGBA"):
        if args.verbose:
           print(f"Converting to {old_image_mode}...")
        final_image = final_image.convert(old_image_mode)
    if args.verbose:
       print(f"Saving to {NEW_DIR}/{f}...")
    final_image.save(f"{NEW_DIR}/{f}")

print("Done!")