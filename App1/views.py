from django.db import models
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Personal_Details
from .forms import Personal_details
import json
from django.core import serializers
# Create your views here.


def save_form(request):
    form = Personal_details()
    if request.method == 'POST' and request.is_ajax():
        form = Personal_details(request.POST, request.FILES)
        
        d = {}
        if form.is_valid():
            print(form.errors)
            form.save()
            d['success']=True
            print(d)
            return HttpResponse(json.dumps(d),content_type="application/json")
        else:
            print(d)
            print(form.errors)
            d['success']=False
            return HttpResponse(json.dumps(d),content_type="application/json")
    else:
        return render(request,'Task1form.html',{'form':form})
        






def success(request):
    return render(request,'base.html')