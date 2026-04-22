Productivity App API
A Flask-based backend for managing tasks, featuring user authentication and full CRUD functionality.

Features
User Auth: Signup, Login, and Logout functionality with Bcrypt password hashing.

Session Management: Uses Flask sessions to track logged-in users.

Task CRUD: Users can create, view, update, and delete their own tasks.

Database: SQLAlchemy with migrations managed via Flask-Migrate.

Clean Structure: Project organized into Models, Schemas (Marshmallow), and Routes blueprints.

Tech Stack
Python 3.x

Flask (Web Framework)

SQLAlchemy (ORM)

Marshmallow (Serialization/Validation)

Pipenv (Dependency Management)

Setup & Installation
1. Clone the repo
Bash
git clone https://github.com/jareelireri-ops/productivity-app.git
cd productivity-app
2. Environment Setup
I used pipenv to keep dependencies clean. Install them and enter the shell:

Bash
pipenv install
pipenv shell
3. Database Initialization
Run the migrations to create your local productivity.db:

Bash
flask db upgrade
4. Seed Data (Optional)
To populate the database with a test user and tasks:

Bash
python seed.py
5. Run the App
Start the server:

Bash
python app.py
The server will run at http://127.0.0.1:5555.

API Endpoints
Auth
POST /signup - Create a new account.

POST /login - Log in to an existing account.

GET /check_session - Verify the current logged-in user.

DELETE /logout - Clear the session.

Tasks
GET /tasks - Get all tasks for the logged-in user.

POST /tasks - Create a new task.

PATCH /tasks/<id> - Update a specific task.

DELETE /tasks/<id> - Delete a specific task.