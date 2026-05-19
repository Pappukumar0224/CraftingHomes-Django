from django.shortcuts import render, redirect
from .models import Customer, Booking
from datetime import date


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# OTHER PAGES
def services_page(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def paint(request):
    return render(request, 'paint.html')


def house_cleaning(request):
    return render(request, 'house_cleaning.html')


def electrical(request):
    return render(request, 'electrical.html')


def flooring(request):
    return render(request, 'flooring.html')


def carpenter(request):
    return render(request, 'carpenter.html')


def plumber(request):
    return render(request, 'plumber.html')


# LOGIN + SIGNUP
def login_view(request):

    # SIGNUP
    if request.method == "POST" and 'mobileNo' in request.POST:

        name = request.POST.get('name')
        mobile = request.POST.get('mobileNo')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # CHECK EXISTING EMAIL
        if Customer.objects.filter(c_email=email).exists():

            return render(request, 'login.html', {
                'error': 'Email already exists'
            })

        # SAVE USER
        Customer.objects.create(
            c_name=name,
            c_email=email,
            c_mob_no=mobile,
            c_password=password
        )

        # CREATE SESSION
        request.session['user_email'] = email

        return redirect('home')

    # LOGIN
    elif request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user = Customer.objects.get(
                c_email=email,
                c_password=password
            )

            request.session['user_email'] = user.c_email

            return redirect('home')

        except Customer.DoesNotExist:

            return render(request, 'login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'login.html')


# BOOKING PAGE
def booking(request):

    if 'user_email' not in request.session:

        return redirect('login')

    service = request.GET.get('service')

    requirements = []

    # Painting
    if service == "paint":

        requirements = [

            "Interior Painting",
            "Exterior Painting",
            "One Wall Painting",
            "Waterproofing"

        ]

    # Electrical
    elif service == "electrical":

        requirements = [

            "Fan Repair",
            "Switch Board Repair",
            "Wiring",
            "Light Installation"

        ]

    # Plumber
    elif service == "plumber":

        requirements = [

            "Tap Repair",
            "Pipe Leakage",
            "Bathroom Fitting",
            "Water Tank Cleaning"

        ]

    # Carpenter
    elif service == "carpenter":

        requirements = [

            "Furniture Repair",
            "Door Repair",
            "Window Work",
            "Wood Polishing"

        ]

    # Flooring
    elif service == "flooring":

        requirements = [

            "Tile Installation",
            "Marble Flooring",
            "Wooden Flooring",
            "Floor Repair"

        ]

    # House Cleaning
    elif service == "house_cleaning":

        requirements = [

            "Kitchen Cleaning",
            "Bathroom Cleaning",
            "Sofa Cleaning",
            "Full House Cleaning"

        ]

    if request.method == "POST":

        Booking.objects.create(

            name=request.POST.get('name'),

            email=request.session['user_email'],

            phno=request.POST.get('phone'),

            address=request.POST.get('address'),

            pin_code=request.POST.get('pincode'),

            pref_date=request.POST.get('date'),

            requirements=", ".join(
                request.POST.getlist('requirements')
            ),

            description=request.POST.get('description'),

            status="Pending",

            cost=0,

            booking_date=date.today()

        )

        return redirect('profile')

    return render(request, 'booking.html', {

        'requirements': requirements,
        'service': service

    })
    
    
# PROFILE PAGE
def profile(request):

    if 'user_email' not in request.session:
        return redirect('login')

    email = request.session['user_email']

    user = Customer.objects.get(c_email=email)

    bookings = Booking.objects.filter(email=email)

    return render(request, 'profile.html', {

        'user': user,

        'bookings': bookings

    })


# LOGOUT
def logout_view(request):

    request.session.flush()

    return redirect('login')


# CONTACT PAGE
def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        print(name)
        print(email)
        print(message)

        return render(request, 'contact.html', {

            'success': 'Message sent successfully!'

        })

    return render(request, 'contact.html')



from django.shortcuts import get_object_or_404


def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        booking_id=booking_id
    )

    booking.delete()

    return redirect('profile')