# Django CRM

Django CRM is a web application built with Django that allows users to manage customer records with functionalities for login, registration, adding, updating, and deleting records.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Record Management**: Authenticated users can add, update, and delete customer records.
- **Record Display**: Displays a list of records with details such as name, email, phone, address, city, state, zipcode, and creation time.
- **User Interface**: Bootstrap-based for a responsive and modern look.

## Prerequisites

- Python 3.8 or newer
- Django 4.0 or newer
- MySQL

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/django-crm.git
   cd django-crm

2. **Create and Activate a Virtual Environmenty**

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Configure the Database**
   ```bash
   python mydb.py

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Create a Django Superuser**
   ```bash
   python manage.py createsuperuser
7. **Run the Server**
   ```bash
   python manage.py runserver

8. **Access the Application**
   Open your browser and navigate to http://127.0.0.1:8000/.

## Project Structure

```plaintext
mysite/
  ├── __init__.py
  ├── settings.py
  ├── urls.py
  ├── wsgi.py
  └── crmapp/
      ├── migrations/
      │   └── __init__.py
      ├── __init__.py
      ├── admin.py
      ├── apps.py
      ├── forms.py
      ├── models.py
      ├── tests.py
      ├── views.py
      ├── templates/
      │   ├── base.html
      │   ├── home.html
      │   ├── add_record.html
      │   ├── record.html
      │   ├── register.html
      │   ├── update_record.html
      │   └── navbar.html
      └── static/
  ├── urls.py
  ├── manage.py
  ├── requirements.txt
  └── mydb.py
