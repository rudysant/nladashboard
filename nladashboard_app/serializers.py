# serializers.py
from rest_framework import serializers
from .models import Books # Sesuaikan dengan nama model Buku Anda

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        # Mengambil field sesuai kebutuhan Anda
        fields = ['id', 'book_title', 'book_publisher']