from django.db import connection
from .models import Tenant


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_name = self.get_tenant_name_from_request(request)
        try:
            tenant = Tenant.objects.get(name=tenant_name)
            connection.set_tenant(tenant)
        except Tenant.DoesNotExist:
            pass

        response = self.get_response(request)
        return response

    def get_tenant_name_from_request(self, request):
        return request.META.get("HTTP_HOST").split(".")[0]
