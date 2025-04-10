from typing import List

from django.urls import URLPattern, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Cafe EM API",
        default_version="v1",
        description="Cafe EM API",
        license=openapi.License(name="MIT License"),
    ),
)
urlpatterns: List[URLPattern] = [
    # path(
    #     r"swagger/",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    path(r"redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
