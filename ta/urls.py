from django.urls import path
from . import views

app_name = 'ta'
urlpatterns = [
    # /applicants/
    path('applicants/', views.TACreateView.as_view(), name='create'),
]
