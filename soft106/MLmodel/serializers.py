from rest_framework import serializers
from .models import HomePageModel

class HomePageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomePageModel
        fields = ["url"]