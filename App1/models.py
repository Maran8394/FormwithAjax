from django.db import models
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password

class Personal_Details(models.Model):
    gender_choice = [('Male','Male'),('Female','Female'),('Other','Other'),]
    relationship_choice = [('married','Married'),('unmarried','Unmarried')]

    #Personal Details
    f_name = models.CharField(max_length=100,null=True,blank=False,verbose_name="First name")
    l_name = models.CharField(max_length=100,null=True,blank=False,verbose_name="Last name")
    dob = models.DateField(verbose_name="Date Of Birth",)
    gender = models.CharField(max_length=50,choices=gender_choice,verbose_name="Gender",null=True,default=None,blank=False)
    relationship_status = models.CharField(max_length=50,choices=relationship_choice,verbose_name="RelationShip status",null=True,default=None,blank=False)
    language_known = models.CharField(verbose_name="Language Known",null=True,blank=False,max_length=100)
    hobbies = models.CharField(verbose_name="Hobbies",null=True,blank=False,max_length=100)
    profile_pic = models.ImageField(verbose_name="Profile picture",upload_to='profile_pic',null=True)

    #Contact Details
    email = models.EmailField(verbose_name="Email",null=True,blank=False)
    mobile = CharField(null=True,default="+91",verbose_name="Mobile Number",max_length=50)
    telePhone = models.IntegerField(verbose_name="TelePhone",default=None,blank=True,null=True)
    door_num = models.CharField(verbose_name="Door Number",null=True,blank=False,max_length=10)
    street =  models.CharField(verbose_name="Street",null=True,blank=False,max_length=100)
    town_city = models.CharField(verbose_name="Town/City",max_length=200,null=True,blank=False)
    district = models.CharField(verbose_name="District",max_length=200,null=True,blank=False)
    state    = models.CharField(verbose_name="State",null=True,blank=False,max_length=100)
    country = models.CharField(verbose_name="Country",null=True,blank=False,max_length=100)
    zip_code = models.IntegerField(verbose_name="Zip code",null=True,blank=False)

    #Educational Details
    course_name = models.CharField(verbose_name="Course Name",max_length=200,null=True,blank=False)
    institute_name = models.CharField(verbose_name="Institute Name",max_length=200,null=True,blank=False)
    institute_address = models.TextField(verbose_name="Institute address",max_length=200,null=True,blank=False)
    started_year = models.IntegerField(verbose_name="Started year",null=True,blank=False)
    passed_year = models.IntegerField(verbose_name="Passed year",null=True,blank=False)
    percentage_gpa = models.DecimalField(verbose_name="Percentage/GPA",null=True,blank=False,max_digits=5,decimal_places=3)
    upload_resume   = models.FileField(verbose_name="Upload resume",upload_to='uploaded_resume',null=True,blank=False)
    password = models.CharField(verbose_name="Password",max_length=200,null=True,blank=False)
    confirm_password = models.CharField(verbose_name="Confirm Password",max_length=200,null=True,blank=False)
    terms_conditions = models.BooleanField(null=True,blank=False,verbose_name="Terms & Conditions")

    def save(self,*args,**kwargs):
        self.password = make_password(self.password)
        self.confirm_password = self.password
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.f_name

