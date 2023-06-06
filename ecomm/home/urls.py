from django.urls import path
from home.views import index,delivery
urlpatterns = [
    path('',index,name='index'),
    path('delivery/',delivery,name='delivery'),
]