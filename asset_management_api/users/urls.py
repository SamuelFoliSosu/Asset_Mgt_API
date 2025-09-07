from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterView, LogoutView, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', include(router.urls)),
]
