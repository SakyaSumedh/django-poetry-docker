from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    # Serve Media and Static files
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    from django.views.generic import RedirectView

    from .swagger_view import drf_yasg_swagger_view

    urlpatterns += [
        path("", RedirectView.as_view(url="/api/doc", permanent=True)),
        path(
            "api/doc",
            drf_yasg_swagger_view.with_ui("swagger", cache_timeout=0),
            name="drf_yasg_swagger_view",
        ),
        path(
            "api/redoc",
            drf_yasg_swagger_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
