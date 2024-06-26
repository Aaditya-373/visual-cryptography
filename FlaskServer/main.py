from PIL import Image,ImageOps
import numpy as np
import random
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2 as cv
import os
from PIL import Image, ImageFilter


def generate_shares(original_image):
    share1 = original_image.copy()
    share2 = original_image.copy()

    width, height = original_image.size
    for i in range(0, width, 2):
        for j in range(0, height, 2):
            if j+1 <height and i+1<width:
           
                pixel_value = original_image.getpixel((i, j))
                if pixel_value == 0: 
                    config_index = random.randint(0, 5)  
                    if config_index == 0:  
                        share1.putpixel((i, j), 0)  
                        share1.putpixel((i+1, j), 255)  
                        share1.putpixel((i, j+1), 0)  
                        share1.putpixel((i+1, j+1), 255) 

                        share2.putpixel((i, j), 255)  
                        share2.putpixel((i+1, j), 0) 
                        share2.putpixel((i, j+1), 255) 
                        share2.putpixel((i+1, j+1), 0)  
                    elif config_index == 1:  
                        share1.putpixel((i, j), 0) 
                        share1.putpixel((i+1, j), 0) 
                        share1.putpixel((i, j+1), 255)  
                        share1.putpixel((i+1, j+1), 255) 
                        
                        share2.putpixel((i, j), 255)  
                        share2.putpixel((i+1, j), 255) 
                        share2.putpixel((i, j+1), 0) 
                        share2.putpixel((i+1, j+1), 0)  
                    elif config_index == 2:  
                        share1.putpixel((i, j), 255)  
                        share1.putpixel((i+1, j), 255) 
                        share1.putpixel((i, j+1), 0)  
                        share1.putpixel((i+1, j+1), 0)  

                        share2.putpixel((i, j), 0)  
                        share2.putpixel((i+1, j), 0) 
                        share2.putpixel((i, j+1), 255)  
                        share2.putpixel((i+1, j+1), 255) 
                    elif config_index == 3:  
                        share1.putpixel((i, j), 255) 
                        share1.putpixel((i+1, j), 0)  
                        share1.putpixel((i, j+1), 255) 
                        share1.putpixel((i+1, j+1), 0) 

                        share2.putpixel((i, j), 0)  
                        share2.putpixel((i+1, j), 255)  
                        share2.putpixel((i, j+1), 0)  
                        share2.putpixel((i+1, j+1), 255)  
                    elif config_index == 4:  
                        share1.putpixel((i, j), 0)  
                        share1.putpixel((i+1, j), 255)  
                        share1.putpixel((i, j+1), 255)  
                        share1.putpixel((i+1, j+1), 0)  

                        share2.putpixel((i, j), 255)  
                        share2.putpixel((i+1, j), 0)  
                        share2.putpixel((i, j+1), 0)  
                        share2.putpixel((i+1, j+1), 255) 
                    elif config_index == 5:  
                        share1.putpixel((i, j), 255)  
                        share1.putpixel((i+1, j), 0) 
                        share1.putpixel((i, j+1), 0)  
                        share1.putpixel((i+1, j+1), 255)  

                        share2.putpixel((i, j), 0)  
                        share2.putpixel((i+1, j), 255)  
                        share2.putpixel((i, j+1), 255) 
                        share2.putpixel((i+1, j+1), 0)  
                else:
                    if i+1<width and j+1<height:  
                        config_index = random.randint(0, 5)  
                        if config_index == 0: 
                            share1.putpixel((i, j), 0) 
                            share1.putpixel((i+1, j), 255)  
                            share1.putpixel((i, j+1), 0)  
                            share1.putpixel((i+1, j+1), 255) 

                            share2.putpixel((i, j), 0) 
                            share2.putpixel((i+1, j), 255)  
                            share2.putpixel((i, j+1), 0)  
                            share2.putpixel((i+1, j+1), 255)  
                        elif config_index == 1:  
                            share1.putpixel((i, j), 0) 
                            share1.putpixel((i+1, j), 0) 
                            share1.putpixel((i, j+1), 255) 
                            share1.putpixel((i+1, j+1), 255)  

                            share2.putpixel((i, j), 0)  
                            share2.putpixel((i+1, j), 0)  
                            share2.putpixel((i, j+1), 255)  
                            share2.putpixel((i+1, j+1), 255)  
                        elif config_index == 2:  
                            share1.putpixel((i, j), 255)  
                            share1.putpixel((i+1, j), 255)  
                            share1.putpixel((i, j+1), 0)  
                            share1.putpixel((i+1, j+1), 0)  

                            share2.putpixel((i, j), 255) 
                            share2.putpixel((i+1, j),255) 
                            share2.putpixel((i, j+1), 0)  
                            share2.putpixel((i+1, j+1), 0)  
                        elif config_index == 3:  
                            share1.putpixel((i, j), 255) 
                            share1.putpixel((i+1, j), 0) 
                            share1.putpixel((i, j+1),255)  
                            share1.putpixel((i+1, j+1), 0)  

                            share2.putpixel((i, j), 255) 
                            share2.putpixel((i+1, j), 0)  
                            share2.putpixel((i, j+1), 255) 
                            share2.putpixel((i+1, j+1), 0) 
                        elif config_index == 4:  
                            share1.putpixel((i, j), 0)  
                            share1.putpixel((i+1, j), 255)  
                            share1.putpixel((i, j+1), 255)  
                            share1.putpixel((i+1, j+1), 0)  

                            share2.putpixel((i, j), 0) 
                            share2.putpixel((i+1, j), 255) 
                            share2.putpixel((i, j+1), 255)  
                            share2.putpixel((i+1, j+1), 0)  
                        elif config_index == 5: 
                            share1.putpixel((i, j), 255)  
                            share1.putpixel((i+1, j), 0)  
                            share1.putpixel((i, j+1), 0)  
                            share1.putpixel((i+1, j+1), 255) 

                            share2.putpixel((i, j), 255)  
                            share2.putpixel((i+1, j), 0)  
                            share2.putpixel((i, j+1), 0)  
                            share2.putpixel((i+1, j+1), 255)  
    return share1, share2



