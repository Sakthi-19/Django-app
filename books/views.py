from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.create(serializer.validated_data)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_detail(request, id):
    book = Book.objects(id=id).first()
    if not book:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(BookSerializer(book).data)

@api_view(['GET', 'POST'])
def book_reviews(request, id):
    book = Book.objects(id=id).first()
    if not book:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(book.reviews, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            book.reviews.append(Review(**serializer.validated_data))
            book.save()
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
