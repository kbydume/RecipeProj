from recipe import Recipe

class RecipeBook:
    """This class is a collection of recipes.
    Attributes:
        recipes(list): a list of recipe objects."""
    
    def __init__(self):
        """This method initializes the RecipeBook class with the attributes.
    Side effect:
        Sets the attribute recipes to an empty list."""
        self.recipes = []

    def add_recipe(self, recipe):
        """This method adds a recipe to the recipe book.
        Args:
            recipe(Recipe): A Recipe object."""
        self.recipes.append(recipe)

    def get_recipe(self, title):
        """This method searches for a recipe in the recipe book using its
        title.
        Args:
            title(str): The title of the recipe.
        Returns:
            Recipe if the title of it is found or None if not.
            """
        for recipe in self.recipes:
            if recipe.get_title() == title:
                return recipe
        return None

    def get_all_recipes(self):
        """This method is just meant to return a list of the recipes
        in the recipe book
        Returns:
            A list of recipe objects.""" 
        return self.recipes

    def remove_recipe(self, recipe):
        """This method removes a recipe from the recipe book.
        Args:
            recipe(Recipe): a recipe object that's gonna be removed."""
        found_recipe = self.get_recipe(recipe)
        if found_recipe:
            self.recipes.remove(found_recipe)
        else:
            return

    def __str__(self):
        """This method returns a string reprsentation of the recipe book.
        Returns:
            A string representation of the recipe book."""
        recipe_list = "\n\n".join([str(recipe) for recipe in self.recipes])
        return f"Recipe Book:\n\n{recipe_list}"
