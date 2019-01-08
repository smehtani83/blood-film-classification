import numpy as np
import h5py

def read_file(file_name) -> np.ndarray:
        """
        read images from idx files.

        All the data are stored in idx format.
        All the integers in the files are stored in the MSB first format used by most non-Intel processors.
        Pixel value in the raw data was 0~255.
        This method normalize all values to 0~1.
        """
        def bytes2int(input_bytes):
            return int.from_bytes(input_bytes, byteorder='big')

        with open(file_name, 'rb') as file:
            first2bytes = bytes2int(file.read(2))
            assert first2bytes == 0  # The first 2 bytes are always 0

            data_type = bytes2int(file.read(1))
            assert data_type == 8  # 0x08: unsigned byte

            num_dimensions = bytes2int(file.read(1))
            shape = [bytes2int(file.read(4)) for _ in range(num_dimensions)] + [1]  # make the num of channels to be 1
            shape=(15000,128,128,1)
            matrix = np.frombuffer(file.read(), dtype=np.uint8).reshape(shape)

        return matrix
images= np.concatenate(((read_file('wbc_train-images-idx3-ubyte-1') /255),(read_file('wbc_train-images-idx3-ubyte-2') /255),((read_file('wbc_train-images-idx3-ubyte-3') /255))),axis=3,out=None)

# training_images1 = read_file('wbc_train-images-idx3-ubyte-1') /255
# training_images2 = read_file('wbc_train-images-idx3-ubyte-2') / 255


# training_images1= np.concatenate(((training_images1),(training_images2)),axis=3,out=None)
# del training_images2
# training_images3 = read_file('wbc_train-images-idx3-ubyte-3') / 255
# training


f = h5py.File("mytrain-30000.hdf5", "w")
dset = f.create_dataset("init", data=images)
