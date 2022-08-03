from django.urls import path
from .views import UserMailView, AdminMailView

urlpatterns = [
    path("send_emails1/", UserMailView.as_view()),
    path("send_emails2/", AdminMailView.as_view())
]
