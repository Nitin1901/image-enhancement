# pip install imageai --upgrade

from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath('model/resnet50_coco_best_v2.1.0.h5')
detector.loadModel()

detections, _ = detector.detectObjectsFromImage(input_image=path, output_image_path=f'{path}_detected.jpg', extract_detected_objects=True)
