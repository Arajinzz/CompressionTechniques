import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

def decodeImage(encoded_img):
    f = open(encoded_img, 'r')
    all_lines = f.readlines()

    img = []

    for row in all_lines:
        row = row.split(',')
        rowDecoded = []
        for i in range(0, len(row), 2):
            rep = int(row[i], 16)
            info = row[i+1]
            for j in range(0, rep):
                rowDecoded.append(float(info)*255)

        img.append(rowDecoded)

    img = np.array(img)

    return img


img = decodeImage(sys.argv[1])
cv2.imshow('win', img)

cv2.waitKey(0)
cv2.destroyAllWindows()