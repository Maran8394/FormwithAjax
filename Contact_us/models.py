from django.core.mail import message
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Contact_Us(models.Model):
    user_name = models.CharField(max_length=50,null=True)
    email_id = models.EmailField(max_length=150,null=True)
    mobile_num = models.IntegerField(null=True,validators=[MaxValueValidator(10),MinValueValidator(10)])
    msg = models.TextField(null=True, max_length=200)
    resume_file = models.FileField(upload_to="Task8/Resumes/",null=True)

    def __str__(self) -> str:
        return self.user_name

    def save(self,*args,**kwargs):
        super(Contact_Us,self).save(*args,**kwargs)
