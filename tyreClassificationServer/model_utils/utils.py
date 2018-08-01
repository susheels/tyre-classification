#!/usr/bin/python
from PIL import Image
import os, sys, random

## to make sure that all the images are in one format. 
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


#resize("./upload","./tyres/resized/")


