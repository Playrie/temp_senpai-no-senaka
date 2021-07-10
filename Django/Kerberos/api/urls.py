from django.urls import path
from . import views

urlpatterns = [
    path('register_rest_request/', views.register_rest_requests),
#    path('option/', views.OptionAPIView.as_view()),
#    path('cast/', views.CastAPIView.as_view()),
#    path('callback/',views.callback),
#    path('temporaryBooking/',views.temporary_booking),
#    path('getBookableInfo',views.bookableInfo),
#    path('getBookingSummary',views.bookingSummary),
#    path('postbookWithCash',views.bookWithCashFromLiff),
#    path('postbookWithCreditComplete',views.bookCompleteWithCreditFromLiff),
#    path('postbookWithCreditPaymentFailed',views.bookWithCreditPaymentFailedFromLiff)
#
]