from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    # path('readkaro',views.read_file,name='readkaromerijaan'),
    # path('aage',views.aage,name='aage'),
    # path('piche',views.piche,name='piche'),
    path('analyze',views.analyze,name='analyze'),
]