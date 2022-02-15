# Detecting Objects Under Extreme Illumination Conditions

With the spirit of reproducible research, this repository contains all the codes required to produce the results in the manuscript: 

> N. S. Bommi, A. L. Costuchen, and S. Dev, Detecting Objects Under Extreme Illumination Conditions, *under review*, 2022.

Please cite the above paper if you intend to use whole/part of the code. This code is only for academic and research purposes.


## Code Organization
All codes are written in `python`. 

### Code 
The script to reproduce all the figures, tables in the paper are as follows:
+ `brightness_enhancement.py`: Loads the pretrained RetinaNet model and performs brighntess enhancement on a set of images. 
+ `contrast_enhancement.py`: Performs contrast enhancement on the images specified in the path.
+ `custom_model.py`: To train the model with custom weights and images. The model can be trained from a checkpoint or from scratch.
+ `preprocess.py`: Clean the dataset by identifying images whose annotations are not valid and removing them while saving the rest in separate folders.  
+ `pretrained_model.py`: Performs object detection on a single image by using a pretrained model. 
+ `results.py`: Code used to generate various plots for comparison. 
+ `sharpness_enhancement.py`: Performs sharpness enhancement on the images specified in the path. A pretrained or a custom trained model can be used. 

### Pretrained RetinaNet model 
The model used for the experiments can be found [here](https://drive.google.com/file/d/1L4UZv-_VtWP2yWkTQZo9OIP5c4T8vl5F/view?usp=sharing).

### Dataset 
We also share the dataset used in our paper, and can be found [here](https://drive.google.com/drive/folders/1rkix-gDmcGn4f0BBbs7WQvxs27Dcbql1?usp=sharing).
