from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bubbleapp-home'),

    path('', views.bubblehtml, name='bubbleapp-bubblehtml')
]
