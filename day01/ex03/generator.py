import time

def random(max):
    t = time.time()
    t = int(t * 10000) % max
    return t

def shuffle(lst):
    data = []

    while len(lst) > 0:
        r = random(len(lst))
        data.append(lst[r])
        del lst[r]
    return data

def unique(lst):
    data = []
      
    for value in lst:
        if value not in data:
            data.append(value)
    return data

def generator(text, sep=" ", option=None):
    if not type(text) is str:
        print('ERROR')
        return

    lst = text.split(sep)

    if option == "shuffle":
        lst = shuffle(lst)
    elif option == "unique":
        lst = unique(lst)
    elif option == "ordered":
        lst.sort()
    elif option and len(option) > 0:
        print('ERROR')
        return

    for w in lst:
        yield w