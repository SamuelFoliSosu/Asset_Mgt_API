"""
URL configuration for asset_management_api project.
...
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from users.views import RegisterView, LogoutView

swagger_schema_view = get_schema_view(
    openapi.Info(
      title='Asset Management API',
      default_version='v1',
      description='API documentation for Asset Management',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('api/register/', RegisterView.as_view(), name='register'),
    # path('api/login/', obtain_auth_token, name='login'),
    # path('api/logout/', LogoutView.as_view(), name='logout'),

    # path('api/departments/', include('departments.urls')),
    # path('api/locations/', include('locations.urls')),
    # path('api/users/', include('users.urls')),
    # path('api/roles/', include('roles.urls')),
    # path('api/owners/', include('owners.urls')),
    # path('api/assets/', include('assets.urls')),
    # path('api/ownership-history/', include('ownership_history.urls')),
    # path('api/maintenance-logs/', include('maintenance_logs.urls')),
    # path('api/asset-status/', include('asset_status.urls')),
    # path('api/asset-status-history/', include('asset_status_history.urls')),

    path('swagger/', swagger_schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', swagger_schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)