from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', signin, name='accounts_signin'),
    path('signup/user/', signup, name='accounts_signup'),
    path('signup/pooler/', pooler_signup, name='accounts_pooler_signup'),
    path('logout/', logout_action, name='accounts_logout_action'),
    path('profile/', profile, name='accounts_profile'),
    path('change_password/', change_password, name='accounts_change_password'),
]