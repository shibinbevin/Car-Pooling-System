from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='admin_index'),
    path('user/complaints/', user_complaints, name='admin_user_complaints'),
    path('user/complaint/resolve/<int:id>', mark_as_complete, name='admin_mark_as_complete'),
    path('user/complaint/remove/<int:id>', delete_complaints, name='admin_delete_complaints'),
    path('pooler/', manage_pooler, name='admin_manage_pooler'),
    path('user/status/<int:id>/<next>', change_active_status, name='admin_change_active_status'),
    path('user/remove/<int:id>/<next>', delete_user, name='admin_delete_user'),
    path('user/', manage_user, name='admin_manage_user'),
    path('manage_rides/', manage_rides, name='admin_manage_rides'),
    path('bookings/', user_booking, name='admin_user_booking'),
    path('ride_details/<int:id>', ride_details, name='admin_ride_details'),
    path('user_details/<int:id>', user_details, name='admin_user_details'),

]