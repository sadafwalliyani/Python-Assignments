from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='add/record'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.delete, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

]