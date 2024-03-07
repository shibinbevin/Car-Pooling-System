from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='pooler_index'),
    path('ride/', make_trip, name='pooler_make_trip'),
    path('ride/delete/<int:id>', delete_ride,name='pooler_delete_ride'),
    path('ride/status/<int:id>', ride_status,name='pooler_ride_status'),
    path('ride/complete/<int:id>', ride_mark_as_complete,name='pooler_ride_mark_as_complete'),
    path('ride/route/<int:id>', view_route, name='pooler_view_route'),
    path('ride/history/', history, name='pooler_ride_history'),
    path('car/add/', add_car, name='pooler_add_car'),
    path('car/manage/', manage_car, name='pooler_manage_car'),
    path('car/visibility/<int:id>', change_visibility, name='pooler_change_visibility'),
    path('car/edit/<int:id>', edit_car, name='pooler_edit_car'),
    path('car/remove/<int:id>', remove_car, name='pooler_remove_car'),
    path('booking/', user_booking, name='user_user_booking'),
    path('ride/info/<int:id>', ride_details, name='pooler_ride_details'),
    path('user/info/<int:id>', user_details, name='pooler_user_details'),

]