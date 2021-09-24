
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import json
from . models import Contact_Us
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
# Create your views here.


class UploadResume(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact_us.html')

    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            msg = request.POST['message']
            resume = request.FILES['resume']
            print(resume)
            c = Contact_Us.objects.create(
                user_name=name,
                email_id=email,
                mobile_num=mobile,
                msg=msg,
                resume_file=resume
            )
            msg_html = render_to_string('mailchimp/index.html')
            send_mail(
                'Thanks For Contact Us',
                "body",
                settings.EMAIL_HOST_USER,
                [c.email_id],
                html_message=msg_html,
            )
            print("sent mail to the user")

            admin_html = render_to_string('mailchimp/admin.html', {
                                          'name': c.user_name, "email": c.email_id, 'mobile': c.mobile_num, 'msg': c.msg})
            m = EmailMessage(
                subject="Contact US",
                body=admin_html,
                from_email=settings.EMAIL_HOST_USER,
                to=['maran8394@gmail.com'],
            )
            m.content_subtype = "html"
            m.attach_file(c.resume_file.path)
            m.send(fail_silently=False)
            print("sent mail to the admin")

            return HttpResponse("success")
        else:
            
            return HttpResponse("Failed")


