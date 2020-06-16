#Please read the README.txt file before running the code

import PIL
from PIL import Image
import pyautogui as pg

#Image should be located in the same directory as the main.py

#only .jpg image
image_name = input("Enter Image Name with extension:")

#Resizng Image, set the width of the image to basewidth and height is proportional it
basewidth = 120 #Base width, the smaller the faster
img = Image.open(image_name)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
save_name = "rez_" + image_name #Name of the resized image
img.save(save_name)
#Resized image will be saved in the source directory
print(save_name)

#Loading the Image
im = Image.open(save_name, 'r')

#Getting the pix_val of image in form of List of tuples where a tuple represents the RGB value of a pixel
pix_val = list(im.getdata())

#Getting width and height of the image
width, height = im.size

#Changing the list of tuples to list of integers where 3 values represent a pixel
pix_val_flat = [x for sets in pix_val for x in sets]

#A counter later used to change the y-axis while drawing
cnt = 0

#Code to draw
print(width, height)
pg.click(1480, 46)
pg.click(1222, 247)
pg.keyDown('p')
pg.keyUp('p')

initial_x = 1376
initial_y = 493

x = initial_x
y = initial_y

old_r = 0
old_g = 0
old_b = 0

#For loop looping through the RGB values of the image
for i in range(0, len(pix_val_flat), 3):
    pg.PAUSE = 0.001
    r = pix_val_flat[i]
    g = pix_val_flat[i+1]
    b = pix_val_flat[i+2]

    #Recording the previous values of RGB
    if (i > 0):
        old_r = pix_val_flat[i-3]
        old_g = pix_val_flat[i-2]
        old_b = pix_val_flat[i-1]
        if (old_r <=100) and (old_g <=100) and (old_b <=100):
            old_r, old_g, old_b = 0, 0, 0
        else:
            old_r, old_g, old_b = 255, 255, 255

    #For ignoring different shades of black and whites and making it quicker
    if (r <=100) and (g <=100) and (b <=100):
        r = 0
        g = 0
        b = 0
    else:
        r = 255
        g = 255
        b = 255

    #To change the primary and secondary color
    if (r != old_r) or (g != old_g) or (b!= old_b):
        pg.click(1073, 200)


    #Draws by clicking in the (x,y) coordinates
    pg.click(x, y)
    x += 1
    cnt += 1
    if (cnt == width):
        cnt = 0
        x = initial_x
        y += 1
