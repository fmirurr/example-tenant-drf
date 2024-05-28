from django.urls import path

from .views import Blog_APIView

urlpatterns = [
    path("create/", Blog_APIView.as_view()),
]