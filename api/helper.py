from django.http.response import HttpResponse
from rest_framework.exceptions import APIException
from .models import UserLogs
from django.contrib.auth.models import *
from .serializers import UserLogSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.mail import EmailMessage

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
    page_size = 2
    page_size_query_param = page_size
    max_page_size = 2 


class SendEmail():
    def sampleEmail():
        email = EmailMessage('User Regisatration', 'Hello Guys', to=['gwedezac@gmail.com'])
        email.send()
