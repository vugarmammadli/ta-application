from django.shortcuts import render

from rest_framework import generics
from .serializers import TeachingAssistantSerializer, CourseSerializer
from .models import TeachingAssistant, Course

class TACreateView(generics.ListCreateAPIView):
    '''Handles the GET and POST requests of the rest api for TAs.
    '''
    serializer_class = TeachingAssistantSerializer
    
    def get_queryset(self):
        '''Return a list of all the applicants. Optionally filters applicants
        according to status or family name.
        '''
        
        queryset = TeachingAssistant.objects.all()
        
        # /applicants?status=status
        status = self.request.query_params.get('status')
        
        # /applicants?fname=fname
        fname = self.request.query_params.get('fname')
        
        # iexact used for filtering case insensitive
        if status is not None:
            queryset = queryset.filter(status__iexact=status)
            
        if fname is not None:
            queryset = queryset.filter(family_name__iexact=fname)
        
        return queryset
    
    def perform_create(self, serializer):
        '''Save the post data when creating a new TA.
        '''
        serializer.save()

class TADetailsView(generics.RetrieveDestroyAPIView):
    '''Handles the GET and DELETE requests of the rest api for individual TA.
    '''
    serializer_class = TeachingAssistantSerializer
    queryset = TeachingAssistant.objects.all()

class CourseCreateView(generics.ListCreateAPIView):
    '''Handles the GET and POST requests of the rest api for courses.
    '''
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        '''Return a list of all the courses. Optionally filters courses
        according to the course code.
        '''
        
        queryset = Course.objects.all()
        
        # /courses?course=code
        code = self.request.query_params.get('course')
        
        # iexact used for filtering case insensitive
        if code is not None:
            queryset = queryset.filter(code__iexact=code)
        
        return queryset
    
    def perform_create(self, serializer):
        '''Save the post data when creating a new TA.
        '''
        serializer.save()    