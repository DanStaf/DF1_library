from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from libr.models import Author, Book, Reading


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    is_returned = serializers.SerializerMethodField(read_only=True)

    def get_is_returned(self, obj):
        reading_list = Reading.objects.filter(book=obj, is_returned=False)
        print(reading_list)
        return False if reading_list else True

    class Meta:
        model = Book
        fields = "__all__"


class ReadingSerializer(ModelSerializer):
    class Meta:
        model = Reading
        fields = "__all__"
