import numpy as np

class NumPyCreator():

    # takes in a list and returns its corresponding NumPy array.
    def from_list(self, lst):
        return np.asarray(lst)

    # takes in a tuple and returns its corresponding NumPy array.
    def from_tuple(self, tpl):
        return np.asarray(tpl)

    # takes in an iterable and returns an array which contains all of its elements.
    def from_iterable(self, itr):
        return np.asarray(list(itr))

    # returns an array filled with the same value.
    # The first argument is a tuple which specifies the shape of the array, and the second argument specifies the value of all the elements. This value must be 0 by default.
    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    # returns an array filled with random values.
    # It takes as an argument a tuple which specifies the shape of the array.
    def random(self, shape):
        return np.random.random_sample(shape)

    # returns an array representing the identity matrix of size n.
    def identity(self, n):
        return np.eye(n)