import os
from PIL import Image
from array import *
from random import shuffle

# Load from and save to
Names = [['/media/smehtani83/41D913FC29D62F2B/pdfs/study/Machine Learning/IIT delhi/Sigtuple_Attacks/wbc_dataset/images','wbc_train']]

for name in Names:
	
	#data_image = array('B')
	#data_label = array('B')
	data_image1 = array('B')
	data_label1 = array('B')
	data_image2 = array('B')
	data_label2 = array('B')
	data_image3 = array('B')
	data_label3 = array('B')
	
	


	FileList = []
	for dirname in os.listdir(name[0])[1:]: # [1:] Excludes .DS_Store from Mac OS
		#print(dirname)
		path = os.path.join(name[0],dirname)
		#print(path)
		FileList.append(path)

	shuffle(FileList) # Usefull for further segmenting the validation set
	print('a')
	i=0
	for filename in FileList[0:15000]:

		#label = int(filename.split('/')[2])
		i=i+1
		Im = Image.open(filename)
		print(i)
		pixel = Im.load()

		width, height = Im.size

		for x in range(0,width):
			for y in range(0,height):
				data_image1.append((pixel[y,x])[0])
				data_image2.append((pixel[y,x])[1])
				data_image3.append((pixel[y,x])[2])
				
				#data_label.append(pixel[y,x])
		 # labels start (one unsigned byte each)

	hexval = "{0:#0{1}x}".format(len(FileList),6) # number of files in HEX

	# header for label array
	print('b')
	#header = array('B')
	header = array("B")
	
	header.extend([0,0,8,1,0,0])
	header.append(int('0x'+hexval[2:][:2],16))
	header.append(int('0x'+hexval[2:][2:],16))
	
	#data_label = header + data_label

	# additional header for images array
	
	if max([width,height]) <= 256:
		header.extend([0,0,0,width,0,0,0,height])
	else:
		raise ValueError('Image exceeds maximum size: 256x256 pixels');

	header[3] = 3 # Changing MSB for image data (0x00000803)
	#data_label = header + data_label	
	data_image1 = header + data_image1
	data_image2 = header + data_image2
	data_image3 = header + data_image3
	data_label2=data_image2
	data_label3=data_image3
	data_label1=data_image1
	
	print('c')
	output_file = open(name[1]+'-images-idx3-ubyte-1', 'wb')
	data_image1.tofile(output_file)
	output_file.close()
	output_file = open(name[1]+'-images-idx3-ubyte-2', 'wb')
	data_image2.tofile(output_file)
	output_file.close()
	output_file = open(name[1]+'-images-idx3-ubyte-3', 'wb')
	data_image3.tofile(output_file)
	output_file.close()
	print('d')
	# output_file = open(name[1]+'-labels-idx1-ubyte', 'wb')
	# data_label.tofile(output_file)
	# output_file.close()
	# print('e')
# gzip resulting files

# for name in Names:
# 	os.system('gzip '+name[1]+'-images-idx3-ubyte-1')
# 	os.system('gzip '+name[1]+'-images-idx3-ubyte-2')
# 	os.system('gzip '+name[1]+'-images-idx3-ubyte-3')
# 	print('f')
	# os.system('gzip '+name[1]+'-labels-idx1-ubyte')
	# print('g')