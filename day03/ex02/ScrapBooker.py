import numpy as np
import math

class ScrapBooker():

    #crop the image as a rectangle with the given dimensions (mean- ing, the new height and width for the image), whose top left corner is given by the position argument. The position should be (0,0) by default. You have to consider it an error (and handle said error) if dimensions is larger than the current image size.
    def crop(self, array, dimensions, position):
        if position[0] + dimensions[0] > array.shape[0]:
            return None
        if position[1] + dimensions[1] > array.shape[1]:
            return None

        return array[position[0]:position[0]+dimensions[0] , position[1]:position[1]+dimensions[1]]

    #delete every n-th pixel row along the specified axis (0 vertical, 1 horizontal), example below.
    def thin(self, array, n, axis):
        size = array.shape[0] if axis == 0 else array.shape[1]
        tmp = array[:]

        max = math.floor(size / n) * n
        while max > 0:
            tmp = np.delete(tmp, max-1, axis)
            max -= n

        return tmp

    #juxtapose n copies of the image along the specified axis (0 vertical, 1 horizontal).
    def juxtapose(self, array, n, axis):
        tmp = array[:]
        while n > 0:
            tmp = np.concatenate((tmp, array), axis=axis)
            n -= 1
        return tmp

    #make a grid with multiple copies of the array. The dimensions argument specifies the dimensions (meaning the height and width) of the grid (e.g. 2x3).
    def mosaic(self, array, dimensions):
        tmp = self.juxtapose(array, dimensions[0], 0)
        tmp = self.juxtapose(tmp, dimensions[1], 1)
        
        return tmp
