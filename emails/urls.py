from django.urls import path
from .views import MailView

urlpatterns = [
    path("send_emails/", MailView.as_view()),
    # path("send_emails2/", AdminMailView.as_view())
]
