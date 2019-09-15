from django.urls import path
from . import views

app_name = 'banhang'

urlpatterns = [
        path("", views.trangchu, name="trangchu"),
        ]
