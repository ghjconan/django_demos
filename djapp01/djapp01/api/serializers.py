from rest_framework import serializers
from api import models


class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.People

