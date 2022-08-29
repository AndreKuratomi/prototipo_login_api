from django.urls import path
from .views import RegisterSupplierView, LoginSupplierView, MailView

urlpatterns = [
    path('suppliers/', RegisterSupplierView.as_view()),
    path('login/', LoginSupplierView.as_view()),
    path("send_emails/", MailView.as_view())

]
