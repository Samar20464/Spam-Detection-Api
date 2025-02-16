from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SpamReport
from .serializers import SpamReportSerializer

class SpamReportListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SpamReportSerializer

    def get_queryset(self):
        return SpamReport.objects.all()

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)