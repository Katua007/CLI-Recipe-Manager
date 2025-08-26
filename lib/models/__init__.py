# lib/models/__init__.py
from .base import session, Base # Import Base and session from the new base.py file

# Import all of your models here. The order doesn't matter for Alembic, but it's good practice.
from .category import Category
from .recipe import Recipe
from .ingredient import Ingredient