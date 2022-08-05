from django.urls import path
from .views import MailView

urlpatterns = [
    path("send_emails/", MailView.as_view()),

]
