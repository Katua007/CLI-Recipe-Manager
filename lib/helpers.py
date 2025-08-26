# Where core logic for each menu option will go
# lib/helpers.py
from lib.models import session
from lib.models.recipe import Recipe
from lib.models.category import Category
from lib.models.ingredient import Ingredient

def find_recipe_by_name():
    """Finds and displays a recipe by its name."""
    recipe_name = input("Enter the name of the recipe you want to find: ")
    # Use SQLAlchemy to query the database for a recipe with that name.
    # The .first() method returns the first matching result or None if not found.
    recipe = session.query(Recipe).filter(Recipe.name.like(f"%{recipe_name}%")).first()

    if recipe:
        print("\n--- Recipe Found! ---")
        print(f"Name: {recipe.name}")
        print(f"Instructions: {recipe.instructions}")
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(f"- {ingredient.name} ({ingredient.quantity})")
    else:
        print(f"No recipe found with the name '{recipe_name}'.")

# Other helper functions like add_recipe(), view_recipes(), etc., go here.

def exit_program():
    print("Goodbye!")
    exit()

def add_recipe():
    name = input("Enter recipe name: ")
    instructions = input("Enter instructions: ")

    # User story 6: Categorize recipes
    category_name = input("Enter category (e.g., Breakfast, Dinner): ")
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        print("Category not found. Creating a new one.")
        category = Category.create(name=category_name)

    try:
        new_recipe = Recipe(name=name, instructions=instructions, category=category)
        session.add(new_recipe)
        session.commit()
        print(f"Recipe '{name}' added successfully!")

        # User story 1: Add ingredients (lists/dicts)
        while True:
            ingredient_name = input("Enter an ingredient name (or 'done' to finish): ")
            if ingredient_name.lower() == 'done':
                break
            quantity = input("Enter quantity (e.g., '1 cup'): ")
            ingredient = Ingredient(name=ingredient_name, quantity=quantity, recipe=new_recipe)
            session.add(ingredient)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error adding recipe: {e}")

def view_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    print("\n--- Your Recipes ---")
    for recipe in recipes:
        print(f"- {recipe.name}")

def delete_recipe():
    """Deletes a recipe from the database."""
    recipe_name = input("Enter the name of the recipe to delete: ")
    recipe_to_delete = session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe_to_delete:
        confirmation = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ").lower()
        if confirmation == 'yes':
            try:
                session.delete(recipe_to_delete)
                session.commit()
                print(f"Recipe '{recipe_to_delete.name}' has been deleted.")
            except Exception as e:
                session.rollback()
                print(f"An error occurred while deleting the recipe: {e}")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Recipe '{recipe_name}' not found.")

# Implement the other functions for user stories 3, 4, 5, etc.
# Make sure to handle input validation and provide clear error messages.