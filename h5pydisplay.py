import numpy as np
import h5py
import matplotlib.pyplot as plt

hdf5_file = h5py.File('mytrain-30000.hdf5', "r")
train_dataset = hdf5_file["init"][:]
print (np.shape(train_dataset))
img = train_dataset[1]
plt.imshow(img)
plt.show()
hdf5_file.close()
#imgdataset = train_dataset[0:10]
