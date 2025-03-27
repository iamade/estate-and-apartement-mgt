from django.urls import path, re_path

from .views import (CustomProviderAuthView, CustomTokenObtainPairView, CustomTokenRefreshView, LogoutAPIView)

urlpatterns = [
    re_path(
        r"^o/(?P<provider>\S+)/$",CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
    path("login/", CustomTokenObtainPairView.as_view()),
    path("refresh/", CustomTokenRefreshView.as_view()),
    path("login/", LogoutAPIView.as_view()),
]