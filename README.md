# Multi-Company Employee Management System

A simple Employee Management System built with Django.

## Features

- **View Employees**: List all current employees.
- **Add Employee**: Form to add new employee details.
- **Update Employee**: Edit existing employee information.
- **Delete Employee**: Remove an employee from the records.

## Prerequisites

- Python 3.x installed.
- `pip` package manager.

## Installation and Setup

1.  **Clone or Download** the repository to your local machine.

2.  **Navigate** to the project directory:
    ```bash
    cd Multi-Company-Employee-Management-System
    ```

3.  **Install Django** (if not already installed):
    ```bash
    pip install django
    ```

4.  **Run Migrations** (optional, but recommended to ensure database is set up):
    ```bash
    python manage.py migrate
    ```

5.  **Create Admin User** (to access the Admin Portal):
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username and password.

6.  **Run the Server**:
    ```bash
    python manage.py runserver
    ```

6.  **Access the Application**:
    Open your web browser and go to:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    You will see a landing page with options to go to the **Admin Portal** or the **Employee System**.

## Project Structure

- `manage.py`: Django's command-line utility.
- `main/`: Project configuration (settings, urls, etc).
- `employees/`: Main application containing views, models, and templates.
    - `templates/`: HTML templates for the UI.
    - `urls.py`: URL routing for the employees app.
    - `views.py`: Logic for handling requests.

## Usage

- **Home Page**: Displays the table of employees.
- **Add Employee**: Click "Add Employee" in the navbar to add a new record.
- **Actions**: Use the "Update" or "Delete" buttons in the table to manage records.