from django.urls import path
from .views import RegisterDashboardView, DashboardByIdView, DashboardByCategoryView

urlpatterns = [
    path('dashboards/', RegisterDashboardView.as_view()),
    path('dashboards/id/<dashboard_id>/', DashboardByIdView.as_view()),
    path('dashboards/category/<dashboard_category>/', DashboardByCategoryView.as_view()),
]