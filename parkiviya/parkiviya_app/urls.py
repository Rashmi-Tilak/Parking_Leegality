from django.urls import path
from .views import AssignParkingSpotView, RetrieveParkingSpotView

urlpatterns = [
    path('assign-parking/', AssignParkingSpotView.as_view(), name='assign-parking'),
    path('retrieve-parking/<str:vehicle_number>/', RetrieveParkingSpotView.as_view(), name='retrieve-parking'),
]