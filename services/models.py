from django.db import models


class Customer(models.Model):

    c_email = models.EmailField(primary_key=True)

    c_name = models.CharField(max_length=100)

    c_mob_no = models.CharField(max_length=10)

    c_password = models.CharField(max_length=100)

    class Meta:
        db_table = 'customer'


class Booking(models.Model):
    
    class Meta:
        db_table = 'bookings'

    STATUS_CHOICES = [

        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),

    ]

    booking_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phno = models.CharField(max_length=15)

    address = models.TextField()

    pin_code = models.CharField(max_length=10)

    pref_date = models.DateField()

    requirements = models.TextField()

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    cost = models.FloatField(default=0)

    booking_date = models.DateField()