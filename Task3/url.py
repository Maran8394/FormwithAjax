from django.urls import path
from . import views

urlpatterns = [
    path("",views.dynamic_fields,name="dynamic"),

    path('image/',views.image_validation, name='image_validation'),
    path('image/success/',views.success,name='Task3.suc'),
]