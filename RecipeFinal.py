import csv
import random
from recipe import Recipe
from recipebook import RecipeBook
from manage import Manager
from Categorize import get_recommendations, Categorize
from recommendation import Recommendation

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
        print("3. Get a specific recommendation")
        print("4. Delete a recipe")
        print("5. Edit a recipe")
        print("6. Quit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1-6.")
            continue

        if choice == 1:
            add_recipe(recipe_book)
            save_to_csv(recipe_book)
        elif choice == 2:
            get_recommendation()
        elif choice == 3:
            specific_recommendations()
        elif choice == 4:
            recipe_title = input("Enter the title of the recipe you want to delete: ")
            manager.delete_recipe(recipe_title)
            save_to_csv(recipe_book)
        elif choice == 5:
            recipe_title = input("Enter the title of the recipe you want to edit: ")
            manager.edit_recipe(recipe_title)
            save_to_csv(recipe_book)
        elif choice == 6:
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

def get_recommendation():
    """
    Prints a randomly selected recipe from the recipe book.

    Args:
        recipe_book (RecipeBook): The recipe book to get a recommendation from.
    """
    categorizer = Categorize('recipe.csv')
    meat_options = list(categorizer.get_meat_categories().keys())
    style_options = list(categorizer.get_cooking_styles().keys())

    while True:
        get_meat = input("What kind of food would you like? These are the options: "
                         f"{', '.join(meat_options).capitalize()}\n---> ").lower()
        if get_meat not in meat_options:
            print("Invalid option. Please choose from the available options.")
            continue
        break

    while True:
        get_style = input("What is your preferred cooking style? "
                          f"{', '.join(style_options).capitalize()}\n--->  ").lower()
        if get_style not in style_options:
            print("Invalid option. Please choose from the available options.")
            continue
        break

    recipe = get_recommendations(get_meat, get_style)
    if len(recipe) > 0:
        print("\nHere's a recipe you might like:")
        print(recipe[0])
        if len(recipe) > 1:
            print("\nHere's another recipe you might like:")
            print(recipe[1])
    else:
        print("\nSorry, there are no recipes that follow those preferences.")
          
def specific_recommendations():
    r = Recommendation('recipe.csv')
    print("Provide any ingredient and a recipe that includes that food "
          "will be provided!\n")
    keyword = input('What would you like to eat: ')
    recommendations = r.get_recommendations(keyword)
    print(f"Here are some '{keyword}' option(s): ")
    for r in recommendations:
        print(r)


def save_to_csv(recipe_book):
    """
    Saves the recipes in the recipe book to a CSV file.

    Args:
        recipe_book (RecipeBook): The recipe book containing the recipes to save.
    """
    try:
        with open("recipe.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            for recipe in recipe_book.get_all_recipes():
                writer.writerow([recipe.get_title(), ",".join(recipe.get_ingredients()), recipe.get_instructions()])
    except IOError as e:
        print(f"Error saving to CSV file: {e}")

def load_from_csv(recipe_book):
    """
    Loads recipes from a CSV file and adds them to the recipe book.

    Args:
        recipe_book (RecipeBook): The recipe book to add the loaded recipes to.
    """
    try:
        with open("recipe.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                title, ingredients, instructions = row
                recipe = Recipe(title, ingredients.split(","), instructions)
                recipe_book.add_recipe(recipe)
    except FileNotFoundError:
        print("recipe.csv not found. Starting with an empty recipe book.")
    except IOError as e:
        print(f"Error loading from CSV file: {e}")

if __name__ == "__main__":
    main()

