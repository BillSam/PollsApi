from django.urls import path
from .views import poll_list, poll_details

urlpatterns = [
    path("polls/", poll_list, name="polls_list"),
    path("polls/<int:pk>", poll_details, name="polls_details")
]