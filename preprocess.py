import os
import shutil
import xml.etree.ElementTree as ETree

from zipfile import ZipFile

with ZipFile('data/fruits.zip', 'r') as z:
    z.extractall('data/fruits')
    
##########################################################################
#####################              TEST              #####################
##########################################################################
    
path = "data/fruits/test_zip/test"

for ann in os.listdir(path):
    temp = ann.split('.')
    if temp[-1] == 'xml':
        xmldata = os.path.join(path, ann)
        prstree = ETree.parse(xmldata)
        root = prstree.getroot()
        for dimension in root.iter('size'):
            width = dimension.find('width').text
            height = dimension.find('height').text
            if width == '0' or height == '0':
                print(temp)
                os.remove(os.path.join(path, ann))
                os.remove(os.path.join(path, temp[0]+'.jpg'))
                
for img in os.listdir(path):
    if img.split('.')[-1] == 'jpg':
        shutil.move(os.path.join(path, img), f"data/fruits/test/images/{img}")

for ann in os.listdir(path):
    if ann.split('.')[-1] == 'xml':
        shutil.move(os.path.join(path, ann), f"data/fruits/test/annotations/{ann}")
        
###########################################################################
#####################              TRAIN              #####################
###########################################################################
                
path = "data/fruits/train_zip/train"

for ann in os.listdir(path):
    temp = ann.split('.')
    if temp[-1] == 'xml':
        xmldata = os.path.join(path, ann)
        prstree = ETree.parse(xmldata)
        root = prstree.getroot()
        for dimension in root.iter('size'):
            width = dimension.find('width').text
            height = dimension.find('height').text
            print(width, height)
            if width == '0' or height == '0':
                print(temp)
                os.remove(os.path.join(path, ann))
                os.remove(os.path.join(path, temp[0]+'.jpg'))
                
for img in os.listdir(path):
    if img.split('.')[-1] == 'jpg':
        shutil.move(os.path.join(path, img), f"data/fruits/train/images/{img}")

for ann in os.listdir(path):
    if ann.split('.')[-1] == 'xml':
        shutil.move(os.path.join(path, ann), f"data/fruits/train/annotations/{ann}")
        
