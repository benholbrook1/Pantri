# Pantri
**Pantri – Your Smarter Pantry Organizer**    Keep track of your food, reduce waste, and never run out of groceries again. Pantri helps you manage expiry dates, plan meals, and create shopping lists—so you always know what’s in stock. Simple, smart, and stress-free! 🍎📦





## Personal Documentation (Notes to self on how to use this project / how to use Django)

to active the virtual environment:
pipenv shell   (from the project root directory)

to install the dependencies:
pipenv install

to run the server:
python manage.py runserver (from src directory)

to make migrations:
python manage.py makemigrations (from src directory)

to apply migrations:
python manage.py migrate (from src directory)

to revert migrations (in DB, then we need to revert the model changes):
python manage.py migrate pantri <migration_number> (from src directory)