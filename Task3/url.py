from django.urls import path
from . import views

urlpatterns = [
    path("",views.dynamic_fields,name="dynamic"),

    path('image/',views.image_validation, name='image_validation'),
    path('success/',views.success,name='success'),
]