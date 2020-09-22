from django.urls import path
from .views import home, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', user_logout, name='logout'),
]