import cv2 as cv
#Reading images
img=cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat',img)


cv.waitKey(0)

#----215 Assertion failed means file could not be found at specified location----

#Reading videos
capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

