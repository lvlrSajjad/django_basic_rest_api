from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from author_api.models import Author
from author_api.serializer import AuthorSerializer


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class AuthorCreate(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetails(APIView):
    def get_by_pk(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Author not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        author = self.get_by_pk(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_by_pk(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_by_pk(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
