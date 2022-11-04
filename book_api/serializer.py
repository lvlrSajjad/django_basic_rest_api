# from rest_framework import serializers
# from book_api.models import Book
#
#
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
#         instance.publish_date = validated_data.get('publish_date', instance.publish_date)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.save()
#         return instance

from rest_framework import serializers
from book_api.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


