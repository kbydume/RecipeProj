import re
import csv
import random

class Categorize:
    def __init__(self, file_name):
        self.file_name = file_name
        self.recipes = []
        self.categories = {
            'beef': [],
            'pork': [],
            'chicken': [],
            'fish': [],
            'lamb': [],
            'other': []
        }
        self.read_csv()

    def read_csv(self):
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader)  # Skip the header row
            self.recipes = [row for row in reader]

    def categorize_recipes(self):
        for recipe in self.recipes:
            name = recipe[1]
            ingredients = recipe[2]
            found = False

            for category in self.categories:
                if category == 'other':
                    continue

                pattern = re.compile(f'\\b{category}\\b', re.IGNORECASE)
                if pattern.search(ingredients):
                    self.categories[category].append(name)
                    found = True

            if not found:
                self.categories['other'].append(name)

    def get_categories(self):
        return self.categories
    
    def get_random_dishes_by_category(self, category, num_dishes=2):
        if category not in self.categories:
            print(f"Category '{category}' not found.")
            return []

        dishes_in_category = self.categories[category]
        if len(dishes_in_category) < num_dishes:
            print(f"Only {len(dishes_in_category)} dishes available in the '{category}' category.")
            num_dishes = len(dishes_in_category)

        random_dishes = random.sample(dishes_in_category, num_dishes)
        return random_dishes
    
    
file_name = 'recipe.csv'

categorizer = Categorize(file_name)
categorizer.categorize_recipes()
categorized_recipes = categorizer.get_categories()

def get_recommendations(meat):

    random_dishes = categorizer.get_random_dishes_by_category(f"{meat}", num_dishes=2)
    return random_dishes

# print(categorizer.categories['beef'])