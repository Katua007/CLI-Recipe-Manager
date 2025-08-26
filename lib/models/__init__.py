# lib/models/__init__.py
from .base import session, Base # Import Base and session from the new base.py file

# Import all of your models here. 
from .category import Category
from .recipe import Recipe
from .ingredient import Ingredient