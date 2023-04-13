from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('category-inflation', views.category_inflation, name='category_inflation')]
