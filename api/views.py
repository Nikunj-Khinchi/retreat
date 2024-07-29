from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Retreat, Booking
from .serializers import RetreatSerializer, BookingSerializer
from  .filters import RetreatFilter
from .pagination import RetreatPagination

class RetreatListView(generics.ListCreateAPIView):
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'location', 'type', 'condition' ,'date']
    filterset_class = RetreatFilter
    pagination_class = RetreatPagination

class RetreatDetailView(generics.RetrieveAPIView):  # Added view to retrieve a single retreat
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by('booking_date')
    serializer_class = BookingSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['retreat__title', 'retreat__location']
    # filterset_fields = ['retreat']
    pagination_class = PageNumberPagination

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer