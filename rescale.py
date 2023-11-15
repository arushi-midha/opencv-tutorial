import cv2 as cv
#Reading images
img=cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('image',resized_image)
cv.waitKey(0)


capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()

    frame_resized=rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows