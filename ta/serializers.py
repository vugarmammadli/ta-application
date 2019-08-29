from rest_framework import serializers
from .models import TeachingAssistant, Course, Application

class TeachingAssistantSerializer(serializers.ModelSerializer):
    '''Serializer to map the TA model instance to JSON format.
    '''
    
    class Meta:
        '''Meta class to map serializer fields with the model fields.
        '''
        model = TeachingAssistant
        fields = ('student_number', 'given_name', 'family_name', 'status', 'year')

class CourseSerializer(serializers.ModelSerializer):
    '''Serializer to map the Course model instance to JSON format.
    '''
    
    class Meta:
        '''Meta class to map serializer fields with the model fields.
        '''
        model = Course
        fields = ('code', 'name', 'description')