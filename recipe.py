class Recipe:
    """
    A class representing a recipe.

    Attributes
    ----------
    title : str
        The title of the recipe.
    ingredients : list
        A list of ingredients needed for the recipe.
    instructions : str
        The instructions for preparing the recipe.
    """

    def __init__(self, title, ingredients, instructions):
        """
        Parameters
        ----------
        title : str
            The title of the recipe.
        ingredients : list
            A list of ingredients needed for the recipe.
        instructions : str
            The instructions for preparing the recipe.

        """
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def get_title(self):
        """
        Returns the title of the recipe.
        """
        return self.title

    def get_ingredients(self):
        """
        Returns a list of ingredients needed for the recipe.
        """
        return self.ingredients

    def get_instructions(self):
        """
        Returns the instructions for preparing the recipe.
        """
        return self.instructions

    def __str__(self):
        """
        Returns a string representation of the recipe.
        """
        return f"{self.title}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"
