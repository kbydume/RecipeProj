import unittest
import io
from recipe import Recipe
from recipebook import RecipeBook
from manage import Manager
from unittest.mock import patch, mock_open
from recommendation import Recommendation
from Categorize import *
from RecipeFinal import add_recipe, get_recommendation, specific_recommendations, save_to_csv, load_from_csv

class TestRecipeProgram(unittest.TestCase):
    """This class tests methods in the overall recipe program."""

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

    #test for editor method
    #test for print output 

###TEST FOR CATEGORIZE CLASS

class TestCategorize(unittest.TestCase):

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

    def test_get_recommendations(self):
        random_dishes = get_recommendations('chicken', 'fried')

        # Check if we get the right number of dishes
        self.assertEqual(len(random_dishes), 2)

        # Check if the dishes are indeed in the 'chicken' and 'fried' categories
        for dish in random_dishes:
            self.assertIn(dish, self.categorizer.meat_categories['chicken'])
            self.assertIn(dish, self.categorizer.cooking_styles['fried'])

###TEST FOR RECOMMENDATION CLASS

###TEST FOR RECOMMENDATION CLASS
    def test_get_recommendations(self):
        """This test checks the recommendation of recipes based on a keyword."""

        # Initialize a recommendation object
        recommender = Recommendation('test_recipes.csv')  # Assumed to exist and have appropriate format

        # Test recommendations
        recommendations_chicken = recommender.get_recommendations('chicken')
        recommendations_broccoli = recommender.get_recommendations('broccoli')

        # Check that all recommended recipes contain the keyword
        for title in recommendations_chicken:
            self.assertIn('chicken', title.lower())
        for title in recommendations_broccoli:
            self.assertIn('broccoli', title.lower())

        # Test keyword with no matches
        recommendations_no_match = recommender.get_recommendations('no_match_keyword')
        self.assertEqual(recommendations_no_match, ["Sorry, we do not have any options with 'no_match_keyword' as an ingredient."])


###TEST FOR RECIPEFINAL.PY 

class RecipeFinalTests(unittest.TestCase):

    @patch('builtins.input', side_effect=['Test Recipe', 'Chicken, Salt, Pepper', 'Cook chicken and add salt and pepper.'])
    def test_add_recipe(self, input):
        recipe_book = RecipeBook()
        add_recipe(recipe_book)
        self.assertEqual(len(recipe_book.get_all_recipes()), 1)

    @patch('Categorize.get_recommendations')
    @patch('builtins.input', side_effect=['chicken', 'grilled'])
    def test_get_recommendation(self, input, mock_get_recommendations):
        mock_get_recommendations.return_value = ['Grilled Chicken']
        result = get_recommendation()
        self.assertEqual(result, 'Grilled Chicken')

    @patch('Recommendation.get_recommendations')
    @patch('builtins.input', return_value='chicken')
    def test_specific_recommendations(self, input, mock_get_recommendations):
        mock_get_recommendations.return_value = ['Chicken Recipe']
        result = specific_recommendations()
        self.assertEqual(result, 'Chicken Recipe')

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_csv(self, mock_file):
        recipe_book = RecipeBook()
        recipe = Recipe('Test Recipe', ['Chicken', 'Salt', 'Pepper'], 'Cook chicken and add salt and pepper.')
        recipe_book.add_recipe(recipe)
        save_to_csv(recipe_book)
        mock_file.assert_called_once_with('recipe.csv', 'w', newline='')

    @patch('builtins.open', new_callable=mock_open, read_data='Test Recipe,Chicken,Salt,Pepper,Cook chicken and add salt and pepper.')
    def test_load_from_csv(self, mock_file):
        recipe_book = RecipeBook()
        load_from_csv(recipe_book)
        self.assertEqual(len(recipe_book.get_all_recipes()), 1)

if __name__ == "__main__":
    unittest.main()
