from django.urls import path
from .views import RegisterDashboardView, DashboardByIdView, LastVisitedDashboardView, DashboardEditFavoriteView, DashboardByCategoryView

urlpatterns = [
    path('dashboards/', RegisterDashboardView.as_view()),
    path('dashboards/id/<dashboard_id>/', DashboardByIdView.as_view()),
    path('dashboards/favorite/<dashboard_id>/', DashboardEditFavoriteView.as_view()),
    path('dashboards/last/<dashboard_id>/', LastVisitedDashboardView.as_view()),
    path('dashboards/category/<dashboard_category>/', DashboardByCategoryView.as_view()),
]