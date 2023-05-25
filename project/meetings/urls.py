from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("meetings", views.meetings, name="meetings"),
    path("add_meeting", views.add_meeting, name="add-meeting"),
    path("delete_meeting/<meeting_id>", views.delete_meeting, name= 'delete-meeting'),
    path("update_meeting/<meeting_id>", views.update_meeting, name= 'update-meeting'),
]