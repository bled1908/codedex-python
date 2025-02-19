# import imageio.v3 as iio
# import os

# # Change working directory to script's location
# # os.chdir(r"C:\Users\bled1\OneDrive\Desktop\Desktop\Courses\CodeDex\The Legend Of Python [Beginner]\Final Project\Create GIF")
# # or
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # Verify working directory
# print("Current working directory:", os.getcwd())

# # Looking for image files
# filenames = ['team-pic1.png', 'team-pic2.png']
# images = [ ]


# for filename in filenames:
#     print(f"Looking for file: {filenames}")
#     images.append(iio.imread(filename))


# iio.imwrite('team.gif', images, duration = 500, loop = 0)

# # Process images as needed
# print("Images loaded successfully!")

# import imageio.v3 as iio
# import os
# from PIL import Image
# import numpy as np

# # Change working directory to script's location
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # Verify working directory
# print("Current working directory:", os.getcwd())

# # Looking for image files
# filenames1 = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
# images = []

# # Load and resize images to the size of the first image
# first_image = Image.open(filenames1[0])
# target_size = first_image.size  # Use the size of the first image as the target size

# print(f"Resizing all images to: {target_size}")

# for filename in filenames1:
#     img = Image.open(filename)
    
#     # Convert to RGB (removes alpha channel if it exists)
#     img_rgb = img.convert('RGB')
    
#     # Resize to match the target size
#     img_resized = img_rgb.resize(target_size)
    
#     img_array = np.array(img_resized)  # Convert to numpy array
#     images.append(img_array)
#     print(f"Image '{filename}' resized to {img_array.shape}")  # Print the shape of each resized image

# # Check if all images have the same shape before writing the GIF
# for img in images:
#     if img.shape != images[0].shape:
#         print(f"Shape mismatch found: {img.shape} != {images[0].shape}")
#         break

# # Write the images to a GIF
# iio.imwrite('nyan_cat.gif', images, duration=500, loop=0)

# # Process images as needed
# print("Images loaded and GIF created successfully!")


import imageio.v3 as iio
import os
from PIL import Image
import numpy as np

# Change working directory to script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Verify working directory
print("Current working directory:", os.getcwd())

# Looking for image files
filenames1 = ['my_pic1.jpg', 'my_pic2.jpg']
images = []

# Load and resize images to the size of the first image
first_image = Image.open(filenames1[0])
target_size = first_image.size  # Use the size of the first image as the target size

print(f"Resizing all images to: {target_size}")

for filename in filenames1:
    img = Image.open(filename)
    
    # Convert to RGB (removes alpha channel if it exists)
    img_rgb = img.convert('RGB')
    
    # Resize to match the target size
    img_resized = img_rgb.resize(target_size)
    
    img_array = np.array(img_resized)  # Convert to numpy array
    images.append(img_array)
    print(f"Image '{filename}' resized to {img_array.shape}")  # Print the shape of each resized image

# Check if all images have the same shape before writing the GIF
for img in images:
    if img.shape != images[0].shape:
        print(f"Shape mismatch found: {img.shape} != {images[0].shape}")
        break

# Write the images to a GIF
iio.imwrite('my_pic.gif', images, duration=500, loop=0)

# Process images as needed
print("Images loaded and GIF created successfully!")




# run this file by going to file destination and opening cmd or terminal and changing directoty by cd address
# then run python create_gif.py
# cd "C:\Users\bled1\OneDrive\Desktop\Desktop\Courses\CodeDex\The Legend Of Python [Beginner]\Final Project\Create GIF"
# python create_gif.py

# This will create a gif file named team.gif in the same directory as the images

# or if you want to run this file in vs code then run this file
# import imageio.v3 as iio

# filenames = [
#     r"C:\Users\bled1\OneDrive\Desktop\Desktop\Courses\CodeDex\The Legend Of Python [Beginner]\Final Project\Create GIF\team-pic1.png",
#     r"C:\Users\bled1\OneDrive\Desktop\Desktop\Courses\CodeDex\The Legend Of Python [Beginner]\Final Project\Create GIF\team-pic2.png"
# ]
# images = []

# print(f"Looking for files: {filenames}")

# for filename in filenames:
#     images.append(iio.imread(filename))

# iio.imwrite(r"C:\Users\bled1\OneDrive\Desktop\Desktop\Courses\CodeDex\The Legend Of Python [Beginner]\Final Project\Create GIF\team.gif", images, duration=500, loop=0)
