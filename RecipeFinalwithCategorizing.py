#Notes for meeting
# Documentation
# Error Handling
# Unit Tests
# Docstrings 
import csv
import random
from recipe import Recipe
from recipebook import RecipeBook
from manage import Manager
from Categorize import get_recommendations, Categorize


def main():
    """
    The main function of the program, presenting the user with a menu to add, get, delete, or edit recipes, and quit the program.
    """
    recipe_book = RecipeBook()
    load_from_csv(recipe_book)
    manager = Manager(recipe_book)

    while True:
        print("\nWelcome to the recipe program!")
        print("What would you like to do?")
        print("1. Add a new recipe")
        print("2. Get a recipe recommendation")
        print("3. Delete a recipe")
        print("4. Edit a recipe")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_recipe(recipe_book)
            save_to_csv(recipe_book)
        elif choice == "2":
            get_recommendation()
        elif choice == "3":
            recipe_title = input("Enter the title of the recipe you want to delete: ")
            manager.delete_recipe(recipe_title)
            save_to_csv(recipe_book)
        elif choice == "4":
            recipe_title = input("Enter the title of the recipe you want to edit: ")
            manager.edit_recipe(recipe_title)
            save_to_csv(recipe_book)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    # file_name = 'recipe.csv'

    # categorizer = Categorize(file_name)
    # categorizer.categorize_recipes()
    # categorized_recipes = categorizer.get_categories()

def add_recipe(recipe_book):
    """
    Adds a new recipe to the recipe book.

    Args:
        recipe_book (RecipeBook): The recipe book to add the recipe to.
    """
    title = input("Enter the title of the recipe: ")
    ingredients = input("Enter the ingredients (separated by commas): ").split(",")
    instructions = input("Enter the instructions: ")
    recipe = Recipe(title, ingredients, instructions)
    recipe_book.add_recipe(recipe)
    print(f"\n{title} has been added to the recipe book.")
    manager_choice = input("Would you like to edit or delete an existing recipe? (y/n): ")
    if manager_choice == "y":
        manager = Manager(recipe_book)
        manager.manage_recipe()


def get_recommendation():
    """
    Prints a randomly selected recipe from the recipe book.

    Args:
        recipe_book (RecipeBook): The recipe book to get a recommendation from.
    """
    get_meat=input("What kind of food would you like? \n")
    get_style=input("What kind of cooking style you want?\n")
    get_meat=get_meat.lower()
    get_style=get_style.lower()
    # print("\nHere's a recipe you might like:")
    recipe=get_recommendations(get_meat,get_style)
    print("\nHere's a recipe you might like:")
    print(recipe[0]+"\n"+recipe[1])


def save_to_csv(recipe_book):
    """
    Saves the recipes in the recipe book to a CSV file.

    Args:
        recipe_book (RecipeBook): The recipe book containing the recipes to save.
    """
    with open("recipez.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for recipe in recipe_book.get_all_recipes():
            writer.writerow([recipe.get_title(), ",".join(recipe.get_ingredients()), recipe.get_instructions()])


def load_from_csv(recipe_book):
    """
    Loads recipes from a CSV file and adds them to the recipe book.

    Args:
        recipe_book (RecipeBook): The recipe book to add the loaded recipes to.
    """
    try:
        with open("recipez.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                title, ingredients, instructions = row
                recipe = Recipe(title, ingredients.split(","), instructions)
                recipe_book.add_recipe(recipe)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()