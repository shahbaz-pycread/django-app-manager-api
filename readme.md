# Django API for App Management

## Description
This project is a simple Django-based API that allows you to manage apps in a database. It provides three key functionalities:
1. Add new app details to the database.
2. Retrieve details of an app by its ID.
3. Delete an app by its ID.

The project uses Django and Django REST Framework for building the API, and SQLite (by default) for managing the database.

## Endpoints

1. **POST** `/api/add-app/`
   - Add app details (fields: `app_name`, `version`, `description`).
   - Example payload:
   ```json
   {
       "app_name": "TaskMaster",
       "version": "2.5",
       "description": "A task management app that helps users track and complete daily tasks efficiently."
   }
2. **GET** `/api/get-app/{id}/`

Retrieve app details by ID.
Example request: /api/get-app/1/

3. **DELETE** ` /api/delete-app/{id}/`

Delete an app by ID.
Example request: /api/delete-app/1/

Setup Instructions
1. Clone the repository
   - git clone https://github.com/yourusername/yourproject.git
   - cd yourproject
     
2. Install Dependencies
   - pip install -r requirements.txt
     
3. Setup Database
Run the following commands to apply migrations and set up the database:
   - python manage.py makemigrations
   - python manage.py migrate
     
4. Load Sample Data
If a sample_data.json file is provided, load sample data using:
   - python manage.py loaddata sample_data.json
     
5. Run the Server. Start the Django development server:
   - python manage.py runserver
The server will be available at http://127.0.0.1:8000/.

6. Testing the API
Use a tool like Postman or cURL to test the API.

Example cURL command to add an app:

**curl -X POST -H "Content-Type: application/json" -d '{"app_name": "FitTrack", "version": "1.2", "description": "A fitness tracking app"}' http://127.0.0.1:8000/api/add-app/**

**Database Schema**

The database schema includes the following fields in the App table:

 1. id: Primary key (auto-incremented).
 2. app_name: Name of the app (string, max length 100).
 3. version: Version of the app (string, max length 20).
 4. description: Description of the app (text).

**Sample Data**

The following are some dummy data entries to test the API:

 1. TaskMaster - Version 2.5 - "A task management app that helps users track and complete daily tasks efficiently."
 2. FitTrack - Version 1.2 - "A fitness tracking app that monitors user activity, steps, and workouts."
 3. BookBuddies - Version 3.0 - "An app that allows book lovers to catalog, review, and recommend books to their friends."
 4. PhotoEditorX - Version 4.1 - "A simple photo editing app with filters and photo enhancement features."
 5. BudgetWise - Version 1.0 - "A budget management app that helps users track expenses and savings goals."
