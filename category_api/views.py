from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from category_api.models import Category
from category_api.serializer import CategorySerializer


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryCreate(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetails(APIView):
    def get_by_pk(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Category not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        category = self.get_by_pk(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_by_pk(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_by_pk(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
