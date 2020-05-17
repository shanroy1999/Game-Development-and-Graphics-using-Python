import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(190, 250):
        for j in range(397, 457):
            if data[i, j] > 70:
                hit("up")
                return

    """for i in range(190, 220):
        for j in range(282, 397):
            if data[i, j] > 70:
                hit("down")
                return
    return False"""

if __name__=="__main__":
    time.sleep(2)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert('L')  # Convert to grayscale
        data = image.load()
        isCollide(data)
        #print(asarray(image))               #Convert image to array

        """#For Cactus
        for i in range(190, 250):
            for j in range(397, 457):
                data[i, j] = 0
        #For Bird
        for i in range(190, 220):
            for j in range(282, 397):
                data[i, j] = 71
        image.show()
        break"""