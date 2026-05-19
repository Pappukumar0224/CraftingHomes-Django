from django.contrib import admin
from django.urls import path
from services import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('services/', views.services_page, name='services'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile, name='profile'),

    path('booking/', views.booking, name='booking'),

    path('paint/', views.paint, name='paint'),

    path('house_cleaning/', views.house_cleaning, name='house_cleaning'),

    path('electrical/', views.electrical, name='electrical'),

    path('flooring/', views.flooring, name='flooring'),

    path('carpenter/', views.carpenter, name='carpenter'),

    path('plumber/', views.plumber, name='plumber'),
    
    path(
    'cancel-booking/<int:booking_id>/',
    views.cancel_booking,
    name='cancel_booking'
    ),

]