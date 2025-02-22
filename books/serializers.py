from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField()

class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    publication_year = serializers.IntegerField()
    genre = serializers.CharField()
    reviews = ReviewSerializer(many=True, required=False)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        return instance
