from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('docs', views.docs, name='docs'),
    path('structure', views.structure, name='structure'),
    path('aup', views.aup, name='aup'),
]
