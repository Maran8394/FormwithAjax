from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Image_Validation
from PIL import Image
from .models import Dynamic_fields
from django.forms.models import model_to_dict
import json
def image_validation(request):
    try:
        if request.method == "POST":
            up_image = request.FILES.getlist('images')
            for i in up_image:
                get_img_size = Image.open(i)
                if get_img_size.height >= 200 and get_img_size.width >=200:
                    img = Image_Validation(img_field=i)
                    img.save()
                else:
                    return HttpResponse("Image doesn't meet minimum requirements.")
            return redirect('success')
        
        return render(request,'task3.html')
    except:
        return HttpResponse("Enter a valid Image")

def success(request):
    m = Image_Validation.objects.all()
    
    return render(request,'success1.html',{'datas':m})


def dynamic_fields(request):
    if request.method == "POST":
        name = request.POST.getlist('name')
        interest = request.POST.getlist("interest")
        d = Dynamic_fields(user=name,interest=interest)
        k = model_to_dict(d)
        print(type(k.keys()),k.keys(),sep="-----")
        print(type(k.keys()),k.values(),sep="-----")
        j = json.dumps(k)
        print(j)
        print(j)
        return redirect("success")
    else:
        return render(request,'dynamic_field.html')