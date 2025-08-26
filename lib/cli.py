# Handle user input and call helper functions
import sys
from pathlib import Path

# Get the project's root directory and add it to the system path.
# This ensures that 'lib' is a recognized package.
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# lib/cli.py


from lib.helpers import (
    # ... other imports
    add_recipe,
    delete_recipe,
    find_recipe_by_name,
    view_recipes,  # Added missing import
    view_recipes_by_category, # New import for viewing by category
    exit_program
)

def main():
    while True:
        print("\n--- CLI Recipe Manager ---")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. Find a recipe by name")
        print("4. Delete a recipe") # New menu option
        print("5. View recipes by category") # New menu option
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            find_recipe_by_name()
        elif choice == '4':
            delete_recipe() # Call the new delete function
        elif choice == '5':
            view_recipes_by_category() # Call the new view by category function
        elif choice == '0':
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()