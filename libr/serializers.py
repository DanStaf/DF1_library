from rest_framework.serializers import ModelSerializer

from libr.models import Author, Book, Reading


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ReadingSerializer(ModelSerializer):
    class Meta:
        model = Reading
        fields = "__all__"
