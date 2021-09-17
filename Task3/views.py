
from typing import Counter
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Image_Validation
from PIL import Image
from .models import Dynamic_fields
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
        d = Dynamic_fields()
        d_user,d_interest, both= {},{},{}
        
        for i in range(len(name)):
           d_user[i]=name[i]  
           d_interest[i]=interest[i]
           both[d_user[i]]=d_interest[i]
        d.user = d_user
        d.interest = d_interest
        d.n_i = both
        d.save()
        return HttpResponse("Finish")
    else:
        return render(request,'dynamic_field.html')

