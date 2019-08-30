from rest_framework import serializers
from .models import TeachingAssistant, Course, Application

class CourseSerializer(serializers.ModelSerializer):
    '''Serializer to map the Course model instance to JSON format.
    '''
    
    class Meta:
        '''Meta class to map serializer fields with the model fields.
        '''
        model = Course
        fields = ('code', 'name', 'description')

class ApplicationSerializer(serializers.ModelSerializer):
    '''Serializer to map the Application model instance to JSON format.
    '''
    
    class Meta:
        '''Meta class to map serializer fields with the model fields.
        '''
        model = Application
        fields = ('applicant', 'course', 'rank', 'experience')

class ApplicationsListingField(serializers.RelatedField):
    '''Custom relational field hat describes exactly how the output
    representation should be generated from the model instance.
    '''
    def to_representation(self, value):
        return {'code': value.course.code,
                'rank': value.rank,
                'experience': value.experience}
        
class TeachingAssistantSerializer(serializers.ModelSerializer):
    '''Serializer to map the TA model instance to JSON format.
    '''
    
    class Meta:
        '''Meta class to map serializer fields with the model fields.
        '''
        model = TeachingAssistant
        fields = ('student_number', 'given_name', 'family_name',
                  'status', 'year', 'courses')
    
    courses = ApplicationsListingField(read_only=True, many=True)