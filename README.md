# django-electron-forum
admin-api-for-django-site

# Django Site with API Admin Panel

This project is a Django-based website with a separate application for managing it via an API. The backend is built using Django, and the admin panel (frontend) is a JavaScript application (e.g., built with React) that interacts with the backend via API.

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Backend (Django)

Make sure you have Python and Django installed. Navigate to the folder containing `manage.py` and run:

```bash
python manage.py runserver

This will start the Django development server at: http://127.0.0.1:8000

If needed, install dependencies first:

pip install -r requirements.txt


### 2. Frontend / Admin Panel (npm app)

Navigate to the folder with the frontend app and run:

npm install
npm start

This will start the frontend development server at: http://localhost:3000

🧰 Requirements

-Python 3.8+

-Django

-Node.js and npm

/project-root/
├── backend/                # Django project folder
│   └── manage.py
│   └── ...
├── admin-panel/            # Frontend application
│   └── main.json
│   └── ...
└── README.md


📦 Installation Notes

## 1. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate


## 2. Install backend dependencies:

pip install -r requirements.txt


## 3. Install frontend dependencies:

npm install

📡 API
The Django backend provides a RESTful API for managing site content. API endpoints are typically available under /api/. For example:


## 🧩 API Endpoints

### 1. **GET /api/categories/**

Get a list of all categories.

- **Response**: A list of all categories (e.g., JSON with names and IDs).

### 2. **GET /api/forums/{category_slug}/**

Get a list of forums within a specific category.

- **Response**: A list of forums in the category.

### 3. **GET /api/forum/{forum_id}/messages/**

Get all messages in a forum.

- **Response**: A list of forum messages (e.g., JSON with message text).

### 4. **GET /api/category/{category_id}/**

Get information about a specific category.

- **Response**: Information about the category (e.g., name and description).


## 🧩 API Endpoints

### 1. **POST /api/login/**

Login with credentials:

- **Request Body**:
  {
    "username": "your_username",
    "password": "your_password"
  }
Response:

{
  "token": "dummy-token-123"
}
2. POST /api/category/
Add a new category.

Request Body:
{
  "name": "Category Name",
  "slug": "category-slug"
}

Response: Success message or created category details.

3. POST /api/forum/{category_slug}/
Add a new forum in a specific category.

Request Body:

{
  "title": "Forum Title",
  "description": "Description of the forum"
}
Response: Success message or created forum details.

4. POST /api/forum/{forum_id}/message/
Add a new message in a forum.

Request Body:

{
  "content": "Message content",
  "author": "author_username"
}
Response: Success message or created message details.

5. POST /api/message/{message_id}/delete/
Delete a specific message.

Response: Success message indicating the message was deleted.

6. POST /api/ad/{ad_id}/delete/
Delete a specific ad.

Response: Success message indicating the ad was deleted.



This format should keep the structure clean and readable for the documentation!
