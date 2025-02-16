from django.urls import path
from .views import SpamReportListCreateView

urlpatterns = [
    path('', SpamReportListCreateView.as_view(), name='spam-report-list'),
]