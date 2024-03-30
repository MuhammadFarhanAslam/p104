import cv2
img = cv2.imread("solar_system.jpg")

cv2.putText(img,  
           "Sun",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (80, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (160, 160),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (250, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (400, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Jupiter",
           (600, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (820, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Uranus",
           (920, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (1120, 120),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )


cv2.imwrite("solar_system_withname.jpg", img)
cv2.imshow("output", img)
cv2.waitKey(0)