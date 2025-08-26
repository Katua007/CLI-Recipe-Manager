# Where core logic for each menu option will go
# lib/helpers.py
from lib.models import session
from lib.models.recipe import Recipe
from lib.models.category import Category
from lib.models.ingredient import Ingredient

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

# Implement the other functions for user stories 3, 4, 5, etc.
# Make sure to handle input validation and provide clear error messages.