import matplotlib.pyplot as plt
import numpy as np
import os

class ImageProcessor():

    def load(self, path):
        if not os.path.exists(path) or not os.path.isfile(path):
            return None

        image = plt.imread(path)
        print("Loading image of dimensions {size[0]} x {size[1]}".format(size=image.shape))
        return image
        
    def display(self, array):
        if array is not None:
            plt.axis('off')
            plt.imshow(array)
            plt.show()
