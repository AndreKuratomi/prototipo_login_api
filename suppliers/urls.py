from django.urls import path
from .views import RegisterSupplierView, LoginSupplierView

urlpatterns = [
    path('suppliers/', RegisterSupplierView.as_view()),
    path('login/', LoginSupplierView.as_view())
]
