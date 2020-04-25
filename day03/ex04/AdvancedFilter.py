import numpy as np
import math 

class AdvancedFilter():

    def ft_map(self, array, func):
        tr = True if array.shape[2] == 4 else False

        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                pixels = func(array, i, j)
                if tr == True:
                    array[i,j] = (pixels[0], pixels[1], pixels[2], 1.0)
                else:
                    array[i,j] = pixels
        return array

    def crop(self, array, dimensions, position):
        if position[0] + dimensions[0] > array.shape[0]:
            return None
        if position[1] + dimensions[1] > array.shape[1]:
            return None

        return array[position[0]:position[0]+dimensions[0] , position[1]:position[1]+dimensions[1]]

    def getDimensions(self, a, i, j, k_size):
        n = abs(k_size * 3 - (k_size - 1))
        d = [n, n]

        size = math.ceil(n/2)

        if i + size > a.shape[0]:
            d[0] -= 1
        if j + size > a.shape[1]:
            d[1] -= 1
        return d

    def getPosition(self, i, j):
        p = [0, 0]
        if i - 1 > 0:
            p[0] = i - 1
        if j - 1 > 0:
            p[1] = j - 1
        return p

    def mean_blur(self, array):
        k_size = 1

        def func(a, i, j):
            crop = self.crop(a, self.getDimensions(a, i, j, k_size), self.getPosition(i, j))
            
            avg = [
                np.average(crop[:,:,:1]),
                np.average(crop[:,:,1:2]),
                np.average(crop[:,:,2:3])
            ]
            return avg
        
        array = self.ft_map(array, func)
        return array

    def gaussian_blur(self, array):
        k_size = 1

        def func(a, i, j):
            crop = self.crop(a, self.getDimensions(a, i, j, k_size), self.getPosition(i, j))
            
            avg = [
                np.average(crop[:,:,:1]),
                np.average(crop[:,:,1:2]),
                np.average(crop[:,:,2:3])
            ]
            return avg
        
        array = self.ft_map(array, func)
        return array
