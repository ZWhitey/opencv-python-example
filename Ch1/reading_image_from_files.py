import cv2
import numpy as np

img_path = '../data/Lena.png'

def main():
    img = cv2.imread(img_path)
    print('Color Image')
    print('Image Shape : ',img.shape)
    print('Image Data Type : ',img.dtype)

    gray_img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    print('Gray Image')
    print('Image Shape : ',gray_img.shape)
    print('Image Data Type : ',gray_img.dtype)

if __name__ == "__main__":
    main()