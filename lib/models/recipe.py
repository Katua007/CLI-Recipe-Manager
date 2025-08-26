# lib/models/recipe.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, session
from .ingredient import Ingredient

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    instructions = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='recipes')
    ingredients = relationship('Ingredient', back_populates='recipe', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Recipe(name="{self.name}")>'

    # Add ORM methods here (create, delete, get_all, find_by_id)
    # The 'create' method should handle the category relationship.