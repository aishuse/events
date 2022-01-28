from django.urls import path
from . import views

urlpatterns = [
    path('home', views.CustomerHome.as_view(), name='custhome'),
    path('event/list', views.EventList.as_view(), name='eventlist'),
    path('myevent/list', views.MyEventList.as_view(), name='myeventlist'),

    # path('event/checkout', views.Checkout.as_views(), name='checkout'),
    path('event/add', views.EventAdd.as_view(), name='eventadd'),
    path('event/update/<int:pk>', views.UpdateEvent.as_view(), name='updateevent'),
    path('event/delete/<int:pk>', views.DeleteEvent.as_view(), name='deleteevent'),

    path("order/proceed", views.GatewayView.as_view(), name="payment-gateway"),
    path("order/payment", views.charge, name="payment"),



]