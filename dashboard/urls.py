from rest_framework.routers import DefaultRouter
from django.urls import path

from dashboard.views import DashboardViewSet, AllDataSummary, LineChartData, PieChartData, YearSummary

router = DefaultRouter()
router.register(r"dashboard", DashboardViewSet, basename="dashboard")

urlpatterns = [
    path("data/", AllDataSummary.as_view(), name="all_summary"),
    path("pie/", PieChartData.as_view(), name="pie_chart"),
    path("line/", LineChartData.as_view(), name="line_chart"),
    path("year-summary/", YearSummary.as_view(), name="year summary"),
]

urlpatterns += router.urls

