# Populate the database with some initial, fake data for testing purposes.

# lib/db/seed.py
from faker import Faker
from lib.models import session
from lib.models.category import Category
from lib.models.recipe import Recipe
from lib.models.ingredient import Ingredient

fake = Faker()

def seed_database():
    print("Seeding database...")
    
    # 1. Clear existing data
    session.query(Category).delete()
    session.query(Recipe).delete()
    session.query(Ingredient).delete()
    session.commit()
    
    # 2. Create and add Category instances
    categories = [
        Category(name='Breakfast'),
        Category(name='Lunch'),
        Category(name='Dinner'),
        Category(name='Dessert')
    ]
    session.add_all(categories)
    session.commit()
    print("Categories created.")
    
    # 3. Create and add Recipe instances
    for _ in range(10): # Create 10 fake recipes
        recipe_name = fake.sentence(nb_words=4)[:-1]
        instructions = fake.paragraph(nb_sentences=5)
        random_category = fake.random_element(categories)
        
        recipe = Recipe(name=recipe_name, instructions=instructions, category=random_category)
        session.add(recipe)
    
    session.commit()
    print("Recipes created.")
    
    # 4. Create and add Ingredient instances for each recipe
    all_recipes = session.query(Recipe).all()
    for recipe in all_recipes:
        for _ in range(3): # Each recipe gets 3 ingredients
            ingredient_name = fake.word()
            quantity = f"{fake.random_int(1, 4)} {fake.word()}"
            ingredient = Ingredient(name=ingredient_name, quantity=quantity, recipe=recipe)
            session.add(ingredient)

    session.commit()
    print("Ingredients created.")
    print("Database seeded successfully! 🎉")

if __name__ == '__main__':
    seed_database()