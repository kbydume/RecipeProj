import unittest
from recipe import Recipe
from recipebook import RecipeBook
from manage import Manager

class TestRecipeProgram(unittest.TestCase):
    """This class tests methods in the overall recipe program."""
    
    def test_recipe_creation(self):
        """This test tests if a Recipe object is successfully made."""
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test instructions")
        self.assertEqual(recipe.get_title(), "Test Recipe")
        self.assertEqual(recipe.get_ingredients(), ["ingredient1", "ingredient2"])
        self.assertEqual(recipe.get_instructions(), "Test instructions")

    def test_recipebook_add_get_delete(self):
        """This test tests the RecipeBook class's methods:
        add_recipe(), get_all_recipes(), and remove_recipe() to see if they are 
        working correctly. """
        recipe_book = RecipeBook()
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test instructions")
        recipe_book.add_recipe(recipe)
        self.assertEqual(len(recipe_book.get_all_recipes()), 1)
        self.assertEqual(recipe_book.get_all_recipes()[0], recipe)
        recipe_book.remove_recipe(recipe)
        self.assertEqual(len(recipe_book.get_all_recipes()), 0)

    def test_manager_delete_recipe(self):
        """This test tests the Manager class's delete_recipe() method."""
        recipe_book = RecipeBook()
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test instructions")
        recipe_book.add_recipe(recipe)
        manager = Manager(recipe_book)
        manager.delete_recipe("Test Recipe")
        self.assertEqual(len(recipe_book.get_all_recipes()), 0)

if __name__ == "__main__":
    unittest.main()
