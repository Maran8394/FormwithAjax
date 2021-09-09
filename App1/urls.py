from django.urls import path
from . import views

urlpatterns = [
    path('',views.save_form,name="personaldetails"),
    path("success/",views.success, name="success"),
]
