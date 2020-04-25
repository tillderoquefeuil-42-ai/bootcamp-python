from ScrapBooker import ScrapBooker
import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("\ntest variable")
print(a)

sb = ScrapBooker()

print("\ntest1")
test1 = sb.crop(a, [2,2], [1,1])
print(test1)

print("\ntest2")
test2 = sb.thin(a, 2, 0)
print(test2)

print("\ntest3")
test3 = sb.thin(a, 5, 0)
print(test3)

print("\ntest4")
test4 = sb.juxtapose(a, 3, 0)
print(test4)

print("\ntest5")
test5 = sb.mosaic(a, [3,4])
print(test5)