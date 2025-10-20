from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show(img):
    #img.show()
    plt.imshow(img,cmap='gray')
    plt.show()

img = Image.new("L", (100, 100))
position = (50,50)

steps=['N','N','N','N','N','N','N','N','N','E','E','E','E','E','E','E','E','E','SW','SW','SW','SW','SW','SW']

img.putpixel(position,128)
for step in steps:
    for direction in step:
        if direction=='N':
            position=(position[0],position[1]-1)
        if direction=='E':
            position=(position[0]+1,position[1])
        if direction=='W':
            position=(position[0]-1,position[1])
        if direction=='S':
            position=(position[0],position[1]+1)

    img.putpixel(position,255)
            

show(img)

