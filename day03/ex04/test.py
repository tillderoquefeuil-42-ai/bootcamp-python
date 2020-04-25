import numpy as np
from ImageProcessor import ImageProcessor
from AdvancedFilter import AdvancedFilter

imp = ImageProcessor()
# arr = imp.load("./42AI.png")
arr = imp.load("./elonmusk.png")

af = AdvancedFilter()

# af.mean_blur(arr)
af.gaussian_blur(arr)

imp.display(arr)