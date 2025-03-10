# Book Review Web Application
A RESTful API for managing a collection of books and user reviews, built with Django REST Framework (DRF) and MongoDB, and deployed using Docker.

## Features  
- Add, View, and Retrieve Books  
- Add and Fetch Reviews for Books  
- RESTful API Endpoints  
- MongoDB Integration
- Dockerized Setup  

## Setup Instructions
- Clone the Repository
    - git clone https://github.com/Sakthi-19/Django-app.git
    - cd Django-app
- Create a Virtual Environment (Optional)
    - python -m venv venv
    - source venv/bin/activate  # macOS/Linux
    - venv\Scripts\activate  # Windows
- Install Dependencies
    - pip install -r requirements.txt
- Configure MongoDB Connection
    - Update .env file with MongoDB credentials:
    - MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database_name>
- Run Django Server Locally
    - python manage.py runserver
    - API is available at:
      - http://127.0.0.1:8000/

## Running with Docker
- Build the Docker Image
     - docker build -t django-book-api .
- Run the Docker Container
     - docker-compose up -d
 
## API Endpoints
- Books API
     - POST	{base_url}/api/books/	Add a new book
          - Request
               - {
                     "title": "The Alchemist",
                     "author": "Paulo Coelho",
                     "publication_year": 1988,
                     "genre": "Fiction",
                     "reviews": []
                 }
     - GET {base_url}/api/books/	List all books
     - GET {base_url}/api/books/{id}/	Get book details + reviews
- Reviews API
     - POST {base_url}/api/books/{id}/reviews/	Add a review
          - {
                "rating": 5,
                "comment": "An amazing book!"
            }
    - GET {base_url}/api/books/{id}/reviews/	Get all reviews
