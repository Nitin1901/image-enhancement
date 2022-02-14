# importing the libraries
import os
import time
from tqdm import tqdm
import numpy as np
from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt
from imageai.Detection import ObjectDetection

# initializing the model
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath('model/resnet50_coco_best_v2.1.0.h5')
detector.loadModel()

img_path = "data/fruits/test/images"
filenames = []

# files
for p in os.listdir(img_path):
    filenames.append(p.split('.')[0])

start = time.time()

# brightness enhancement
for filename in tqdm(filenames):

    prev = -1
    delta = 1               # enhancement factor
    step = 1                # change in enhancement factor

    while abs(step) > 0.005:

        curr = 0
        image = Image.open(f'data/fruits/test/images/{filename}.jpg')
        current_brightness = ImageEnhance.Brightness(image)
        image = current_brightness.enhance(delta)

        image = np.array(image)
        image = image[:,:,::-1]

        # detect objects 
        detections = detector.detectObjectsFromImage(input_image=image, input_type='array', output_image_path=f'{path}_contrast_detected.jpg')
        
        # average of probabilities
        for d in detections:
            curr += d['percentage_probability']
        if len(detections) > 0:
            curr = curr / len(detections)
        else:
            curr = 0
        
        # update change in enhancement factor
        if curr > prev:
            step = step / 2
        elif curr < prev:
            step = -step / 2
        else:
            break

        delta += step       # update enhancement factor

        prev = curr
        image = image[:,:,::-1]
        image = Image.fromarray(image.astype('uint8'), 'RGB')

end = time.time()
print(f'\nTime taken = {round(end - start, 3)} seconds')
