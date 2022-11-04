from django.urls import path
from category_api.views import CategoryList, CategoryCreate, CategoryDetails

urlpatterns = [
    path('list/', CategoryList.as_view()),
    path('', CategoryCreate.as_view()),
    path('<int:pk>', CategoryDetails.as_view())
]
