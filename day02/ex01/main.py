def what_are_the_vars(*arg, **kwargs):

    result = ObjectC()
    for key, value in kwargs.items():
        setattr(result, key, value)

    for i in range(0, len(arg)):
        key = "var_" + str(i)
        if not getattr(result, key, None):
            setattr(result, key, arg[i])
        else:
            return None

    return result

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return

    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    # var_0: 7
    obj = what_are_the_vars(7)
    doom_printer(obj)
    # var_0: ft_lol / var_1: Hi
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    #
    obj = what_are_the_vars()
    doom_printer(obj)
    # a: 10 / hello: world / var_0: 12 / var_1: Yes / var_2: [0, 0, 0]
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    # ERROR
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)