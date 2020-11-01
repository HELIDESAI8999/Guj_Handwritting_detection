import PIL
from PIL import Image, ImageOps
import numpy as np
import sys
import os, cv2
import csv
import pandas as pd
myDir = "..\GujOCR\Output"
#Useful function
def createFileList(myDir, format='.png'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList
columnNames = list()
for i in range(784):
    pixel = 'p'
    pixel += str(i)
    columnNames.append(pixel)
l = os.listdir("..\GujOCR\Output")
print(l)

dic = {val : idx for idx, val in enumerate(l)}
print(dic)


test_data = pd.DataFrame(columns=columnNames)
test_data.to_csv("trainset.csv", index=False)
label_count = list()


print(len(l))

for i in range(len(l)):
    mydir = 'OUTPUT/' + l[i]
    fileList = createFileList(mydir)
    for file in fileList:
        #print("hello")
        img_file = Image.open(file)  # imgfile.show()
        width, height = img_file.size
        format = img_file.format
        mode = img_file.mode

        label_count.append(dic[l[i]])
        inverted_image =img_file.convert('RGB')
        im_invert = ImageOps.invert(inverted_image)
        size = (28, 28)
        new_image = img_file.resize(size)

        img_grey = new_image.convert('L')
        value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        value = value.flatten()
        with open("trainset.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(value)


