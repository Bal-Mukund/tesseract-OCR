import cv2
import pytesseract

# connecting tesseract to the environment using pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def nothing(x):       # literally does nothing
    pass
# path of the file
img = cv2.imread("C:\\Users\\balmu\\OneDrive\\Pictures\\20210621_140112 (1) (1).jpg")

img = cv2.resize(img,None,fx=0.25,fy=0.25)        # resizing the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # image to gray
# setting trackbar
cv2.namedWindow("img")
cv2.createTrackbar("trackbar","img",128,255,nothing)

while True:
    value = cv2.getTrackbarPos("trackbar","img")        # getting a integer value using trackbar

    _, threshold = cv2.threshold(gray,value,255,cv2.THRESH_BINARY)
    _, zero = cv2.threshold(gray,value,255,cv2.THRESH_TOZERO)


    cv2.imshow("img",img)
    cv2.imshow("thres",threshold)
    cv2.imshow("zero",zero)

    key = cv2.waitKey(100)
    if key == 27:
        break

cv2.destroyAllWindows()

text = pytesseract.image_to_string(zero)    # getting text from image using threshold
print(text)
