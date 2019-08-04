from rest_framework import serializers
from .models import TeachingAssistant, Course, Application

class TeachingAssistantSerializer(serializers.ModelSerializer):
    '''Serializer to map the Model instance to JSON format.
    '''
    
    class Meta:
        '''Meta class to map serializer's fields with the model fields.
        '''
        model = TeachingAssistant
        fields = ('student_number', 'given_name', 'family_name', 'status', 'year')