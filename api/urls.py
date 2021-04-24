from django import urls
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api import views

router  = DefaultRouter()

router.register('users', views.UserViewSet, basename = 'Users')
router.register('groups', views.GroupViewSet, basename = 'Groups')
router.register('permissions', views.PermissionViewSet, basename = 'Permissions')
router.register('user_logs', views.UserLogsViewSet, basename = 'User Logs')

urlpatterns = [
    path('', include(router.urls)),
]