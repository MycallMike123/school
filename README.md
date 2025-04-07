# Secondary School DBMS

A full-stack Database Management System for Secondary Schools, built with Django and Bootstrap.

## 🔧 Features

- 🔐 Admin, Teacher, and Parent login
- 🎓 Student & Subject registration
- 📝 Exam result entry by teachers
- 📊 Result analysis (average, grades, rankings)
- 🧾 Report form generation (printable)
- 👨‍👩‍👧‍👦 Parent portal for performance monitoring

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, Bootstrap, Crispy Forms
- **Database**: SQLite (default), easily switchable to PostgreSQL
- **Others**: Django Admin, PDF export (coming soon)

## 🖥️ Getting Started

### Clone the Repo
```bash
git clone <your-repo-url>

cd school-dbms

Set up a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run the server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Create admin user
bash
Copy
Edit
python manage.py createsuperuser
📁 Project Structure
core/: Main app for user roles, models, views

templates/: HTML templates with Bootstrap

static/: Static files (CSS, JS)

schooldbms/: Project settings

📌 Upcoming Features
PDF Report cards

Bulk student import

SMS/email alerts to parents

Full API (Node.js microservice)

Advanced analytics dashboard
