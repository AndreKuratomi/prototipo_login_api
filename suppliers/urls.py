from django.urls import path
from .views import RegisterSupplierView, LoginSupplierView, AskChangePasswordMailView

urlpatterns = [
    path('suppliers/', RegisterSupplierView.as_view()),
    path('login/', LoginSupplierView.as_view()),
    path("ask_emails/", AskChangePasswordMailView.as_view())

]
