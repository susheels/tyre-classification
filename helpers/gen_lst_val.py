from os import listdir
from os.path import isfile, join

mypath_pos = '/Users/susheelsuresh/Documents/transferLearning/tyres/val/good_tyre'
mypath_neg =  '/Users/susheelsuresh/Documents/transferLearning/tyres/val/defective_tyre'
outFileName = 'tyre_val.lst'


onlyfiles_pos = [f for f in listdir(mypath_pos) if isfile(join(mypath_pos, f))]
onlyfiles_neg = [f for f in listdir(mypath_neg) if isfile(join(mypath_neg, f))]


with open(outFileName, 'w') as f:
	for i in range(0,len(onlyfiles_pos)):
		f.write(str(i+1) + "\t" + str(1) + "\t" + 'good_tyres/'+onlyfiles_pos[i] + "\n")

with open(outFileName, 'a') as f:
	for i in range(0,len(onlyfiles_neg)):
		f.write(str(i+len(onlyfiles_pos)+1) + "\t" + str(0) + "\t" + 'defective_tyres/'+onlyfiles_neg[i] + "\n")