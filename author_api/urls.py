from django.urls import path
from author_api.views import AuthorList, AuthorCreate, AuthorDetails

urlpatterns = [
    path('list/', AuthorList.as_view()),
    path('', AuthorCreate.as_view()),
    path('<int:pk>', AuthorDetails.as_view())
]
