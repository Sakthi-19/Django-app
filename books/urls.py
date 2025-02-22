from django.urls import path
from .views import books, book_detail, book_reviews

urlpatterns = [
    path('books/', books, name='books'),  # Combined GET & POST
    path('books/<str:id>/', book_detail, name='book_detail'),  # GET a single book
    path('books/<str:id>/reviews/', book_reviews, name='book_reviews'),  # Combined GET & POST
]
