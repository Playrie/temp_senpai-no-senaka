from django.urls import path
from . import views

urlpatterns = [
    path('register_rest_request/', views.register_rest_requests),
    path('get_rest_schedules/', views.get_rest_schedules),

]