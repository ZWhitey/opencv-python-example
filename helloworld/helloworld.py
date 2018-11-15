import numpy as np
import cv2

myimg = 'lenna.png'
def main():
    raw_img = cv2.imread(myimg) #讀圖片彩色資訊
    gray_img = cv2.imread(myimg, cv2.IMREAD_GRAYSCALE) #讀圖片灰階資訊
    while True:
        cv2.imshow('OpenCV Color Image', raw_img) #顯示彩色圖片
        cv2.imshow('OpenCV Gray Image', gray_img) #顯示灰階圖片
        if cv2.waitKey(1) == ord('q'): #按q關閉視窗
            cv2.imwrite('gary.jpg', gray_img) #儲存灰階圖片
            break

if __name__ == "__main__":
    main()