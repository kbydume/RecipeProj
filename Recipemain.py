import csv
import random
from recipe import Recipe
from recipebook import RecipeBook
from manage import Manager


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
            get_recommendation(recipe_book)
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


def get_recommendation(recipe_book):
    """
    Prints a randomly selected recipe from the recipe book.

    Args:
        recipe_book (RecipeBook): The recipe book to get a recommendation from.
    """
    if len(recipe_book.get_all_recipes()) == 0:
        print("There are no recipes in the recipe book.")
        return

    recipe = random.choice(recipe_book.get_all_recipes())
    print("\nHere's a recipe you might like:")
    print(recipe)


def save_to_csv(recipe_book):
    """
    Saves the recipes in the recipe book to a CSV file.

    Args:
        recipe_book (RecipeBook): The recipe book containing the recipes to save.
    """
    with open("recipe.csv", mode="w", newline="") as file:
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
        with open("recipe.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                title, ingredients, instructions = row
                recipe = Recipe(title, ingredients.split(","), instructions)
                recipe_book.add_recipe(recipe)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
