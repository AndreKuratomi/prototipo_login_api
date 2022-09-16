from django.urls import path
from .views import RegisterSupplierView, SupplierByCNPJView, LoginSupplierView, AskChangePasswordMailView, ChangePasswordMailView

urlpatterns = [
    path('suppliers/', RegisterSupplierView.as_view()),
    path('suppliers/<supplier_cnpj>/', SupplierByCNPJView.as_view()),
    path('login/', LoginSupplierView.as_view()),
    path('ask/', AskChangePasswordMailView.as_view()),
    path('change/', ChangePasswordMailView.as_view())
]
