from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from datetime import datetime
from rest_framework.generics import (
	DestroyAPIView, RetrieveUpdateAPIView
	)

from .models import Flight, Booking
from .serializers import (
	FlightSerializer, BookingSerializer, 
	DetailSerializer, UpdateSerializer
	)


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


class DetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class UpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class DeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'