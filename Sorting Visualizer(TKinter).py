import time
from tkinter import *
from tkinter import ttk
import random

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)

def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)
    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]
    leftIdx = rightIdx = 0
    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]
    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    # swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick)

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    drawData(data, ['red' for x in range(len(data))])  # ['red', 'red' ,....]

def StartAlgorithm():
    global data
    if not data: return
    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    drawData(data, ['green' for x in range(len(data))])

def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                   label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
