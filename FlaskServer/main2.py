from PIL import Image,ImageOps
import numpy as np
import random
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2 as cv

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
    share1.show()
    share2.show()
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

            # Combine them to reconstruct the original pixel value
            # reconstructed_pixel =min( pixel_share1,pixel_share2)
            reconstructed_pixel = min(pixel_share1,pixel_share2)

            # Update the reconstructed image accordingly
            reconstructed_image.putpixel((i, j),reconstructed_pixel)

    return reconstructed_image


def medianFiltering(img):
    # Convert the image to RGB format (if it's not already)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # Apply median filtering with a kernel size of 5x5
    imgFilter = cv.medianBlur(imgRGB, 5)
    
    # Convert the filtered image back to PIL format
    filtered_image = Image.fromarray(cv.cvtColor(imgFilter, cv.COLOR_RGB2BGR))
    
    return filtered_image

original_image_path = "tesla.jpg"
source_image = Image.open((original_image_path))
original_image = convert_to_binary(Image.open(original_image_path))
share1, share2 = generate_shares(original_image)
reconstructed_image = superimpose_shares(share1, share2)
reconstructed_image_noiseless = medianFiltering(np.array(reconstructed_image))

# Show the noise-reduced reconstructed image
reconstructed_image.show()
original_image.show()
reconstructed_image_noiseless.show()

def assess_validity(reconstructed_image, original_image, threshold):
    reconstructed_array = np.array(reconstructed_image)
    original_array = np.array(original_image)

    # Compare combined image with a template/reference image
    similarity_score = ssim(reconstructed_array, original_array)
    
    if similarity_score > threshold:
        return True
    else:
        return False

threshold = 0.475 
if assess_validity(reconstructed_image, original_image, threshold):
    print("Valid image.")
else:
    print("Invalid image.")
    