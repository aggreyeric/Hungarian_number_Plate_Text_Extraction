import re
import numpy as np
import cv2
import  pytesseract




def totext(path):
    top = int(160)  # shape[0] = rows
    bottom = top
    left = int(160)  # shape[1] = cols
    right = left
    image=cv2.imread(path,0)
    m = np.load('dim.npy')
    crop_img = image[m[0]-4: m[1]-5, m[2]-7:m[3]-7 ]
    (thresh, img) = cv2.threshold(crop_img, 78, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=255)
    text1 = pytesseract.image_to_string(img)
    cv2.imwrite("k.jpg", img)
    return text1

