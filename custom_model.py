from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="data/fruits")

trainer.setTrainConfig(object_names_array=["apple", "banana", "orange"], batch_size=64, num_experiments=10, train_from_pretrained_model="model/pretrained-yolov3.h5")
trainer.trainModel()

