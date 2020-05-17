import cv2
import pytesseract

#Install Tesseract-OCR and pytesseraact
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\text.jpg")
text = pytesseract.image_to_string(image)
print(text+"\n")
cv2.imshow("Text",image)
cv2.waitKey(0)


image1 = cv2.imread(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\book_page.jpg")
image1 = cv2.resize(image1, None, fx=0.4, fy=0.4)
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
adapt_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config1 = "--psm 0"     #Orientation and Script Detection only
config2 = "--psm 1"     #Auto page segmentation with OSD
config3 = "--psm 2"     #Auto page segmentation, no OSD, no OSR
config4 = "--psm 3"     #Fully auto segementation, no OSD               #Default
config5 = "--psm 4"     #Assume single column of text of variable sizes
config6 = "--psm 5"     #Assume single uniform block of vertically alligned text
config7 = "--psm 6"     #Assume single uniform block of text
config8 = "--psm 7"     #Treat image as single text line
config9 = "--psm 8"     #Treat image as single word
config10 = "--psm 9"    #Treat image as single word in a Circle
config11 = "--psm 10"   #Treat image as single character

text1 = pytesseract.image_to_string(gray)
text2 = pytesseract.image_to_string(adapt_thresh, config=config5)
print("Grayscale\n")
print(text1+"\n")

print("Adaptive Threshold\n")
print(text2)

cv2.imshow("Gray",gray)
cv2.imshow("Adaptive Threshold",adapt_thresh)
#cv2.imshow("Actual Text",image1)
cv2.waitKey(0)

image2 = cv2.imread(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\chinese_text.jpg")
image2 = cv2.resize(image2, None, fx=0.4, fy=0.4)
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
adapt_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)


text2 = pytesseract.image_to_string(adapt_thresh, config=config5, lang="chi_sim")
print(text2)

cv2.imshow("Gray",gray)
cv2.imshow("Adaptive Threshold",adapt_thresh)
cv2.imshow("Chinese",image2)

cv2.waitKey(0)
