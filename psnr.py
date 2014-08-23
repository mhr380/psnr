import cv2
import math
import numpy as np

refName = "ref.png"
imgName = "ref.png"

ref = cv2.imread(refName,0)
img = cv2.imread(imgName,0)

height = 300
width  = 400

mse = 0 
for y in range(height):
    for x in range(width):
        dif = ref[y, x] - img[y, x]
        mse = mse + math.pow(dif , 2) / (height * width)

psnr = 10 * math.log(pow(255, 2) / mse, 10)

print "PSNR:",psnr
