from PIL import Image
import numpy as np
  

INPUT_FILENAME = 'your image name'              #Input Image filename
OUTPUT_FILENAME = 'output.hex'               #Output Hex filename

imgFile = Image.open(INPUT_FILENAME)        #BMP image file open
img_array = np.asarray(imgFile)             #Converting image to numpy array

shape = img_array.shape                     #Shape of the image  (h,w,c)
height, width, color = shape

#Converting the multi dimensional array into 1D list
#This is done in Reverse order for convenient of fpga
pixvals = []
for h in range(height-1,-1,-1):          
    for w in range(width):          
        for c in range(color):        
            pixvals.append(img_array[h][w][c])

length = len(pixvals)

print("FileName: {}\nHeight: {} px\nWidth: {} px\nColors: {}\nHex Data Length: {}".format(INPUT_FILENAME ,height,width,color,length))

#Writing the values to a hex file

print("\nFile Conversion Began.....")

OUTPUT_FILENAME = 'image.hex'
with open(OUTPUT_FILENAME,'w') as f:
    for value in range(length):
        fval = hex(pixvals[value])[2:]
        f.write(fval+'\n')

print("Hex File created succesfully")