"""mycv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from mycv_django.apps.businesses.views import BusinessViewSet
from mycv_django.apps.collaborations.views import CollaborationViewSet
from mycv_django.apps.collaborators.views import (
    DeveloperViewSet,
    ManagerViewSet,
)
from mycv_django.apps.projects.views import ProjectViewSet
from mycv_django.apps.technologies.views import TechnologyViewSet
from mycv_django.apps.users.views import UsersViewSet

schema_view_yasg = get_schema_view(
    openapi.Info(
        title="MyCV API",
        default_version='v0.1',
        description="MyCV Django API",
        contact=openapi.Contact(email="diogo.gomes77@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'developers', DeveloperViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'users', UsersViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'collaborations', CollaborationViewSet)
router.register(r'businesses', BusinessViewSet)
router.register(r'technologies', TechnologyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('redoc/', schema_view_yasg.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('api-docs/', schema_view_yasg.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
