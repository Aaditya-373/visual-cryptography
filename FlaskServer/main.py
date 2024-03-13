from PIL import Image,ImageOps
import numpy as np
import random
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2 as cv
import os
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


def medianFiltering(img):
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgFilter = cv.medianBlur(imgRGB, 5)
    filtered_image = Image.fromarray(cv.cvtColor(imgFilter, cv.COLOR_RGB2BGR))
    return filtered_image


def assess_validity(reconstructed_image, original_image, threshold):
    reconstructed_array = np.array(reconstructed_image)
    original_array = np.array(original_image)

    # Compare combined image with a template/reference image
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
    share1.save(os.path.join(userId, "share1.png"))
    share2.save(os.path.join(userId, "share2.png"))

def login(userId):
    original_image_path="./"+userId+"/original.png"
    share1_path="./"+userId+"/share1.png"
    share2_path="./"+userId+"/share2.png"
    # Load images and explicitly convert them to PIL.Image.Image
    share1 = Image.open(share1_path).convert('L')
    share2 = Image.open(share2_path).convert('L')
    original_image = convert_to_binary(Image.open(original_image_path))
    reconstructed_image = superimpose_shares(share1, share2)
    if assess_validity(reconstructed_image, original_image, threshold=0.1):
        return True
    else:
        return False


