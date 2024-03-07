from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from accounts.models import Pooler, UserExtra
from .models import Ride, WayPoint
from user.models import Booking

# Create your views here.

def check_car(func):
    def inner(*args, **kwargs):
        car = Car.objects.filter(owner__user=args[0].user)
        if len(car) == 0: return redirect('pooler_add_car')
        return func(*args, **kwargs)
    
    return inner

@login_required(login_url='accounts_signin')
@check_car
def index(request):
    if request.method == 'GET':
        context = {}
        context['datas'] = Ride.objects.filter(car__owner__user=request.user, is_completed=False)
        return render(request, 'pooler/index.html', context)

@login_required(login_url='accounts_signin')
@check_car
def make_trip(request):
    if request.method == 'GET':
        return render(request, 'pooler/create_ride.html')
    elif request.method == 'POST':
        ride = Ride()
        ride.origin = request.POST['from']
        ride.destination = request.POST['to']
        ride.departure_time = request.POST['d_time']
        ride.estimated_reaching_time = request.POST['e_time']
        ride.gender_preference = request.POST['preference']
        ride.description = request.POST['desc']
        ride.price = request.POST['amount']
        ride.car = Car.objects.get(owner__user=request.user)
        ride.save()
        points = request.POST['points']
        points = points.strip()
        points = points.split(',')
        kilometers = request.POST['kilometers']
        kilometers = kilometers.strip()
        kilometers = kilometers.split(',')
        datas = zip(points, kilometers)
        for data in datas:
            obj = WayPoint(point=data[0], km=data[1], ride=ride)
            obj.save()
        return JsonResponse({'success': 1})

@login_required(login_url='accounts_signin')
@check_car
def delete_ride(request, id):
    Ride.objects.get(pk=id).delete()
    return redirect('pooler_index')

@login_required(login_url='accounts_signin')
@check_car
def ride_status(request, id):
    ride = Ride.objects.get(pk=id)
    ride.status = True
    ride.save()
    return redirect('pooler_index')

@login_required(login_url='accounts_signin')
@check_car
def ride_mark_as_complete(request, id):
    ride = Ride.objects.get(pk=id)
    ride.is_completed = True
    ride.save()
    return redirect('pooler_index')

@login_required(login_url='accounts_signin')
@check_car
def view_route(request, id):
    context = {}
    context['routes'] = WayPoint.objects.filter(ride_id=id)
    context['next'] = request.GET.get('next')
    return render(request, 'pooler/routes.html', context)



@login_required(login_url='accounts_signin')
def add_car(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CarForm()
        return render(request, 'pooler/create_car.html', context=context)
    elif request.method == 'POST':
        car = CarForm(request.POST, request.FILES)
        if car.is_valid():
            obj = car.save(commit=False)
            obj.owner = Pooler.objects.get(user=request.user)
            obj.save()
            return redirect('pooler_index')
        else:
            context = {}
            context['form'] = car
            return render(request, 'pooler/create_car.html', context=context)

@login_required(login_url='accounts_signin')
@check_car
def manage_car(request):
    if request.method == 'GET':
        context = {}
        context['car'] = Car.objects.get(owner__user=request.user)
        return render(request, 'pooler/manage_car.html', context=context)

@login_required(login_url='accounts_signin')
@check_car
def edit_car(request, id):
    car = Car.objects.get(pk=id)
    if request.method == 'GET':
        context = {}
        context['form'] = CarEditForm(instance=car)
        return render(request, 'pooler/create_car.html', context=context)
    elif request.method == 'POST':
        obj = CarEditForm(data=request.POST, files=request.FILES, instance=car)
        if obj.is_valid():
            obj.save()
            return redirect('pooler_manage_car')
        else:
            context = {}
            context['form'] = car
            return render(request, 'pooler/create_car.html', context=context)

@login_required(login_url='accounts_signin')
@check_car
def remove_car(request, id):
    car = Car.objects.get(pk=id)
    car.delete()
    return redirect('pooler_add_car')


@login_required(login_url='accounts_signin')
@check_car
def change_visibility(request, id):
     if request.method == 'GET':
         car = Car.objects.get(pk=id)
         car.status = not car.status
         car.save()
         return redirect('pooler_manage_car')


@login_required(login_url='accounts_signin')
@check_car
def history(request):
    if request.method == 'GET':
        context = {}
        rides = Ride.objects.filter(car__owner__user=request.user, is_completed=True)
        context['datas'] = Booking.objects.filter(ride_id__in=rides)
        return render(request, 'pooler/history.html', context)

@login_required(login_url='accounts_signin')
@check_car
def user_booking(request):
    if request.method == 'GET':
        context = {}
        rides = Ride.objects.filter(car__owner__user=request.user, is_completed=False).values_list("id")
        context['datas'] = Booking.objects.filter(ride_id__in=rides)
        print(context['datas'])
        return render(request, 'pooler/booking.html', context)


@login_required(login_url='accounts_signin')
@check_car
def ride_details(request, id):
     if request.method == 'GET':
        context = {}
        context['ride'] = Ride.objects.get(pk=id)
        return render(request, 'pooler/ride.html', context)

@login_required(login_url='accounts_signin')
@check_car
def user_details(request, id):
     if request.method == 'GET':
        context = {}
        context['user'] = UserExtra.objects.get(pk=id)
        context['next'] = request.GET.get('next')
        return render(request, 'pooler/user.html', context)

