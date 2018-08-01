#!/usr/bin/python
from PIL import Image
import os, sys, random

#path = "/Users/susheelsuresh/Documents/transferLearning/tyres/good_tyre"
#outpath = "/Users/susheelsuresh/Documents/transferLearning/tyres/resized/good_tyre/"
#dirs = os.listdir(path)

## just to make sure that all the images are in one format. 

def convert2jpg(imObject):
	if imObject.mode != 'JPEG':
		return imObject.convert('RGB')
	

def resize(path,outpath):
	dirs = os.listdir(path)
	for item in dirs:
		if not item.startswith('.') and os.path.isfile(path+'/'+item):
			im = Image.open(path+'/'+item)
			f, e = os.path.splitext(path+'/'+item)
			imResize = im.resize((200,200), Image.ANTIALIAS)
			imResize = convert2jpg(imResize)
			imResize.save(outpath + item, 'JPEG', quality=90)

def createValidationSet(inDir,outDir):
	filenameList = []
	while len(filenameList) < 101 :
		filename = random.choice(os.listdir(inDir))
		if not filenameList in filenameList:
			filenameList.append(filename)
			oldFilePath = os.path.join(inDir, filename)
			newFilePath = os.path.join(outDir, filename)
			os.rename(oldFilePath,newFilePath)



#resize("/Users/susheelsuresh/Documents/transferLearning/tyres/good_tyre","/Users/susheelsuresh/Documents/transferLearning/tyres/resized/good_tyre/")

#resize("/Users/susheelsuresh/Documents/transferLearning/tyres/defective_tyre","/Users/susheelsuresh/Documents/transferLearning/tyres/resized/defective_tyre/")
resize("/Users/susheelsuresh/Documents/transferLearning/tyres/sample/","/Users/susheelsuresh/Documents/transferLearning/tyres/test/")


#createValidationSet("/Users/susheelsuresh/Documents/transferLearning/tyres/train/defective_tyre","/Users/susheelsuresh/Documents/transferLearning/tyres/val/defective_tyre")
#createValidationSet("/Users/susheelsuresh/Documents/transferLearning/tyres/train/good_tyre","/Users/susheelsuresh/Documents/transferLearning/tyres/val/good_tyre")