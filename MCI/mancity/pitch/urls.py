from . import views
from django.urls import path

urlpatterns = [
    path('',views.main,name='pitch'),
    path("download_time/<str:time>/", views.download_time, name="download_time"),
    path("redirect_to_space/<str:filename>/", views.redirect_to_space, name="redirect_to_space"),]
