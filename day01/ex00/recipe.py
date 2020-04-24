
class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):

        self.__setName(name)
        self.__setCookingLvl(cooking_lvl)
        self.__setCookingTime(cooking_time)
        self.__setIngredients(ingredients)
        self.__setDescription(description)
        self.__setRecipeType(recipe_type)



    def __str__(self):
        '''Return the string to print with the recipe info'''

        return "Recipe for {self.name}:\n\
            Description: {self.description}\n\
            Ingredients list: {self.ingredients}\n\
            To be eaten for {self.recipe_type}\n\
            Takes {self.cooking_time} minutes of cooking\n\
            Recipe level: {self.cooking_lvl}\
        ".format(self=self)


    def __setName(self, name):
        if not type(name) is str:
            raise TypeError("name has to be -str-")
        if not name:
            raise ValueError("name can't be null")

        self.name = name
        return True

    # range 1 to 5
    def __setCookingLvl(self, cooking_lvl):
        if not type(cooking_lvl) is int:
            raise TypeError("cooking_lvl has to be -int-")
        if 0 > cooking_lvl or cooking_lvl > 5:
            raise ValueError("cooking_lvl has to be between 1 and 5")

        self.cooking_lvl = cooking_lvl
        return True

    # in minutes (no negative numbers)
    def __setCookingTime(self, cooking_time):
        if not type(cooking_time) is int:
            raise TypeError("cooking_time has to be -int-")
        if 0 > cooking_time:
            raise ValueError("cooking_time can't be negative")

        self.cooking_time = cooking_time
        return True

    # list of all ingredients each represented by a string 
    def __setIngredients(self, ingredients):
        if not type(ingredients) is list:
            raise TypeError("ingredients has to be -list-")
        if not all(isinstance(x, str) for x in ingredients):
            raise TypeError("ingredients must contains -str- only")
        if len(ingredients) == 0:
            raise ValueError("ingredients can't be empty")

        self.ingredients = ingredients
        return True

    # description of the recipe
    def __setDescription(self, description):
        if not type(description) is str:
            raise TypeError("description has to be -str-")

        self.description = description
        return True

    # can be “starter”, “lunch” or “dessert”.
    def __setRecipeType(self, recipe_type):
        recipe_types = ["starter", "lunch", "dessert"]

        if not type(recipe_type) is str:
            raise TypeError("recipe_type has to be -str-")
        if not recipe_type in recipe_types:
            raise ValueError("recipe_type has to be 'starter', 'lunch' or 'dessert'")

        self.recipe_type = recipe_type
        return True
