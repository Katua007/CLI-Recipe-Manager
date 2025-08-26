# lib/models/ingredient.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, session

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(String, nullable=True) # e.g., "1 cup", "2 cloves"
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship('Recipe', back_populates='ingredients')

    def __repr__(self):
        return f'<Ingredient(name="{self.name}", quantity="{self.quantity}")>'
    # Add ORM methods here