import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class StudentFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="created_at", lookup_expr='gte')
    end_date=DateFilter(field_name="created_at", lookup_expr='lte')
    name = CharFilter(field_name="admin__first_name", lookup_expr='icontains')
    class Meta:
        model = Students
        fields = ['status','course_id']