from django.urls import path
from app import views

urlpatterns = [
    path('', views.reg),
    path('login/',views.log),
    path('done/',views.done),
]
