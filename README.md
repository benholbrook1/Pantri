# Pantri
**Pantri – Your Smarter Pantry Organizer**    Keep track of your food, reduce waste, and never run out of groceries again. Pantri helps you manage expiry dates, plan meals, and create shopping lists—so you always know what’s in stock. Simple, smart, and stress-free! 🍎📦





## Personal Documentation (Notes to self on how to use this project / how to use Django)

to active the virtual environment:
pipenv shell   (from the project root directory)

to install the dependencies:
pipenv install

to run the server: (from src directory)
python manage.py runserver

to make migrations: (from src directory)
python manage.py makemigrations 

to apply migrations: (from src directory)
python manage.py migrate 

to revert migrations (in DB, then we need to revert the model changes): (from src directory)
python manage.py migrate pantri <migration_number> 