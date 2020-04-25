import time

import ai42.progressbar

listy = range(1000)
ret = 0
for elem in ai42.progressbar.progressbar(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
 
print()
print(ret)

