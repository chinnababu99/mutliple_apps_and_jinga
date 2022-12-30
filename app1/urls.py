from django.urls import path 
from app1.views import *
app_name="wertyu"

urlpatterns=[
    path('user1/',user1,name='user1'),
    path('user2/',user2,name='user2')
]