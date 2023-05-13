import unittest
from Categorize import Categorize, get_recommendations

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


if __name__ == '__main__':
    unittest.main()
