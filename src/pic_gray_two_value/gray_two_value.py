# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''
import cv2


img = cv2.imread('4.jpg')

# #灰度
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('4_gray.jpg',img)

#二值化
cv2.threshold(img,50,255,cv2.THRESH_BINARY)
cv2.imwrite('4_two_value.jpg',img)