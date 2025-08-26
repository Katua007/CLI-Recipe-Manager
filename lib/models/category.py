# lib/models/category.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import Base, session

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    recipes = relationship('Recipe', back_populates='category')

    def __repr__(self):
        return f'<Category(name="{self.name}")>'

    @classmethod
    def create(cls, name):
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category
    # Add other ORM methods (delete, get_all, find_by_id) as needed