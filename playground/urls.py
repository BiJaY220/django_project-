from django.urls import path 
from . import views 
#url_conf

urlpatterns = [
    path( 'hello/' , views.say_hello)
]
