from django.urls import path , re_path , include
from tempTag import views

app_name = "tempTag"

urlpatterns = [ 
               re_path(r"^relative/" , views.relative , name="relative") , 
               re_path(r"^other/" , views.other , name="other"), 
               ]