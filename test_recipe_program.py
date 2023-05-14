import unittest
import io
from recipe import Recipe
from recipebook import RecipeBook
from manage import Manager
from unittest.mock import patch, mock_open
from recommendation import Recommendation
from Categorize import *
import RecipeFinal

class TestRecipeProgram(unittest.TestCase):
    """This class tests methods in the overall recipe program."""
    ###TEST FOR CATEGORIZE CLASS

    def setUp(self):
        self.file_name = 'recipe.csv'  # A file path to a valid CSV file is needed here
        self.categorizer = Categorize(self.file_name)
        self.categorizer.categorize_recipes()

    def test_categorize_recipes(self):
        meat_categories = self.categorizer.get_meat_categories()
        cooking_styles = self.categorizer.get_cooking_styles()
        
        # Check if the categorization was successful
        self.assertTrue(meat_categories)
        self.assertTrue(cooking_styles)

    def test_get_random_dishes_by_category(self):
        random_dishes = self.categorizer.get_random_dishes_by_category('beef', 'grilled', 2)

    # Check if we get the right number of dishes
        self.assertEqual(len(random_dishes), 2)

        # Check if the dishes are indeed in the 'beef' and 'grilled' categories
        for dish in random_dishes:
            self.assertIn(dish, self.categorizer.meat_categories['beef'])
            self.assertIn(dish, self.categorizer.cooking_styles['grilled'])

        print("\nRandom dishes in the 'beef' and 'grilled' categories:")
        for dish in random_dishes:
            print(dish)

    def test_get_recommendations(self):
        random_dishes = get_recommendations('chicken', 'fried')

        # Check if we get the right number of dishes
        self.assertEqual(len(random_dishes), 2)

        # Check if the dishes are indeed in the 'chicken' and 'fried' categories
        for dish in random_dishes:
            self.assertIn(dish, self.categorizer.meat_categories['chicken'])
            self.assertIn(dish, self.categorizer.cooking_styles['fried'])

        print("\nRecommended dishes in the 'chicken' and 'fried' categories:")
        for dish in random_dishes:
            print(dish)

###TEST FOR RECIPE CLASS
    def test_recipe_creation(self):
        """This test tests if a Recipe object is successfully made."""
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test instructions")
        self.assertEqual(recipe.get_title(), "Test Recipe")
        self.assertEqual(recipe.get_ingredients(), ["ingredient1", "ingredient2"])
        self.assertEqual(recipe.get_instructions(), "Test instructions")
        
###TEST FOR RECIPEBOOK CLASS
    def test_recipebook_add_get_delete(self):
        """This test tests the RecipeBook class's methods:
        add_recipe(), get_all_recipes(), and remove_recipe() to see if they are 
        working correctly. """
        recipe_book = RecipeBook()
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test instructions")
        recipe_book.add_recipe(recipe)
        self.assertEqual(len(recipe_book.get_all_recipes()), 1)
        self.assertEqual(recipe_book.get_all_recipes()[0], recipe)
        recipe_book.remove_recipe(recipe.title)
        self.assertEqual(len(recipe_book.get_all_recipes()), 0)

### TEST FOR MANAGER CLASS 
    def test_manager_delete_recipe(self):
        """This test tests the Manager class's delete_recipe() method."""
        recipe_book = RecipeBook()
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test instructions")
        recipe_book.add_recipe(recipe)
        manager = Manager(recipe_book)
        manager.delete_recipe("Test Recipe")
        self.assertEqual(len(recipe_book.get_all_recipes()), 0)

    def test_get_recipe_input(self):
        recipe_book = RecipeBook()
        recipe = Recipe("test recipe", ["test","eggs"], "test instructions")
        recipe_book.add_recipe(recipe)

        manager = Manager(recipe_book)

        # Test case where user enters new ingredients
        manager.get_recipe_input("test recipe")
        new_recipe = recipe_book.get_recipe("test recipe")
        self.assertIsInstance(new_recipe, Recipe)
        self.assertEqual(new_recipe.get_ingredients(), ["test", "eggs"])
        self.assertEqual(new_recipe.get_instructions(), "test instructions")

        # Test case where user does not enter new ingredients
        manager.get_recipe_input("test recipe")
        new_recipe = recipe_book.get_recipe("test recipe")
        self.assertIsInstance(new_recipe, Recipe)
        self.assertEqual(new_recipe.get_ingredients(), ["test", "eggs"])
        self.assertEqual(new_recipe.get_instructions(), "test instructions")


###TEST FOR RECOMMENDATION CLASS
    def test_get_recommendations(self):
        """This test checks the recommendation of recipes based on a keyword,return the right length."""

        # Initialize a recommendation object
        recommender = Recommendation('recipe.csv')  # Assumed to exist and have appropriate format

        # Test recommendations
        recommendations_chicken = recommender.g_recommendationz('chicken')
        recommendations_broccoli = recommender.g_recommendationz('broccoli')


        # Test the length
        self.assertEqual(len(recommendations_chicken),5)
        self.assertEqual(len(recommendations_broccoli),5)

###TEST FOR RECIPEFINAL.PY 
    @patch('RecipeFinal.add_recipe')
    @patch('RecipeFinal.get_recommendation')
    @patch('RecipeFinal.specific_recommendations')
    @patch('RecipeFinal.Manager.delete_recipe')
    @patch('RecipeFinal.Manager.edit_recipe')
    def test_main(self, mock_edit_recipe, mock_delete_recipe, mock_specific_recommendations, mock_get_recommendation, mock_add_recipe):
        """        
        This function is mocking user's input tp ensure the RecipeFinal main() is calling the right function everytime
        """
        with patch('builtins.input', side_effect=['1', 'Test Recipe', 'Ingredient1,Ingredient2', 'Test Instructions', '6']):
            RecipeFinal.main()
            mock_add_recipe.assert_called()

        with patch('builtins.input', side_effect=['2', '6']):
            RecipeFinal.main()
            mock_get_recommendation.assert_called()

        with patch('builtins.input', side_effect=['3', 'Test Ingredient', '6']):
            RecipeFinal.main()
            mock_specific_recommendations.assert_called()

        with patch('builtins.input', side_effect=['4', 'Test Recipe', '6']):
            RecipeFinal.main()
            mock_delete_recipe.assert_called_with('Test Recipe')

        with patch('builtins.input', side_effect=['5', 'Test Recipe', '6']):
            RecipeFinal.main()
            mock_edit_recipe.assert_called_with('Test Recipe')

if __name__ == "__main__":
    unittest.main()
