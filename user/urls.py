from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='user_index'),
    path('route/<int:id>', view_route, name='user_view_route'),
    path('driver/<int:id>', driver_details, name='user_driver_details'),
    path('booking/<int:id>/<frm>/<to>', book_now, name='user_book_now'),
    path('booking/upcoming/', upcoming_journey, name='user_upcoming_journey'),
    path('booking/rideinfo/<int:id>', ride_info, name='user_ride_info'),
    path('booking/history/', history, name='user_history'),
    path('complaints/', user_complaints, name='user_user_complaints'),
    path('complaints/history/', user_complaints_history, name='user_user_complaints_history'),

]