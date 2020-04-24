from datetime import datetime
from recipe import Recipe

class Book:

    def __init__(self, name):

        self.__setName(name)
        self.__setLastUpdate()
        self.__setCreationDate()
        self.__initRecipesList()

    def __str__(self):
        '''Return the string to print with the book info'''

        return "Book name {self.name}:\n\
            Created on {self.creation_date}\n\
            Updated on {self.last_update}\n\
            Recipes available: {self.recipes_list}\
        ".format(self=self)

    def __setName(self, name):
        if not type(name) is str:
            raise TypeError("name has to be -str-")
        if not name:
            raise ValueError("name can't be null")

        self.name = name
        return True

    def __setLastUpdate(self):
        self.last_update = datetime.now()
        return True

    def __setCreationDate(self):
        self.creation_date = datetime.now()
        return True

    def __initRecipesList(self):
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }
        return True


    def get_recipe_by_name(self, name):
        '''Print a recipe with the name `name` and return the instance'''
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe    


    def get_recipes_by_types(self, recipe_type):
        '''Get all recipe names for a given recipe_type '''
        recipe_types = ["starter", "lunch", "dessert"]
        if not recipe_type in recipe_types:
            print("recipe_type has to be 'starter', 'lunch' or 'dessert'")
            return

        names = []
        for recipe in self.recipes_list[recipe_type]:
            names.append(recipe.name)
        print(", ".join(names))
        return names

    def add_recipe(self, recipe):
        '''Add a recipe to the book and update last_update'''

        if not type(recipe) is Recipe:
            print("var recipe is not of type -Recipe-")
            return

        self.recipes_list[recipe.recipe_type].append(recipe)
        self.__setLastUpdate()

