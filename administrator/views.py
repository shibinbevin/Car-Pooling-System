from django.shortcuts import render, redirect
from .models import UserComplaint
from accounts.models import UserExtra, Pooler, User
from pooler.models import Ride
from datetime import datetime
from user.models import Booking


# Create your views here.

def index(request):
    context = {}
    context['user'] = {
        'all': UserExtra.objects.all().count(),
        'active': UserExtra.objects.filter(user__is_active=True).count(),
        'inactive': UserExtra.objects.filter(user__is_active=False).count()
    }
    context['pooler'] = {
        'all': Pooler.objects.all().count(),
        'active': Pooler.objects.filter(user__is_active=True).count(),
        'inactive': Pooler.objects.filter(user__is_active=False).count()
    }
    context['complaint'] = {
        'all': UserComplaint.objects.all().count(),
        'solved': UserComplaint.objects.filter(resolved=True).count(),
        'unsolved': UserComplaint.objects.filter(resolved=False).count()
    }
    context['ride'] = {
        'active': Ride.objects.filter(is_completed=False).count(), 
        'inactive': Ride.objects.filter(is_completed=True).count(),
        'all': Ride.objects.all().count()
    }

    return render(request, 'admin/index.html', context=context)


def user_complaints(request):
    if request.method == 'GET':
        context = {}
        context['datas'] = UserComplaint.objects.all().order_by('resolved')
        return render(request, 'admin/user_complaints.html', context)

def mark_as_complete(request, id):
    complaint = UserComplaint.objects.get(pk=id)
    complaint.resolved = True
    complaint.resolved_date = datetime.today()
    complaint.save()
    return redirect('admin_user_complaints')

def delete_complaints(request, id):
    complaint = UserComplaint.objects.get(pk=id)
    complaint.delete()
    return redirect('admin_user_complaints')

def manage_pooler(request):
    if request.method == 'GET':
        context = {}
        context['poolers'] = Pooler.objects.all()
        return render(request, 'admin/manage_pooler.html', context)

def change_active_status(request, id, next):
    user = User.objects.get(pk=id)
    user.is_active = not user.is_active
    user.save()
    if next == 'user':
        return redirect('admin_manage_user')
    return redirect('admin_manage_pooler')

def delete_user(request, id, next):
    user = User.objects.get(pk=id)
    user.delete()
    if next == 'user':
        return redirect('admin_manage_user')
    return redirect('admin_manage_pooler')

def manage_user(request):
    if request.method == 'GET':
        context = {}
        context['users'] = UserExtra.objects.all()
        return render(request, 'admin/manage_user.html', context)

def manage_rides(request):
    if request.method == 'GET':
        context = {}
        context['datas'] = Ride.objects.all()
        return render(request, 'admin/rides.html', context)

def user_booking(request):
    if request.method == 'GET':
        context = {}
        context['datas'] = Booking.objects.all()
        return render(request, 'admin/booking.html', context)

def ride_details(request, id):
     if request.method == 'GET':
        context = {}
        context['ride'] = Ride.objects.get(pk=id)
        return render(request, 'admin/ride.html', context)

def user_details(request, id):
     if request.method == 'GET':
        context = {}
        context['user'] = UserExtra.objects.get(pk=id)
        return render(request, 'admin/user.html', context)
