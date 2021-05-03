from django import template
from django.conf import settings
from django.http.response import HttpResponse
from rest_framework.exceptions import APIException
from .models import UserLogs
from django.contrib.auth.models import *
from rest_framework.pagination import PageNumberPagination
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template


class UserLogHelper():
    def createLog(log, tag, user_id):
        user = User.objects.get(pk = user_id)
        user_log = UserLogs()
        user_log.fk_userid = user
        user_log.log = log 
        user_log.tag = tag
        user_log.save()
        return  


class ResponsePaginationHelper(PageNumberPagination):
    page_query_param = 'page'
    page_size = 100
    page_size_query_param = page_size
    max_page_size = 100 


class SendEmail():
    def sampleEmail(email):
        email = EmailMessage('Subject', 'Hello Guys', to=[email])
        email.send()

    def UserRegistration(username, email):
        with open(settings.BASE_DIR / "api/templates/user_registration_email.txt") as txt_message:
            user_registration_message = txt_message.read()+" Username: "+username+" Email: "+email
        email_message = EmailMultiAlternatives('User Account Confirmation', user_registration_message, 'no-reply@example.com', to=[email])
        html_templete = get_template("user_registration_email.html").render({'username':username, 'email':email})
        email_message.attach_alternative(html_templete, "text/html")
        email_message.send()