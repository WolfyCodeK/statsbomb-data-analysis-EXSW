from . import views
from django.urls import path

urlpatterns = [
    path('',views.main,name='pitch'),
    path("download_time/<str:time>/", views.download_time, name="download_time"),]
