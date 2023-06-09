import re
import csv
import random

class Categorize:
    def __init__(self, file_name):

        """
        Initialize the Categorize object.

        Args:
            file_name (str): The name of the CSV file containing recipes.
        """

        self.file_name = file_name
        self.recipes = []
        self.meat_categories = {
            'beef': [],
            'pork': [],
            'chicken': [],
            'fish': [],
            'lamb': [],
            'other': []
        }
        self.cooking_styles = {
            'grilled': [],
            'fried': [],
            'baked': [],
            'roasted': [],
            'stewed': [],
            'boiled': [],
            'steamed': [],
            'stir-fried': [],
            'other':[]
        }
        self.read_csv()

    def read_csv(self):

        """
        Read the CSV file and populate the recipes list with its contents.
        """

        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader)  # Skip the header row
            self.recipes = [row for row in reader]

    def categorize_recipes(self):

        """
        Categorize the recipes based on meat type and cooking style.
        """

        for recipe in self.recipes:
            name = recipe[0]
            ingredients = recipe[1]
            instructions = recipe[2]

            found_meat = False
            found_style = False

            for category in self.meat_categories:
                if category == 'other':
                    continue

                pattern = re.compile(f'\\b{category}\\b', re.IGNORECASE)
                if pattern.search(ingredients):
                    self.meat_categories[category].append(name)
                    found_meat = True

            if not found_meat:
                self.meat_categories['other'].append(name)

            for style in self.cooking_styles:
                pattern = re.compile(f'\\b{style}\\b', re.IGNORECASE)
                if pattern.search(instructions):
                    self.cooking_styles[style].append(name)
                    found_style = True

            if not found_style:
                self.cooking_styles['other'].append(name)

    def get_meat_categories(self):

        """
        Get the categorized recipes based on meat type.

        Returns:
            dict: A dictionary containing the categorized recipes based on meat type.
        """

        return self.meat_categories

    def get_cooking_styles(self):

        """
        Get the categorized recipes based on cooking style.

        Returns:
            dict: A dictionary containing the categorized recipes based on cooking style.
        """

        return self.cooking_styles

    def get_random_dishes_by_category(self, meat, style, num_dishes=2):

        """
        Get random dishes from the specified meat category and cooking style.

        Args:
            meat (str): The meat category.
            style (str): The cooking style.
            num_dishes (int, optional): The number of random dishes to retrieve. Defaults to 2.

        Returns:
            list: A list of random dish names.
        """

        dishes_in_meat_category = self.meat_categories.get(meat, [])
        dishes_in_style_category = self.cooking_styles.get(style, [])
        
        if not dishes_in_meat_category:
            print(f"Meat category '{meat}' not found.")
            return []

        if not dishes_in_style_category:
            print(f"Cooking style '{style}' not found.")
            return []

        combined_dishes = list(set(dishes_in_meat_category) & set(dishes_in_style_category))

        if len(combined_dishes) < num_dishes:
            print(f"Only {len(combined_dishes)} dishes available in the '{meat}' and '{style}' categories.")
            num_dishes = len(combined_dishes)

        random_dishes = random.sample(combined_dishes, num_dishes)
        return random_dishes

# ...

def get_recommendations(meat, style):
    
    """
    Get random dish recommendations based on the specified meat category and cooking style.

    Args:
        meat (str): The meat category.
        style (str): The cooking style.

    Returns:
        list: A list of random dish names.
    """

    file_name = 'recipe.csv'
    categorizer = Categorize(file_name)
    categorizer.categorize_recipes()
    random_dishes = categorizer.get_random_dishes_by_category(meat, style, num_dishes=2)
    return random_dishes