def convert_to_binary(image, threshold=128):
    if image.mode != 'L':
        image = image.convert('L')
    binary_image = ImageOps.posterize(image, 1)
    return binary_image

def superimpose_shares(share1, share2):
    # Initialize the reconstructed image
    width,height = share1.size
    reconstructed_image = Image.new("L",(width,height))
    # Iterate through each pixel in the shares and combine them
    for i in range(width):
        for j in range(height):
            # Get pixel values from both shares
            pixel_share1 = share1.getpixel((i, j))
            pixel_share2 = share2.getpixel((i, j))
            reconstructed_pixel = min(pixel_share1,pixel_share2)
            reconstructed_image.putpixel((i, j),reconstructed_pixel)
    return reconstructed_image


def invert_image(image):
    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Invert the colors by subtracting each pixel value from 255
    inverted_array = 255 - image_array

    # Convert the inverted array back to an image
    inverted_image = Image.fromarray(inverted_array)

    return inverted_image


def assess_validity(reconstructed_image, original_image, threshold):
    reconstructed_array = np.array(reconstructed_image)
    original_array = np.array(original_image)
    similarity_score = ssim(reconstructed_array, original_array)
    print(similarity_score)
    if similarity_score > threshold:
        return True
    else:
        return False




def register(userId):
    original_image_path="./"+userId+"/original.png"
    original_image = convert_to_binary(Image.open(original_image_path))
    share1, share2 = generate_shares(original_image)
    
    original_image = Image.open(original_image_path)
    original_image = invert_image(original_image)
    original_image.save(original_image_path)
    share1.save(os.path.join(userId, "share1.png"))
    share2.save(os.path.join(userId, "share2.png"))

def login(userId):
    try:
        original_image_path="./"+userId+"/original.png"
        share1_path="./"+userId+"/share1.png"
        share2_path="./"+userId+"/share2.png"
        share1 = Image.open(share1_path).convert('L')
        share2 = Image.open(share2_path).convert('L')
        
        original_image=Image.open(original_image_path)
        original_image=invert_image(original_image)
        original_image = convert_to_binary(original_image)
        reconstructed_image = superimpose_shares(share1, share2)
        if assess_validity(reconstructed_image, original_image, threshold=0.01):
            return True
        else:
            return False
    except Exception as e :
        return False

