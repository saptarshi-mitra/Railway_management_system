from django.urls import path
from . import views


app_name = 'train'

urlpatterns = [
    path('home/', views.home_page, name='home'),

]
