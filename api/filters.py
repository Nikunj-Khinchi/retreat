import django_filters
from .models import Retreat
import logging

logger = logging.getLogger(__name__)


class RetreatFilter(django_filters.FilterSet):
    filter = django_filters.CharFilter(method='custom_filter')

    class Meta:
        model = Retreat
        fields = ['title', 'location', 'price',
                  'duration', 'type', 'condition', 'date']

    def custom_filter(self, queryset, name, value):
        value = value.lower()
        filtered_qs = queryset.filter(title__icontains=value) | queryset.filter(
            location__icontains=value) | queryset.filter(type__icontains=value) | queryset.filter(
            condition__icontains=value
        ) | queryset.filter(date__icontains=value)
        return filtered_qs
