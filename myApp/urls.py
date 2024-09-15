from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('signup/',views.handleSignup,name='signup'),
    path('signin/',views.handleSignin,name='signin'),
    path('logOut/',views.logOut,name='logOut'),
    path('menu/',views.menu,name='menu'),
    path('order/',views.order,name='order'),
    path('food_donation/',views.food_donation,name='food_donation'),
    path('checkout/',views.checkout,name='checkout'),
    path('success/',views.success,name='success'),
    path('contact/',views.contact1,name='contact'),


]