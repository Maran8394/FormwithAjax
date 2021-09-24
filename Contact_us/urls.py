from django.urls import path
from . import views
urlpatterns = [
    path("", views.UploadResume.as_view(),name="resumeform"),
    
]