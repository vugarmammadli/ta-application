from django.shortcuts import render

from rest_framework import generics
from .serializers import TeachingAssistantSerializer
from .models import TeachingAssistant

# Create your views here.

class TACreateView(generics.ListCreateAPIView):
    '''Handles the GET and POST requests of the rest api for TAs.
    '''
    queryset = TeachingAssistant.objects.all()
    serializer_class = TeachingAssistantSerializer
    
    def perform_create(self, serializer):
        '''Save the post data when creating a new TA.
        '''
        serializer.save()
