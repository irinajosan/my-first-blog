from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('irina', views.hello_irina, name='hello_irina'),
    path('adrian', views.hello_adrian, name='hello_adrian'),
]
