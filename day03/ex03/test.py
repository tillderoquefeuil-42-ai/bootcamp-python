import numpy as np
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imp = ImageProcessor()
# arr = imp.load("./42AI.png")
arr = imp.load("./elonmusk.png")

cf = ColorFilter()

# cf.invert(arr)
# cf.to_blue(arr)
# cf.to_green(arr)
# cf.to_red(arr)
# cf.celluloid(arr)

# cf.to_grayscale(arr, 'm')
# cf.to_grayscale(arr, 'weigthed')

imp.display(arr)