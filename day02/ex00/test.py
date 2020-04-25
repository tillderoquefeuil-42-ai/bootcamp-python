from functools import reduce

from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

def test_map():
    print("\nMAP_TEST 1:\n")
    def addition(n): 
        return n + n

    numbers = (1, 2, 3, 4) 

    result = map(addition, numbers) 
    print(list(result)) 
    result = ft_map(addition, numbers) 
    print(list(result)) 


    print("\n\nMAP_TEST 2:\n")
    numbers = (1, 2, 3, 4)

    result = map(lambda x: x + x, numbers) 
    print(list(result)) 
    result = ft_map(lambda x: x + x, numbers) 
    print(list(result)) 


    print("\n\nMAP_TEST 3:\n")
    l = ['sat', 'bat', 'cat', 'mat'] 
    
    test = list(map(list, l)) 
    print(test)
    test = list(ft_map(list, l)) 
    print(test)


    print("\n\nMAP_TEST 4:\n")
    nbr = 4

    try:
        result = map(list, nbr)
    except TypeError as e:
        print(e)

    try:
        result = ft_map(list, nbr)
    except TypeError as e:
        print(e)

def test_filter():
    print("\n\nFILTER_TEST 1:\n")
    seq = [0, 1, 2, 3, 5, 8, 13] 
    
    result = filter(lambda x: x % 2 != 0, seq)
    print(list(result))
    result = ft_filter(lambda x: x % 2 != 0, seq)
    print(list(result))


    print("\n\nFILTER_TEST 2:\n")

    seq = [0, 1, 2, 3, 5, 8, 13] 
    result = filter(lambda x: x % 2 == 0, seq)
    print(list(result))
    result = ft_filter(lambda x: x % 2 == 0, seq)
    print(list(result))

def test_reduce():
    print("\n\nREDUCE_TEST 1:\n")

    lis = [ 1, 3, 4, 10, 4 ] 
    
    result = reduce(lambda x, y:x+y, lis)
    print(result)
    result = ft_reduce(lambda x, y:x+y, lis)
    print(result)


    print("\n\nREDUCE_TEST 2:\n")

    lis = [ 1, 3, 4, 10, 4 ] 
    
    result = reduce(lambda x, y:x*y, lis)
    print(result)
    result = ft_reduce(lambda x, y:x*y, lis)
    print(result)

test_map()
test_filter()
test_reduce()