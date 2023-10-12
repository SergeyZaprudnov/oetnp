import django_filters

from network_model.models import Structure


class StructureFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Structure
        fields = ['country']
