from django.urls import path
from . import views

urlpatterns = [
    path('',views.image_validation, name='image_validation'),
    path('success/',views.success,name='success'),
]