# OpenCV Hello World

讀取、顯示圖片

* cv2.imread(filename, flag)
  * filename 圖檔路徑 (str)
  * flag 讀檔模式
    * cv2.IMREAD_COLOR (預設值) 讀取圖片中 RGB 3個通道的資訊
    * cv2.IMREAD_GRAYSCALE 讀取圖片中灰階的資訊
    * cv2.IMREAD_UNCHANGED 讀取圖片中 RGBA 4個通道的資訊
* cv2.imshow(winname, mat)
  * winname 視窗名稱 (str)
  * mat 視窗顯示的圖片 (np.array)
* cv2.waitKey(delay)
  * delay 等待按鍵時間(毫秒) (int)
  * return 按下按鍵的 ASCII Code
