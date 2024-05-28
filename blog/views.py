from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SomeModelModelSerializer

from .models import SomeModel


# Create your views here.
class Blog_APIView(APIView):
    def post(self, request, format=None):
        serializer = SomeModelModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.save()
        data = SomeModel(blog).data
        return Response(data, status=status.HTTP_201_CREATED)
