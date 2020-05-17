import numpy as np
import imageio
import scipy.ndimage
import cv2

img = r"C:\Users\Lenovo\Desktop\New folder\Passport Photo.jpg"

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front, back):
    result = front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

scan = imageio.imread(img)
gray = grayscale(scan)
i = 255-gray
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
res = dodge(blur,gray)

cv2.imwrite(r'C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Passport_Sketch.jpg', res)
