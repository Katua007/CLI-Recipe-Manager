# CLI-Recipe-Manager

# Project Description
The CLI Recipe Manager is a command-line interface application designed to help users manage their personal recipe collection. Built using Python, SQLAlchemy, and Alembic, this application allows users to add, view, search, and delete recipes, as well as categorize them for easy organization. The project demonstrates a strong understanding of object-oriented programming (OOP) principles, data structures, and object-relational mapping (ORM) with a relational database.

# Getting Started
To set up and run the application, follow these simple steps:

1. Clone the Repository:

Bash

git clone https://github.com/your-username/cli-recipe-manager.git
cd cli-recipe-manager

2. Set up the Virtual Environment: Use Pipenv to install all necessary dependencies.

Bash

pipenv install
pipenv shell

3. Run Migrations: Initialize the database by running the Alembic migrations.

Bash

alembic upgrade head

4. Seed the Database (Optional): To populate the database with sample data for testing, run the seed script.

Bash

python lib/db/seed.py

5. Run the CLI Application:

Bash

python lib/cli.py

# File Structure and Modules
The project is structured to follow best practices for Python applications, ensuring a clean separation of concerns.

alembic.ini and migrations/: These files are used by Alembic to manage database schema changes (migrations). They allow us to update the database schema in a version-controlled way.

lib/cli.py: This is the main CLI script and the application's entry point. It contains the primary main() function with a while loop that displays the main menu, handles user input, and calls functions from helpers.py to perform tasks. This file is responsible for the user interface.

lib/helpers.py: This module contains the core business logic of the application. It holds functions for each major task (e.g., add_recipe(), view_recipes(), delete_recipe()). These functions interact directly with the ORM models to query and manipulate data, keeping the main cli.py file clean and focused on user interaction.

lib/db/seed.py: This script is used for seeding the database with sample data. It uses the Faker library to generate fake categories, recipes, and ingredients for testing purposes, which is invaluable during development.

lib/models/: This directory contains all the ORM models that define our database schema. It represents the data persistence layer of the application.

lib/models/base.py: This file holds the shared SQLAlchemy objects like Base, engine, and session to avoid circular imports.

lib/models/category.py, lib/models/recipe.py, lib/models/ingredient.py: These files define the Category, Recipe, and Ingredient classes, which are mapped to database tables. They contain class methods for CRUD operations (Create, Read, Update, Delete) and define the relationships between the tables (e.g., Recipe has many Ingredients).

# Learning Goals Achieved
This project demonstrates proficiency in several key learning goals from Phase 3:

Object-Oriented Programming (OOP): The application is built with distinct classes (Category, Recipe, Ingredient) and well-defined methods, showcasing proper encapsulation, inheritance (via SQLAlchemy's declarative base), and a modular design.

Object-Relational Mapping (ORM): We used SQLAlchemy to map Python classes directly to database tables, allowing us to interact with the database using Python objects instead of raw SQL queries. This includes defining relationships like the one-to-many relationship between a Recipe and its Ingredients.

Command-Line Interface (CLI): The application is a fully functional, interactive CLI with a user-friendly menu system, persistent loops, and input validation, all built from scratch using fundamental Python constructs.

Data Structures: The project effectively uses Python's built-in data structures, such as lists and tuples, to handle collections of objects and provide ordered or immutable data.

# External Libraries
SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapper that provides the full power of SQL with the flexibility of Python.

Alembic: A lightweight database migration tool for SQLAlchemy.

Faker: A Python package that generates fake data for populating a database.



