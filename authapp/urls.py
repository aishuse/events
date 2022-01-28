from django.urls import path
from . import views


urlpatterns = [

    path('home', views.Home.as_view(), name='home'),
    path('customer/add', views.AddCustomer.as_view(), name='customeradd'),
    path('customer/list', views.ListCutomers.as_view(), name='listcustomers'),

]