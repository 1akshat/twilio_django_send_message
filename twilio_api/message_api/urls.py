from django.conf.urls import url
import django_twilio
from . import views

urlpatterns = [
	 url(r'^api/$', views.home),
	 url(r'^send/', views.sms),
]
