import cv2
import numpy as np
import qrcode

#mg=qrcode.make("1111,2222,3333,4444,5555,6666,7777,8888,9999")
#img.save('QR')
img = cv2.imread('QR')
qr = cv2.QRCodeDetector()
output_image = img.copy()
data, points, straight_qrcode = qr.detectAndDecode(img)
for i in range(4):
    cv2.line(output_image, tuple(points[0][i]), tuple(points[0][(i + 1) % len(points[0])]), (0, 0, 255), 4)
cv2.imshow('QR',output_image)
# 画像表示
#cv2.imshow('cv2', img)
cv2.waitKey(0)
print('データ:', data)
print("バージョン：", ((straight_qrcode.shape[0] - 21) / 4) + 1)