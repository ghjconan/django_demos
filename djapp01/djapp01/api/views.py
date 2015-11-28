from rest_framework.viewsets import ModelViewSet
from api import models, serializers


class PeopleViewSet(ModelViewSet):

    queryset = models.People.objects.all()
    serializer_class = serializers.PeopleSerializer
