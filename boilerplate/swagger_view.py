from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

swagger_info = openapi.Info(
    title="Boilerplate APIs",
    default_version="v1",
    description="APIs of Boilerplate",
    contact=openapi.Contact(email="sumedhshakya11@gmail.com"),
    license=openapi.License(name="BSD License"),
)


drf_yasg_swagger_view = get_schema_view(
    swagger_info,
    public=False,
    permission_classes=[permissions.AllowAny],
)
