from rest_framework import viewsets
from .models import Tenant
from rest_framework.response import Response
from .serializers import TenantSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantAPIView(APIView):
    def post(self, request, format=None):
        serializer = TenantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tenant = serializer.save()
        data = TenantSerializer(tenant).data
        return Response(data, status=status.HTTP_201_CREATED)