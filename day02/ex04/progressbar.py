import time

def progressbar(lst):
    length = len(lst)
    start = time.time()
    timer = -1

    for key in lst:

        ratio = key * 100 / length
        left = 100 - ratio

        current = time.time()
        elapsed = current - start
        
        if ratio > 0:
            timer = (elapsed / ratio) * (left)

        progressBar = '=' * (int(ratio/5) - 1) + '>' + ' ' * (int(left/5))

        print("ETA: {:.2f}s [ {:.0f}%][{:s}] {:d}/{:d} | elapsed time {:.2f}s".format(timer, ratio, progressBar, key, length, elapsed), end='\r')

        yield lst[key]
