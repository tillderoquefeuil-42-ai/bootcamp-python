cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}

# keys = []
# values = []
# for key in cookbook:
#     keys.append(key)
#     values.append(cookbook[key])

# print(keys)    
# print(values)
# print(cookbook)


def getRecipe(name):
    if name in cookbook:
        print("Recipe for %s:" % name)
        print("Ingredients list: " + ", ".join(cookbook[name]['ingredients']))
        print("To be eaten for %s." % cookbook[name]['meal'])
        print("Takes %d minutes of cooking." % cookbook[name]['prep_time'])
    else:
        print("No matching recipe for %s" % name)

# getRecipe("pasta")
# getRecipe("salad")


def deleteRecipe(name):
    if name in cookbook:
        del cookbook[name]
        print("%s has been deleted from cookbook" % name)
    else:
        print("No matching recipe for %s" % name)

# deleteRecipe("pasta")
# deleteRecipe("sandwich")
# print(cookbook)

def addRecipe(name, ingredients, meal, prep_time):
    if name in cookbook:
        print("Already a recipe for %s" % name)
    else:
        cookbook[name] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time
        }
        print("%s has been added to cookbook" % name)

# addRecipe("salad", ["thuna", "rice", "corn"], 'lunch', 15)
# addRecipe("pasta", ["pasta", "pesto"], "lunch", 7)
# print(cookbook)


def getRecipesNames():
    keys = []
    for key in cookbook:
        keys.append(key)

    print(" - ".join(keys))

# getRecipesNames()


def navigate():

    selection = 0
    while selection != 5:
        choices = [1, 2, 3, 4, 5]

        selection = 0
        selection = input("\n\nPlease select an option by typing the corresponding number:\n\
1: Add a recipe\n\
2: Delete a recipe\n\
3: Print a recipe\n\
4: Print the cookbook\n\
5: Quit\n")
        if selection.isdigit():
            selection = int(selection)

        while not selection in choices:
            selection = input("This option does not exist, please type the corresponding number.\n\
To exit, enter 5.\n")
            if selection.isdigit():
                selection = int(selection)

        if selection == 1:
            name = input("What's the new recipe's name?\n")
            while not name:
                name = input("Can't be empty\n")

            ingredients = input("What are the ingredients (separated by a space)?\n")
            while not ingredients:
                ingredients = input("Can't be empty\n")

            meal = input("What kind of meal is it?\n")
            while not meal:
                meal = input("Can't be empty\n")

            prep_time = input("How many time does it take to be done?\n")
            while not prep_time.isdigit():
                prep_time = input("It has to be a number\n")

            ingredients = list(ingredients.split(" ")) 
            prep_time = int(prep_time)

            addRecipe(name, ingredients, meal, prep_time)
        elif selection == 2:
            name = input("Which recipe do you want to delete?\n")
            while not name:
                name = input("Can't be empty\n")

            deleteRecipe(name)
        elif selection == 3:
            name = input("Which recipe do you want to print?\n")
            while not name:
                name = input("Can't be empty\n")

            getRecipe(name)
        elif selection == 4:
            getRecipesNames()

    print("Cookbook closed.")

navigate()