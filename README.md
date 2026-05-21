# Blog API

A RESTful Blog API built with Django REST Framework featuring authentication, CRUD operations, and role-based permissions.

## Features

- User authentication
- CRUD operations for blog posts
- Admin-only create, update, and delete permissions
- Pagination
- SQLite database
- RESTful API structure

## API ENDPOINTS 

| Endpoint           | Method    | Description                             |
| ------------       | --------- | --------------------------------------  |
| blog/posts/        | GET       | List all posts(Authenticated)           |
| blog/posts/<id>/   | GET       | Retrieve single post(Authenticated)     |
| blog/posts/        | POST      | Create post (Admin only)                |
| blog/posts/<id>/   | PUT/PATCH | Update post (Admin only)                |
| blog/posts/<id>/   | DELETE    | Delete post (Admin only)                |


## Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite

## Quick Start

```bash
git clone <repo-url>
cd core

python -m venv env
env\Scripts\activate     # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
