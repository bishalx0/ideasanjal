from django.urls import path
from . views import HomeView, register

# including urlpatterns

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("register/", register, name="register"),
]
