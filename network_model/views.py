from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network_model.filters import StructureFilter
from network_model.models import Structure
from network_model.permissions import IsActiveUser
from network_model.serializers import StructureCreateSerializer, StructureSerializer


class StructureViewSet(viewsets.ModelViewSet):
    queryset = Structure.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StructureFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return StructureCreateSerializer
        else:
            return StructureSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.clean()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.clean()
