from matplotlib import pyplot as plt
import numpy as np
import os


class MNIST(object):
    """
    Prepare data batches for training and testing.

    Data files are from http://yann.lecun.com/exdb/mnist/

    The training set contains 60000 examples, and the test set 10000 examples.
    The first 5000 examples of the test set are taken from the original NIST training set.
    The last 5000 are taken from the original NIST test set.
    The first 5000 are cleaner and easier than the last 5000.
    each image is 28x28 pixels
    """
    def __init__(self):
        self.training_images1 = self.read_file('/content/drive/My Drive/15000_files_wbc/wbc_train-images-idx3-ubyte-1') /255
        self.training_images2 = self.read_file('/content/drive/My Drive/15000_files_wbc/wbc_train-images-idx3-ubyte-2') / 255
        self.training_images3 = self.read_file('/content/drive/My Drive/15000_files_wbc/wbc_train-images-idx3-ubyte-3') / 255
        self.shp=(self.training_images3.shape)
        # self.t4=self.training_images3
        # del self.t4
        # del self.training_images3
        self.training_labels = None

        self.testing_images1 = None
        self.testing_images2 = None
        self.testing_images3 = None
        self.testing_labels = None

    def give(self):
        print(self.shp)
    def read_file(self, file_name) -> np.ndarray:
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

    def vectorize(self, labels):
        """
        convert labels into a 1-hot vectors
        """
        num_labels = labels.shape[0]
        num_classes = 10

        keys = np.zeros((num_labels, num_classes))
        for key, label in zip(keys, labels):
            key[label] = 1
        return keys

    def get_batch(self, batch_size, dataset='training'):
        """
        get a batch of images and corresponding labels.

        returned images would have the shape of (batch_size, 28, 28);
        returned labels would have the shape of (batch_size, 10)

        :param batch_size:
        :param dataset: 'training' or 'testing'
        """
        if dataset == 'training':
            # if self.training_images1 is None or self.training_labels is None:
            #     # self.training_images1 = self.read_file('wbc_train-images-idx3-ubyte-1') / 255
                # self.training_images2 = self.read_file('wbc_train-images-idx3-ubyte-2') / 255
                # self.training_images3 = self.read_file('wbc_train-images-idx3-ubyte-3') / 255
                    
                #self.training_labels = self.training_images
                #self.training_labels = self.vectorize(self.read_file('MNIST_files/train-labels-idx1-ubyte'))
            # images1 = self.training_images1
            # images2 = self.training_images2
            # images3 = self.training_images3
            xyza=1  
            #labels = self.training_labels
        elif dataset == 'testing':
            if self.testing_images is None or self.testing_labels is None:
                self.testing_images = self.read_file('MNIST_files/t10k-images-idx3-ubyte') / 255
                self.testing_labels = self.vectorize(self.read_file('MNIST_files/t10k-labels-idx1-ubyte'))
            images = self.testing_images
            labels = self.testing_labels
        else:
            return
        #print(images1.shape)    
        #num_samples = labels.shape[0]
        num_samples=((self.training_images1).shape)[0]
        #print(num_samples)
        idx = np.random.randint(num_samples, size=batch_size)
        images= np.concatenate(((self.training_images1)[idx],(self.training_images2)[idx],(self.training_images3)[idx]),axis=3,out=None)
        #print(images.shape)
        #return images[idx], labels[idx]
        return images,0

def main():
    #mnist = MNIST()
    #images, labels = mnist.get_batch(10, 'training')
    #mnist.give()
    # for im, lb in zip(images, labels):
    #     plt.imshow(im, cmap=plt.cm.gray, interpolation='nearest')
    #     plt.text(1, 1, lb, color='w')
    #     plt.show()
    # images=mnist.get_batch(10, 'training')
    #print(type(images))
    x=1

# if __name__ == '__main__':
#     main()


if __name__ == '__main__':
    main()