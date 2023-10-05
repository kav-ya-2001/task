from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('tour',views.tour,name='tour'),
    path('information',views.information,name='information')
]
