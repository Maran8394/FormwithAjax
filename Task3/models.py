from django.db import models
from PIL import Image
from io import BytesIO
import sys
from django.db.models.fields import files
from django.utils.crypto import get_random_string
from django.core.files.uploadedfile import InMemoryUploadedFile

    

# Create your models here.
class Image_Validation(models.Model):
    img_field = models.ImageField(upload_to="img_validation/",null=True,blank=False)
    img_thumb = models.ImageField(upload_to="img_validation_thumb/",null=True,blank=True, default=None)
    

    def save(self,*args,**kwargs):
        
        try:
            print("enter ....")
            output = BytesIO() # for local storage
            output1 = BytesIO()

            # image Thumbnail
            img = Image.open(self.img_field)
            output_size = (200,200) # 300,169
            img.thumbnail(output_size)    
            img.save(output1,format='JPEG',quality=90)
           
            # image Resize    
            im = Image.open(self.img_field)
            im = im.resize((400,250)) # 400,250
            im.save(output, format='JPEG', quality=90)
            output.seek(0)
           
            unique_id = get_random_string(length=32)
            
            self.img_field = InMemoryUploadedFile(
                file=output,
                size=sys.getsizeof(output),
                field_name=files.ImageField,name="%s.jpg"%self.img_field.name.split(".")[0],
                content_type='image/jpeg',
                charset=None)
           
            self.img_thumb = InMemoryUploadedFile(
                file=output1,
                size=sys.getsizeof(output1),
                field_name=files.ImageField,
                name="%s.jpg"%unique_id,
                content_type='image/jpeg',
                charset=None)
            print(self.img_thumb)
            print(self.img_field)
            super(Image_Validation, self).save(*args,**kwargs)
            
        except:
            print("except block")
            super(Image_Validation, self).save(*args,**kwargs)
        
  


class Dynamic_fields(models.Model):
    user = models.JSONField(max_length=50,null=True,blank=False,default=dict)
    interest = models.JSONField(max_length=500,null=True,blank=False,default=dict)
    n_i = models.JSONField(max_length=500,null=True,blank=False,default=dict)
    
   