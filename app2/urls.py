from django.urls import path
from app2.views import *
app_name='sdfghj'

urlpatterns=[
    path('user3/',user3,name='user3'),
    path('user4/',user4,name='user4')
]