
# coding: utf-8

# In[ ]:


import PIL
import fnmatch
from resizeimage import resizeimage
import os
import glob
import cv2
from PIL import Image



# Set variables value:


# Set images path

path = 'images/*'



# Set images scaling variables

# Set image file formats

image_formats = ['png', 'jpg', 'gif'] 



# Image width and height  

width = 4000

height = 4000

# Image filter type
#filters = [PIL.Image.NEAREST, PIL.Image.BILINEAR, PIL.Image.BICUBIC,  PIL.Image.ANTIALIAS]

filter_name = [PIL.Image.ANTIALIAS]

# to resize image in gray scale

grey_scale = False

#######################################################



# def Image filteration to enhance its resolution

def image_filteration(one_image, width, height, grey_scale):
            
    #im = Image.open(one_image)
    
    img = one_image.thumbnail((width, height), filter_name)
    
    img = one_image

    if grey_scale is True:
        
        img = img.convert('L')  # to resize image in gray scale
        
    # saving image  after filteration

    #img.save( one_image ,image.format, quality=100) 
    return img



# def Image resize function scaling an image  

def image_resize (images_list, width, height, grey_scale):
    
    
    
     # iterating over all images from a given folder
    
    for one_image in images_list:

        

        # image scaling 
        
        with open(one_image, 'r+b') as f:
            
            with Image.open(f) as image:
                
                cover = resizeimage.resize_cover(image, [width, height], validate=False)
                
                # image filteration
                
                new_image = image_filteration( cover, width, height )
               
            # saving image  after scaling
            
                cover.save(new_image, image.format, quality=100)

                
# def get_all_images function extract all images from existing foulder to run the image_resize and image_filteration functions         
def get_all_images(path, width, height, image_formatsm ,grey_scale): 
    
    # get all images_folder's name  in directory
    
    images_folder = glob.glob(path)
   


    # reading all images from a given folders

    for folder in images_folder:
    
    images_list = []
    
    [images_list.extend(glob.glob(folder +'/'+ '*.' + e)) for e in image_formats]
    
    image_resize (images_list, width, height, grey_scale)

