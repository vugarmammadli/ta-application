from django.db import models

# Create your models here.

class TeachingAssistant(models.Model):
    student_number = models.IntegerField(primary_key=True)
    given_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    status = models.CharField(max_length=5)
    year = models.IntegerField(default=1)
    
    def __str__(self):
        return "Given Name: {}\n Family Name: {}\n Student Number: {}\n \
        Status: {}\n Year: {}".format(self.given_name, self.family_name,
                                      self.student_number, self.status,
                                      self.year)

class Course(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return "{}: {}".format(self.code, self.name)

class Application(models.Model):
    applicant = models.ForeignKey(TeachingAssistant, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rank = models.IntegerField()
    experience = models.IntegerField()
    