from recipe import Recipe

class Manager:
    """This class manages the recipe book which allows for editing and deleting.
    Attributes:
        recipe_book: : A reference to a RecipeBook object that contains
        a collection of recipes."""
    
    def __init__(self, recipe_book):
        """This method initilaizes the Manager class.
        Args:
            recipe_book(RecipeBook): A RecipeBook object containing
            a collection of recipes.
        Side Effects: 
            Sets recipe_book object to its corresponding value."""
        self.recipe_book = recipe_book

    def delete_recipe(self, recipe_title):
        """This method allows for a recipe to be removed from the csv file.
        Args:
            recipe_title(str): The title of the recipe thats deleted."""
        recipe = self.recipe_book.get_recipe(recipe_title)
        if recipe:
            self.recipe_book.remove_recipe(recipe_title)
            print(f"{recipe_title} has been deleted from the recipe book.")
        else:
            print(f"{recipe_title} not found in recipe book.")

    def get_recipe_input(self,title):
        """This method prompts user input for the new recipe information.
        Returns:
            A recipe object with the updated information, none if otherwise. 
            """
        recipe = self.recipe_book.get_recipe(title)
        if not recipe:
            print(f"{title} not found in recipe book.")
            return None

        ingredients = input(f"Enter new ingredients for {title} (leave blank to keep current ingredients): ")
        if ingredients:
            ingredients = ingredients.split(",")
        else:
            ingredients = []

        instructions = input(f"Enter new instructions for {title} (leave blank to keep current instructions): ")
        if not instructions:
            instructions = recipe.get_instructions()

        new_recipe = Recipe(title, ingredients, instructions)
        return new_recipe


    def print_recipe_output(self, recipe):
        """This method prints the updated recipe information.
        Args:
         recipe(Recipe): The Recipe object to print the information for.
         """
        print(f"\n{recipe.get_title()} has been updated with:")
        print(f"Ingredients: {', '.join(recipe.get_ingredients())}")
        print(f"Instructions: {recipe.get_instructions()}")

    def edit_recipe(self,title):
        """This method edits the recipe book by replacing the new Recipe object
        with the updated information."""
        recipe = self.recipe_book.get_recipe(title)
        if not recipe:
            print(f"{title} not found in recipe book.")
            return

        new_recipe = self.get_recipe_input(title)
        if not new_recipe:
            return
        self.recipe_book.remove_recipe(title)
        self.recipe_book.add_recipe(new_recipe)
        print(f"{title} successfully updated.")

