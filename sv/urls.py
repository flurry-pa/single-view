from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app.settings import SPECTACULAR_SETTINGS as SS

from api.routers import router


schema_view = get_schema_view(
   openapi.Info(
      title=SS.get("title"),
      default_version=SS.get("version"),
      description=SS.get("description"),
      terms_of_service=SS.get("terms_of_service"),
      contact=openapi.Contact(email=SS.get("contact")),
      license=openapi.License(name=SS.get("license")),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

app_name = 'sv'
urlpatterns = [
    re_path(r'^api/v1/', include(router.urls)),
]

# API URLS
urlpatterns += [
    re_path(
        r'^swagger(?P<format>\.json)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
