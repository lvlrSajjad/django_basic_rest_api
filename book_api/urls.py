from django.contrib import admin
from django.urls import path
# from book_api.views import book_list, book_create, book
from book_api.views import BookList, BookCreate, BookDetails

urlpatterns = [
    # path('<int:pk>', book),
    # path('', book_create),
    # path('list/', book_list)
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetails.as_view())
]
