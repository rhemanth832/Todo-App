📝 To-Do App – Built with Django

This is a simple yet fully functional To-Do List Web Application developed using the Django web framework. The app allows users to manage daily tasks efficiently by adding, editing, marking as complete, and deleting tasks. It demonstrates key backend and frontend integration using Django’s powerful built-in features.

🔧 Features
- 🔐 User Authentication  
  - Sign up, Login, Logout  
  - User-specific tasks (each user can only access their own task list)
- ➕ Task Creation  
  - Add new tasks with title and description  
  - Set task due dates
- ✅ Task Completion  
  - Mark tasks as complete or incomplete  
  - Visual distinction between pending and completed tasks
- 📝 Edit and Delete Tasks  
  - Update task information  
  - Delete tasks permanently
- 📊 Task Filtering  
  - View all tasks, completed tasks, or pending tasks  
  - Organized task dashboard
- 💻 Admin Panel  
  - Built-in Django admin for managing users and tasks

🛠 Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript (Bootstrap)
- Database: SQLite (default, easily switchable to PostgreSQL)
- Authentication: Django’s built-in auth system

📁 Project Structure
todo_app/
├── todo/               # Core app with models, views, URLs, templates
├── users/              # Custom user login/signup handling
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── db.sqlite3          # Default database
└── manage.py           # Django's command-line utility

▶️ How to Run the Project Locally
1. Clone the repository
   git clone https://github.com/your-username/django-todo-app.git
   cd django-todo-app

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install dependencies
   pip install -r requirements.txt

4. Apply migrations
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser (optional for admin panel)
   python manage.py createsuperuser

6. Run the development server
   python manage.py runserver

7. Open in browser
   Visit: http://127.0.0.1:8000/
