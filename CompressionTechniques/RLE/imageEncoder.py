import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
import math

def encoderRLE(data):
    prev = data[0]
    encoded = []
    count = 1

    for i in range(1, len(data)):
        if prev == data[i]:
            count += 1
        else:
            encoded.append([hex(count)[2:], prev])
            count = 1

        if(i == len(data) - 1):
            encoded.append([hex(count)[2:], data[i]])
        prev  = data[i]

    return encoded

def encodeImage(img, save):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img = img / 255

    rows, cols = img.shape

    for i in range(0, rows):
        for j in range(0, cols):
            if img[i, j] < 0.6:
                img[i, j] = 0
            else:
                img[i, j] = 1

    f = open(save, 'w')

    for row in img:
        encodedRow = str(encoderRLE(row))
        encodedRow = encodedRow.replace('.0', '')
        encodedRow = encodedRow.replace('[','')
        encodedRow = encodedRow.replace('[[','')
        encodedRow = encodedRow.replace(' ', '')
        encodedRow = encodedRow.replace(']', '')
        encodedRow = encodedRow.replace('\'', '')
        f.write(encodedRow+'\n')
    
    f.close()

encodeImage(sys.argv[1], sys.argv[2])
