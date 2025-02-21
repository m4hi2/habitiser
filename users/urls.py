from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import register

urlpatterns = [
    path("register/", register, name="register"),
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html", next_page="dashboard_index"
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
