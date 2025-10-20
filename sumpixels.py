from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show(img):
    #img.show()
    plt.imshow(img,cmap='gray')
    plt.show()

img = Image.open("asd.png").convert("RGB") #RGBA? L - skala szarości
print("Image opened:", img.size, img.mode)

show(img)

img2 = Image.new("L", (img.width, img.height))

for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x, y))
        # MODULO 255
        s = (r+g+b) % 255

        #Odejmowanie od 255
        #if 255-r+255-g+255-b > 255:
        #    s=255
        #else:
        #    s=255-r-g-b
        
        img2.putpixel((x,y),s)

show(img2)
#img.save("img3.bmp")
