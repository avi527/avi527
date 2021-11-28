from rest_framework import serializers
from .models import Libraries,Books,Library_books,Users,Library_activites


class BooksSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    author_name = serializers.CharField(max_length=100)
    isbn_num = serializers.CharField(required=True)
    genre = serializers.CharField(max_length=100)
    discription = serializers.CharField(max_length=1000)


    def create(self, validated_data):
        return Books.objects.create(**validated_data)


class LibrariesSerializer(serializers.Serializer):
    libraries_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True,max_length=100)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    postal_code = serializers.CharField(max_length=10)


    def create(self, validated_data):
        return Libraries.objects.create(**validated_data)

class LibraryBookRecordSerializer(serializers.ModelSerializer):
    lib = LibrariesSerializer(read_only=True,many=True)
    book = BooksSerializer(read_only=True,many=True)
    class Meta:
        model = Library_books
        fields = "__all__"


class LibraryBookInOutSerializer(serializers.ModelSerializer):
    # user = Library_activites(read_only=True,many=True)
    lib = LibraryBookRecordSerializer(read_only=True,many=True)
    class Meta:
        model = Library_activites
        fields = "__all__"








