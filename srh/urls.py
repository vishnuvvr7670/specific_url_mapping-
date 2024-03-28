from django.urls import path
from srh.views import *
app_name='vvr'

urlpatterns=[
    path('pat/',pat,name='pat'),
    path('klassen/',klassen,name='klassen'),
]