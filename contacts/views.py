from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    Permission_Classes = [IsAuthenticated]
    Serializer_Class = ContactSerializer

    def Get_Query_Set(self):
        return Contact.objects.filter(added_by=self.request.user)

    def Perform_Create(self, serializer):
        serializer.save(added_by=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    Permission_Classes = [IsAuthenticated]
    Serializer_Class = ContactSerializer

    def Get_Query_Set(self):
        return Contact.objects.filter(added_by=self.request.user)