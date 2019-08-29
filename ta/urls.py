from django.urls import path
from . import views

app_name = 'ta'
urlpatterns = [
    # /applicants/
    path('applicants/', views.TACreateView.as_view(), name='ta_create'),
    path('applicant/<int:pk>/', views.TADetailsView.as_view(), name='ta_details'),
    # /courses/
    path('courses/', views.CourseCreateView.as_view(), name='course_create'),
]
