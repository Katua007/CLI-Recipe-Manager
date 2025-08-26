# Handle user input and call helper functions
# lib/cli.py
from helpers import (
    add_recipe, view_recipes, find_recipe_by_name, delete_recipe, exit_program
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "3":
            find_recipe_by_name()
        # Add other choices for the remaining user stories
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\n--- CLI Recipe Manager ---")
    print("1. Add a new recipe")
    print("2. View all recipes")
    print("3. Search for a recipe")
    # Add more options based on your user stories
    print("0. Exit")

if __name__ == "__main__":
    main()