from django.contrib import admin
from .models import Customer, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('c_name', 'c_email', 'c_mob_no')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'booking_id',
        'name',
        'email',
        'requirements',
        'status',
        'cost'
    )

    list_filter = ('status',)

    search_fields = ('name', 'email')