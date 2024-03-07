from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from pooler.models import Ride, WayPoint
from accounts.models import Pooler, UserExtra
from .models import Booking
from django.http import JsonResponse
from .forms import UserComplaintForm
from django.contrib import messages
from administrator.models import UserComplaint



# Create your views here.
@login_required(login_url='accounts_signin')
def index(request):
    today = datetime.now()
    context = {}
    context['places'] = WayPoint.objects.filter(ride__is_completed=False, ride__status=True).values('point').order_by()
    context['is_search'] = False
    if request.method == "GET":
        f = request.GET.get('from', None)
        t = request.GET.get('to', None)
        d = request.GET.get('departure_time', None)
        if f is not None and t is not None:
            if d == '':
                data = WayPoint.objects.filter(point=f).values('ride').order_by()
            else:
                date = datetime.fromisoformat(d)
                data = WayPoint.objects.filter(point=f, ride__departure_time__year=date.year, ride__departure_time__month=date.month, ride__departure_time__day=date.day).values('ride').order_by()
            # else:
            #     context['data'] = WayPoint.objects.filter(point=f, km=0.0, ride__departure_time=d)
            rides = []
            for d in data:
                r = WayPoint.objects.filter(ride_id=d['ride'], point=t, km__gt=0.0)
                if len(r)>0:
                    r = Ride.objects.filter(id=d['ride'],departure_time__gte=today)
                    if len(r) > 0:
                        rides.append(r[0])
            context['from'] = f
            context['to'] = t
            context['d'] = d
            context['rides'] = rides
            context['is_search'] = len(rides) == 0
    return render(request, 'user/index.html', context)

@login_required(login_url='accounts_signin')
def view_route(request, id):
    context = {}
    context['routes'] = WayPoint.objects.filter(ride_id=id)
    return render(request, 'user/routes.html', context)

@login_required(login_url='accounts_signin')
def driver_details(request, id):
    context = {}
    context['driver'] = Pooler.objects.get(user_id=id)
    return render(request, 'user/driver.html', context)

@login_required(login_url='accounts_signin')
def book_now(request, id, frm, to):
    ride = Ride.objects.get(pk=id)
    if request.method == 'GET':
        bookings = Booking.objects.filter(ride=ride)
        seats_list = []
        for booking in bookings:
            seat = booking.seat
            seat = seat.split(',')
            seat = seat[:-1]
            seats_list.extend(seat)
        point = WayPoint.objects.filter(ride=ride, point=frm) | WayPoint.objects.filter(ride=ride, point=to)
        s = point[0].km
        d = point[1].km
        total_distance = d-s
        amt = total_distance * float(ride.price)
        cgst=amt*((18/2)/100)
        sgst=cgst
        total_amt=amt+cgst+sgst
        context = {}
        context['from'] = frm
        context['to'] = to
        context['total_distance'] = total_distance
        context['price'] = ride.price
        context['amt'] = amt
        context['cgst'] = cgst
        context['sgst'] = sgst
        context['total'] = total_amt
        context['seats'] = seats_list
        return render(request, 'user/car.html', context)
    elif request.method == 'POST':
        seats = request.POST['seats']
        total = request.POST['total']
        tk = float(request.POST['total_kilometer'])
        obj = Booking(
            ride=ride, 
            user=UserExtra.objects.get(user=request.user), 
            source=frm,
            destination=to,
            total_km=tk,
            seat=seats,
            amount=total
        )
        obj.save()
        return JsonResponse({'success': 1})

@login_required(login_url='accounts_signin')
def upcoming_journey(request):
    if request.method == 'GET':
        today = datetime.now()
        bookings = Booking.objects.filter(user__user=request.user, ride__departure_time__gte=today)
        context = {}
        context['bookings'] = bookings
        return render(request, 'user/upcoming.html', context)


@login_required(login_url='accounts_signin')
def ride_info(request, id):
    ride = Ride.objects.get(id=id)
    way = WayPoint.objects.filter(ride=ride)
    context = {}
    context['ride'] = ride
    context['from'] = way[0].point
    context['to'] = way[len(way)-1].point
    context['next'] = request.GET.get('next')
    return render(request, 'user/ride_info.html', context)

@login_required(login_url='accounts_signin')
def history(request):
    if request.method == 'GET':
        today = datetime.now()
        bookings = Booking.objects.filter(user__user=request.user, ride__departure_time__lt=today)
        context = {}
        context['bookings'] = bookings
        return render(request, 'user/history.html', context)

@login_required(login_url='accounts_signin')
def user_complaints(request):
    if request.method == 'POST':
        form = UserComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, f'Complaint successfully registred on {obj.complaint_date}')
            return redirect('user_index')
    else:
        form = UserComplaintForm()
    return render(request, 'user/complaints.html', {'form': form})
    

@login_required(login_url='accounts_signin')
def user_complaints_history(request):
    complaints = UserComplaint.objects.filter(user=request.user)
    return render(request, 'user/complaint_history.html', {'complaints': complaints})