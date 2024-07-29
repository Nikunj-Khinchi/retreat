from django.urls import path
from .views import RetreatListView, BookingListView,RetreatDetailView, BookingDetailView

urlpatterns = [
    path('retreats/', RetreatListView.as_view(), name='retreat-list'),
    path('retreats/<int:pk>/', RetreatDetailView.as_view(), name='retreat-detail'),  # Added URL pattern for single retreat
    path('book/', BookingListView.as_view(), name='booking-create'),
    path('book/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
