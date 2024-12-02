from django.urls import path
from . import views

app_name = "weatherApp"

urlpatterns = [
	path("", views.index, name="index"),
	path("getFive", views.getFive, name="getFive"),
	path("getSingle", views.getSingle, name="getSingle"),
	path("getFromDB", views.getFromDB, name="getFromDB"),
]