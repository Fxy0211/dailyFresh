from django.urls import path

from user.views import *

app_name = 'user'

urlpatterns = [
    
    path('user/',fanxiangyang,name = 'fxy')
]