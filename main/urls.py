from django.urls import path, include
from register.forms import RegisterForm
from . import views


urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),

]
