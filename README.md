# Django Travel Companion App

## Description

The **Django Travel Companion App** is a web application built using the Django framework designed to help users manage and share their travel experiences. Users can sign up, log in, create trips, and add detailed notes about excursions, experiences, and events during their travels. This app allows for easy trip planning, travel journaling, and connecting with fellow travelers.

### Key Features:
- **User Authentication**: Allows users to sign up, log in, and manage their accounts.
- **Trip Management**: Users can create and manage their trips, specifying destinations, start and end dates, and more.
- **Notes for Excursions**: Add and categorize notes related to trips, such as events, dining experiences, and general travel tips.
- **Ratings**: Rate experiences on a scale from 1 to 5 stars.
- **Admin Dashboard**: Manage trips, notes, and user data through the Django Admin interface.
- **Tailwind CSS**: Utilized for modern and responsive front-end design.

---

## Technologies Used

- **Django**: Web framework for the backend.
- **SQLite**: Default database (can be replaced with PostgreSQL or MySQL).
- **Tailwind CSS**: Front-end framework for styling.
- **Pillow**: Python Imaging Library for handling images in the app.
- **Django Crispy Forms**: For rendering Django forms with Tailwind CSS.

---

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git (for version control)

### Steps

1. **Clone the repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/ayushgoyal04/django-travel-companion-app.git
   cd django-travel-companion-app

2. **Clone the repository**
   It’s a good practice to create a virtual environment for your project. This ensures that dependencies are isolated and won't conflict with other Python projects on your system.
-  MacOS
python3 -m venv venv
source venv/bin/activate  # Activating the virtual environment
- Windows
python -m venv venv
venv\Scripts\activate  # Activating the virtual environment

3. **Install dependencies**
   After activating the virtual environment, install the required dependencies using pip:
pip install -r requirements.txt

4. **Apply migrations**
   Now that the dependencies are installed, apply the database migrations to set up your database:
python manage.py migrate

5. **Create a superuser (for accessing the Django admin panel)**
Create a superuser to access the Django admin interface, where you can manage trips and notes:
python manage.py createsuperuser

6. **Run the development server**
   You are now ready to run the application! Start the Django development server:
python manage.py runserver

