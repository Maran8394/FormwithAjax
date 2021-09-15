from sys import getsizeof
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Image_Validation
from PIL import Image

# Create your views here.


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
    
    return render(request,'success.html',{'datas':m})
