from book import Book
from recipe import Recipe


print("TEST ON RECIPE")

try:
    print("\nExpected: OK")
    r1 = Recipe('pasta', 1, 7, ['pasta', 'pesto'], 'pasta with pesto', 'lunch')
    print(str(r1))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: No name")
    r2 = Recipe('', 1, 7, ['pasta', 'pesto'], 'pasta with pesto', 'lunch')
    print(str(r2))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: Bad input on cooking_lvl")
    r3 = Recipe('pasta', 10, 7, ['pasta', 'pesto'], 'pasta with pesto', 'lunch')
    print(str(r3))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: Bad type on cooking_lvl")
    r4 = Recipe('pasta', 1, "seven", ['pasta', 'pesto'], 'pasta with pesto', 'lunch')
    print(str(r4))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: ingredients empty")
    r5 = Recipe('pasta', 1, 7, [], 'pasta with pesto', 'lunch')
    print(str(r5))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: Bad type on ingredients values")
    r6 = Recipe('pasta', 1, 7, ['pasta', 'pesto', 14], 'pasta with pesto', 'lunch')
    print(str(r6))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: Ok (but no description)")
    r7 = Recipe('pasta', 1, 7, ['pasta', 'pesto'], '', 'lunch')
    print(str(r7))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: Bad value for recipe_type")
    r8 = Recipe('pasta', 1, 7, ['pasta', 'pesto'], 'pasta with pesto', 'breakfast')
    print(str(r8))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))


print("TEST ON BOOK")

try:
    print("\nExpected: OK")
    b1 = Book('cookbook')
    print(str(b1))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))

try:
    print("\nExpected: bad name type")
    b2 = Book(14)
    print(str(b2))
except (TypeError, ValueError) as error:
    print("ERROR: " + str(error))



print("\n\nTEST ON BOTH")

myBook = Book('my cookbook')

pasta = Recipe('pasta', 1, 7, ['pasta', 'pesto'], 'pasta with pesto', 'lunch')
salad = Recipe('salad', 2, 15, ['rice', 'thuna', 'tomatoes'], 'Rice salad with thuna and tomatoes', 'lunch')
avocado = Recipe('avocado', 1, 2, ['avocado', 'salt', 'vinegar'], 'half avocado with salt and vinegar', 'starter')
cake = Recipe('cake', 2, 45, ['flour', 'sugar', 'eggs'], 'yumi yumi cake', 'dessert')

myBook.add_recipe(pasta)
myBook.add_recipe(salad)
myBook.add_recipe(avocado)
myBook.add_recipe(cake)
myBook.add_recipe("it's a prank, i'm not a recipe")

myBook.get_recipe_by_name('pasta')
myBook.get_recipes_by_types('lunch')