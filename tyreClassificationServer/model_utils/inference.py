from __future__ import print_function, division
import torch
import torchvision
from torchvision import datasets, models, transforms
from PIL import Image
from torch.autograd import Variable
import time
import os
import copy

class_names = ['Defective Tyre', 'Good Tyre']

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def infer_model(model, filename):
    loader = transforms.Compose([transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    def image_loader(image_name):
        """load image, returns tensor"""
        image = Image.open(image_name)
        image = loader(image).float()
        image = Variable(image, requires_grad=True) #[3,224,224]
        # resnet requires input in below format.
        image = image.unsqueeze(0) # done to add a extra dimension for image tensor. [1,3,224,244]
        return image  #assumes that you're using 

    image = image_loader(filename)
    was_training = model.training
    model.eval()

    with torch.no_grad():
        outputs = model(image)
        _, preds = torch.max(outputs, 1)
        print(class_names[preds[0]])
        return class_names[preds[0]]    

def infer(modelFileName,filenames):
    model = torch.load(modelFileName)
    out = []
    for filename in filenames:
        out.append(infer_model(model,filename))
    return out

#infer(modelFileName='model_conv_tyres.pt',filenames=['/Users/susheelsuresh/Documents/transferLearning/flask-fileupload-ajax-example-master/tyres/resized/g2.jpg',])




