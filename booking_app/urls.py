from django.urls import path,include
from . import views

app_name = 'booking_app'

urlpatterns = [
    path('',views.index,name='index'),
     path('delete/<int:id>',views.delete,name='delete'),   
    path('add',views.add_,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
]