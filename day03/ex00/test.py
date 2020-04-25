from NumPyCreator import NumPyCreator

npc = NumPyCreator()

r = npc.from_list([[1,2,3],[6,3,4]])
print(r)

r = npc.from_tuple(("a", "b", "c"))
print(r)

r = npc.from_iterable(range(5))
print(r)

shape=(3,5)
r = npc.from_shape(shape, value=0)
print(r)

r = npc.random(shape)
print(r)

r = npc.identity(4)
print(r)