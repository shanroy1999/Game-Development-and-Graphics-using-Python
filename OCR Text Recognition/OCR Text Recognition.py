import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\text1.jpg")
print(img.shape)
height, width, _ = img.shape

#Send image to API in bytes
roi = img[0:height, 400: width]
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api, files={r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\kungfu.jpg":file_bytes},
              data={"apikey":"9acef02e7088957"})
result = result.content.decode()
result = json.loads(result)
print(result)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

cv2.imshow("ROI",roi)
cv2.imshow("Text",img)
cv2.waitKey(0)

img = cv2.imread(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\kungfu.jpg")
print(img.shape)
height, width, _ = img.shape

#Send image to API in bytes
roi = img
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api, files={r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\OCR Text Recognition\kungfu.jpg":file_bytes},
              data={"apikey":"9acef02e7088957",
                    "language": "cht"})
result = result.content.decode()
result = json.loads(result)
print(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(parsed_results)
print(text_detected)

cv2.imshow("ROI",roi)
cv2.imshow("Text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()